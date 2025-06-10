# 📚 Book Recommender System 📖

This project is a collaborative filtering-based book recommender system built with **HTML**, **Bootstrap CSS**, and **Flask**. It helps users discover new books by suggesting similar titles based on their preferences and also provides a list of the most popular books.

---

## ✨ Features

- **Collaborative Filtering:** Recommends books based on user-item interactions and similarities.
- **Cosine Similarity & Euclidean Distance:** Utilizes these metrics to find books similar to a given book.
- **Popularity-Based Recommendations:** Displays the top 50 most popular books on the platform.
- **User-Friendly Interface:** Built with HTML and Bootstrap for a clean and responsive design.

---

## 💾 Dataset

The system uses the **Book Recommendation Dataset** from Kaggle, which includes information about books, users, and ratings.

---

## 🛠️ Technologies Used

- **Python:** Backend logic and data processing.
- **Flask:** Web framework for building the application.
- **HTML:** Structure of the web pages.
- **Bootstrap CSS:** Styling and responsive design.
- **Jinja2:** Templating engine for rendering HTML.
- **Pandas:** Data manipulation and analysis.
- **Scikit-learn:** For calculating cosine similarity (and potentially other machine learning utilities).

---

## 🚀 Usage

- **Search for a book:** Enter the name of a book in the search bar to find similar recommendations.
- **Explore popular books:** Browse the "Top 50 Books" section for widely enjoyed titles.

---

## 📁 Project Structure

```
Book-Recommender/                    # Main project directory
├── .idea/                          # IDE specific files (e.g., PyCharm)
├── templates/                      # HTML templates
│   ├── index.html                  # Home page template
│   └── recommendations.html        # Recommendations page template
├── app.py                          # Main Flask application file
├── books.pkl                       # Pickled data for books (likely DataFrame)
├── popular.pkl                     # Pickled data for popular books
├── pt.pkl                          # Pickled data for pivot table (user-item matrix)
├── similarity_score.pkl            # Pickled data for similarity scores
└── README.md                       # This README file
```



