# ✨ AI Story Generator

A Streamlit-based web application that uses the **Groq API with LLaMA 3** to generate short, creative stories from user prompts. Just enter your idea, and let the AI turn it into a vivid short story.

---

## 🚀 Live Demo

👉 [Open the App]([https://shanmukha18-ai-story-generator.streamlit.app](https://ai-story-generator-xuuytgtfp3yyvtt4xtadoc.streamlit.app/))

---

## 📌 Features

* 🧠 AI-generated short stories using Groq’s LLaMA 3 model
* ✍️ Creative writing based on any prompt
* ⚡ Fast and responsive interface built with Streamlit
* 🔐 Secure API key management with `.env` locally and Streamlit Secrets on deployment

---

## 💠 Tech Stack

* [Streamlit](https://streamlit.io/) – UI framework
* [Groq API](https://console.groq.com/) – LLaMA 3 model
* [Python](https://www.python.org/)
* `requests`, `python-dotenv`

---

## 📅 Local Installation

Follow these steps to run the app locally on your machine:

1. **Clone this repository:**

```bash
git clone https://github.com/Shanmukha18/ai-story-generator.git
cd ai-story-generator
```

2. **(Optional) Create a virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

4. **Set up the `.env` file:**

Create a `.env` file in the root directory with your Groq API key:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

5. **Run the app:**

```bash
streamlit run app.py
```

---

## 🎞️ Project Working

1. Open the web app.
2. Enter a story prompt in the input box (e.g., "A dragon who loves gardening").
3. Click the **Generate Story** button.
4. The app sends your prompt to Groq's LLaMA 3 model via API.
5. The generated story is displayed below the input field.

---

## 📸 Screenshots

### 📚 Home Screen

![Home Screen](https://github.com/user-attachments/assets/fd7e369d-912e-4d65-9b63-0f1da5f30020)


### 💭 Story Output Example

![Prompt and Output](https://github.com/user-attachments/assets/2f856cf6-e951-4b26-9df6-df4b72168de2)


![Generated Story](https://github.com/user-attachments/assets/9e763bbe-02e3-48e0-9359-17871e1b2bbd)


---

## 🙌 Author

Made by [Shanmukha Thadavarthi](https://github.com/Shanmukha18) using Groq API.

---

## 📋 License

This project is licensed under the [MIT License](LICENSE).

---

## 📢 Feedback or Contributions?

Feel free to open issues or submit pull requests. All contributions are welcome!
