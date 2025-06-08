from flask import Flask, render_template, request  # Needed for Flask app and form handling
import pickle  # For loading precomputed data
import numpy as np  # For numerical operations
import pandas as pd  # For working with DataFrames (optional, but useful)
import os

# Get the directory where app.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load the pickled data
popular_df = pickle.load(open(os.path.join(base_dir, 'popular.pkl'), 'rb'))  # Popular books DataFrame
pt = pickle.load(open(os.path.join(base_dir, 'pt.pkl'), 'rb'))  # Pivot table (book-user matrix)
books = pickle.load(open(os.path.join(base_dir, 'books.pkl'), 'rb'))  # Book metadata
similarity_scores = pickle.load(open(os.path.join(base_dir, 'similarity_scores.pkl'), 'rb'))  # Cosine similarity matrix

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_ratings'].values)
    )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


def get_recommendations(book_name):
    # Index fetch - find the book in the pivot table
    try:
        index = np.where(pt.index == book_name)[0][0]
    except IndexError:
        print(f"Book '{book_name}' not found in pivot table.")
        return [["❌ Book not found", "", ""]]

    # Get similarity scores and sort them
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]  # Top 4 similar books (excluding the book itself)

    data = []
    for i in similar_items:
        item = []
        # Get book details from the original books dataframe
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        item.extend(list(temp_df['Book-Title'].values))
        item.extend(list(temp_df['Book-Author'].values))
        item.extend(list(temp_df['Image-URL-M'].values))
        data.append(item)

    print("Recommended books:", data)  # This will now work
    return data


@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    """
    Flask route to handle book recommendation requests
    """
    user_input = request.form.get('user_input')  # Book name from form

    if not user_input:
        return render_template('recommend.html', data=[["❌ No book name provided", "", ""]])

    # Get recommendations using the helper function
    data = get_recommendations(user_input)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)