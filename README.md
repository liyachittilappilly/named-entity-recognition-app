# 🌸 Named Entity Recognition Web App

This is a simple and beautiful Named Entity Recognition (NER) web application built using **Python**, **Flask**, and **spaCy**. It allows users to upload `.txt` files and highlights named entities such as people, organizations, dates, etc., in the text using spaCy's powerful NLP engine.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/Flask-Web_Framework-green.svg" />
  <img src="https://img.shields.io/badge/spaCy-NLP_Library-purple.svg" />
</p>

## 🧠 Features

- Upload `.txt` files for entity recognition.
- View original and annotated text side-by-side.
- Supports English NER using `en_core_web_sm`.
- Styled with a soft pink aesthetic for a polished user interface.

## 🚀 Demo

<img src="Named Entity Recognition App.jpg" alt="NER App Screenshot" width="700">

## 🔧 Technologies Used

- Python 3
- Flask
- spaCy
- HTML5 + Bootstrap 5 (for UI)

## 📦 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/ner-web-app.git
cd ner-web-app
```

## 2. **Create a Virtual Environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the Dependencies**

```bash
pip install -r requirements.txt
```

4. **Download spaCy Model**

```bash
python -m spacy download en_core_web_sm
```

5. **Run the App**

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 📁 Project Structure

```
ner-web-app/
│
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # HTML frontend template
├── static/                # (Optional) CSS/JS/images if needed
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 📝 Example Entities Recognized

* **PERSON** – People, including fictional.
* **ORG** – Companies, agencies, institutions.
* **GPE** – Countries, cities, states.
* **DATE** – Absolute or relative dates.

*For more info, see [spaCy Named Entities](https://spacy.io/api/annotation#named-entities)*

## 💖 UI Aesthetic

The interface uses a soft pink theme with Georgia font to create an elegant and user-friendly experience. Designed with both functionality and beauty in mind.

## 📌 TODO

* Add support for more languages or models.
* Save past uploads and results.
* Option to paste text directly instead of uploading files.

## 🙌 Acknowledgements

Special thanks to [AI with Noor] [(https://youtu.be/gko4WnAgzz4?feature=shared)] for the tutorial inspiration.



## 🧑‍💻 Author

Developed by Liya S Chittilappilly 💻
Feel free to connect or contribute!

