import pandas as pd
import faiss
import numpy as np

df = pd.read_csv('mood_movies.csv')

def query_movies_by_emotion(mood_vector, top_k=1000, index_path="movie_emotion_index.faiss"):
    # Load the FAISS index
    index = faiss.read_index(index_path)  # load the index.
    mood_vector = np.array(mood_vector, dtype='float32').reshape(1, -1)
    faiss.normalize_L2(mood_vector)
    distances, indices = index.search(mood_vector, top_k)
    results = df.iloc[indices[0]].copy()
    results['similarity'] = distances[0]
    return results[['title','popularity','runtime','genres','original_language','similarity']]

#print(df.head(10))