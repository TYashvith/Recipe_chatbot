# 🍳 RecipeGenie – AI-Powered Recipe Recommendation Chatbot

## 📌 Overview

**RecipeGenie** is an AI-powered web application that recommends recipes based on ingredients provided by the user.
It combines intelligent matching algorithms with generative AI APIs to deliver relevant and creative recipe suggestions in real-time.

The project demonstrates full-stack development along with AI integration and fallback handling for reliability.

---

## ⚙️ Key Features

* 🔹 Ingredient-based recipe recommendation
* 🔹 Smart ranking of recipes based on relevance
* 🔹 AI-powered suggestions using LLM APIs
* 🔹 Fallback mechanism for high availability
* 🔹 Pagination for handling large recipe sets
* 🔹 Clean and responsive web interface

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS
* **AI APIs:** Gemini API (primary), Groq API (fallback)
* **Data Handling:** JSON-based local recipe dataset
* **Deployment:** Render

---

## 🧠 How It Works

1. User inputs available ingredients
2. System searches local dataset for matching recipes
3. Recipes are ranked based on ingredient overlap and relevance
4. If needed, AI APIs generate additional recipe suggestions
5. Results are displayed with pagination for better UX

---

## 📂 Project Structure

```id="5s4q4o"
recipegenie/
│
├── app.py                 # Main Flask application
├── templates/            # HTML templates
├── static/               # CSS and assets
├── recipes.json          # Local recipe dataset
└── utils/                # Helper functions (ranking, API calls)
```

---

## 🚀 Live Demo

🔗 Deployed on Render (add your link here)

---

## 🎯 Use Cases

* Reduce food waste by suggesting recipes from available ingredients
* Assist users in quick meal planning
* Demonstrate AI integration in real-world applications

---

## 🧠 Key Learning Outcomes

* Building REST-based web applications using Flask
* Integrating multiple AI APIs with fallback logic
* Designing scalable and user-friendly interfaces
* Implementing ranking algorithms for better recommendations

---

## ⚡ Installation & Setup

1. Clone the repository:

   ```
   git clone https://github.com/<your-username>/recipegenie.git
   ```
2. Navigate to the project:

   ```
   cd recipegenie
   ```
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Run the app:

   ```
   python app.py
   ```

---

## 🔐 Environment Variables

Create a `.env` file and add:

```
GEMINI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

---

## 🚀 Future Improvements

* 🔸 Add user authentication
* 🔸 Voice-based input
* 🔸 Nutrition analysis integration
* 🔸 Mobile app version
* 🔸 Recommendation personalization using ML

---

## 👨‍💻 Author

**Yashvith Moolya**
ECE Student 

---

## ⭐ Acknowledgment

This project was built to explore AI-driven applications and real-world problem solving using modern web technologies.
