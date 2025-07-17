Here is your **cleaned-up and combined content** as **one copy-paste-ready `README.md` file** — fully integrated and structured properly.

---

```markdown
# Flaskgram

Flaskgram is a lightweight Instagram-like web application built using Flask. It allows users to register, log in, and post images with captions. It includes basic image handling, user authentication, and a responsive web interface — perfect for learning full stack Flask development.

---

## 🚀 Features

- ✅ User Registration & Login  
- 🖼️ Image Upload with Captions  
- 🗑️ Post Deletion  
- 📏 Image Resizing (max 800x800)  
- 🧠 EXIF Orientation Handling  
- 🔐 Flask-Login based Session Management  
- 🧰 SQLite DB with SQLAlchemy ORM  
- 🧼 Random Image Name Generator  
- 📱 Responsive Frontend with Bootstrap  

---

## 🛠️ Tech Stack

- Python  
- Flask  
- SQLAlchemy  
- Flask-WTF  
- Flask-Login  
- Pillow (Image Processing)  
- SQLite  
- Bootstrap  

---

## 📁 Project Structure

```

flaskgram/
├── .venv/                 # Python virtual environment
├── app/                  # Main Flask app package
│   ├── templates/        # HTML templates
│   ├── static/           # CSS, images, etc.
│   ├── routes.py         # Route definitions
│   ├── models.py         # Database models
│   └── forms.py          # WTForms classes
├── instance/
│   └── site.db           # SQLite database file
├── migrations/           # Flask-Migrate scripts
├── .gitignore
├── requirements.txt
└── run.py                # Entry point

````

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pranavchikte/Flaskgram.git
   cd Flaskgram
````

2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate    # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**

   ```bash
   flask db upgrade
   ```

5. **Run the app**

   ```bash
   python run.py
   ```

   App will be live at: [http://localhost:5000](http://localhost:5000)

---

## 🖼️ Image Handling

* Only JPEG and PNG formats supported
* Images are resized to 800x800 px max
* EXIF orientation is preserved
* Images stored under: `static/uploads/`
* Filenames are converted to secure random hex strings

---

## 🙌 Usage

* Register a new account
* Log in with your credentials
* Upload an image with a caption
* View and delete your posts

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch:

   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Make changes and commit:

   ```bash
   git commit -m "Add amazing feature"
   ```
4. Push to GitHub and create a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 🌐 Author

Built with 💻 by [Pranav Chikte](https://github.com/Pranavchikte)

