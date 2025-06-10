from flask import Flask, render_template, request  
import pickle  
import numpy as np  
import pandas as pd  
import os


base_dir = os.path.dirname(os.path.abspath(__file__))


popular_df = pickle.load(open(os.path.join(base_dir, 'popular.pkl'), 'rb'))  
pt = pickle.load(open(os.path.join(base_dir, 'pt.pkl'), 'rb'))  
books = pickle.load(open(os.path.join(base_dir, 'books.pkl'), 'rb'))  
similarity_scores = pickle.load(open(os.path.join(base_dir, 'similarity_scores.pkl'), 'rb'))  

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
    
    try:
        index = np.where(pt.index == book_name)[0][0]
    except IndexError:
        print(f"Book '{book_name}' not found in pivot table.")
        return [[" Book not found", "", ""]]

    
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]  

    data = []
    for i in similar_items:
        item = []
        
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        item.extend(list(temp_df['Book-Title'].values))
        item.extend(list(temp_df['Book-Author'].values))
        item.extend(list(temp_df['Image-URL-M'].values))
        data.append(item)

    print("Recommended books:", data)  
    return data


@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    """
    Flask route to handle book recommendation requests
    """
    user_input = request.form.get('user_input')  

    if not user_input:
        return render_template('recommend.html', data=[[" No book name provided", "", ""]])

    
    data = get_recommendations(user_input)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)