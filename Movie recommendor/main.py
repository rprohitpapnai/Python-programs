import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies=pd.read_csv("ml-20m\movies.csv")
movie=input("enter the movie name:  ")
movies['genres'] = movies['genres'].str.replace('|', ' ')
movies['title'] = movies['title'].str.replace('""', '')
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
movie_indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()
def recommend_similar_movies(movie_title, num_recommendations=5):
    idx = movie_indices[movie_title]
    similar = list(enumerate(cosine_sim[idx]))
    similar = sorted(similar, key=lambda x: x[1], reverse=True)
    similar = similar[1:num_recommendations + 1]
    movie_list = [i[0] for i in similar]
    return movies['title'].iloc[movie_list]
print(recommend_similar_movies(movie,10))
