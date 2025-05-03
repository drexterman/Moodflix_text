from text_emotion.text import text
from movie_recommender.recommender import recommend_top_movies_for_mood


prompt = input("Describe your mood in a sentence: ")
if not prompt:
    prompt = "I am feeling happy and excited today!"

#get your mood vector
mood_vector = text(prompt)

#get your top movies
movies = recommend_top_movies_for_mood(mood_vector,10)

#print the top 10 movies
print("Top 10 Movies for your mood:")
print(movies)