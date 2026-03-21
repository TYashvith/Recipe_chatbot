from flask import Flask, render_template, request, jsonify
import json
import re
from google import genai

app = Flask(__name__)

# ── Gemini setup ──────────────────────────────────────────────
GEMINI_API_KEY = "Enter your Gemini Api Key Here"

client = genai.Client(api_key=GEMINI_API_KEY)

# ── Load local recipes ────────────────────────────────────────
with open("recipes.json") as f:
    recipes = json.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"].lower()

    # 1. Try matching from local recipes.json first
    results = []
    for recipe in recipes:
        for ingredient in recipe["ingredients"]:
            if ingredient in user_input:
                results.append(recipe)
                break

    if results:
        return jsonify(results)

    # 2. No local match → ask Gemini
    prompt = f"""
You are a helpful recipe assistant. The user has these ingredients: {user_input}

Suggest 2 simple recipes they can make. Respond ONLY with a valid JSON array. No markdown, no code fences, no explanation — just the raw JSON array like this:

[
  {{
    "name": "Recipe Name",
    "ingredients": ["ingredient1", "ingredient2", "ingredient3"],
    "time": "15 min",
    "steps": "Step 1. Step 2. Step 3."
  }},
  {{
    "name": "Recipe Name 2",
    "ingredients": ["ingredient1", "ingredient2"],
    "time": "10 min",
    "steps": "Step 1. Step 2."
  }}
]

Only use the ingredients the user mentioned plus basic pantry staples like salt, oil, water. Keep it beginner-friendly.
"""

    # Try models in order — fallback if one is quota-exhausted
    models_to_try = [
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
    ]

    raw = None
    for model_name in models_to_try:
        try:
            print(f"Trying model: {model_name}")
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            raw = response.text.strip()
            print(f"\n=== GEMINI RAW RESPONSE ({model_name}) ===")
            print(raw)
            print("==========================================\n")
            break  # success — stop trying other models

        except Exception as e:
            print(f"Model {model_name} failed: {e}")
            raw = None
            continue

    if not raw:
        return jsonify({
            "response": "All AI models are currently quota-limited. Please wait a minute and try again!"
        })

    try:
        # Strip markdown fences if present
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        raw = raw.strip()

        # If Gemini returned an object instead of array, extract the array
        if raw.startswith("{"):
            match = re.search(r'\[.*\]', raw, re.DOTALL)
            if match:
                raw = match.group(0)

        ai_recipes = json.loads(raw)

        for r in ai_recipes:
            r["ai_generated"] = True

        return jsonify(ai_recipes)

    except json.JSONDecodeError as e:
        print("JSON parse error:", e)
        print("Raw that failed:", raw)
        return jsonify({
            "response": "I got a response but couldn't read it properly. Please try again!"
        })


if __name__ == "__main__":
    app.run(debug=True)
