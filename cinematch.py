# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:52:27 2024

@author: Adithyash BC
"""

cinema_industries = {
    'Hollywood': 5,
    'Bollywood': 4,
    'Kollywood': 3,
    'Tollywood': 2
}

genres = {
    'Action': 5,
    'Scifi': 4,
    'Mystery': 3,
    'Horror': 2,
    'Comedy': 1
}

directors = cinema_industries.copy()
movies = []

# Function to add a new movie
def add_movie(title, industry, genre, director_industry, actors):
    if industry not in cinema_industries or genre not in genres or director_industry not in directors:
        print("Invalid industry, genre, or director industry. Please check your inputs.")
        return

    industry_score = cinema_industries[industry]
    genre_score = genres[genre]
    director_score = directors[director_industry]
    actor_score = sum(actor['score'] for actor in actors) / len(actors)

    rating = industry_score + genre_score + director_score + actor_score
    movies.append({
        "title": title,
        "industry": industry,
        "genre": genre,
        "director_industry": director_industry,
        "actors": actors,
        "rating": rating
    })

def title_search(title):
    return [movie for movie in movies if title.lower() in movie['title'].lower()]

def genre_search(genre):
    return [movie for movie in movies if genre.lower() in movie['genre'].lower()]

def recomend(n):
    return sorted(movies, key=lambda x: x['rating'], reverse=True)[:n]

def delete_movie(title):
    global movies
    movies = [movie for movie in movies if movie['title'].lower() != title.lower()]
    print(f"Movie '{title}' deleted successfully!")

def display(movie_list):
    for movie in movie_list:
        print(f"Title: {movie['title']}, Industry: {movie['industry']}, Genre: {movie['genre']}, Director Industry: {movie['director_industry']}, Rating: {movie['rating']}")
        print("Actors:")
        for actor in movie['actors']:
            print(f"  Name: {actor['name']}, Score: {actor['score']}")

movie_data = [
   ]

for movie in movie_data:
    add_movie(*movie)

def main_menu():
    while True:
        print("\nCineMatch - Movie Recommendation System")
        print("1. Add a New Movie")
        print("2. search movie by title")
        print("3. search movie by genre")
        print("4. Recommend top movies")
        print("5. Delete a movie")
        print("6. Display sl movie")
        print("7. Exit")
        
        choice = input("Enter a number(1-7): ")

        if choice == '1':
            title = input("Enter movie title: ")
            industry = input("Enter cinema industry (Hollywood, Bollywood, Kollywood, Tollywood): ")
            genre = input("Enter movie genre (Action, Scifi, Mystery, Horror, Comedy): ")
            director_industry = input("Enter director industry (Hollywood, Bollywood, Kollywood, Tollywood): ")
            actors_count = int(input("Enter number of actors: "))
            actors = [{"name": input("Enter actor name: "), "score": int(input("Enter actor score (1-5): "))} for _ in range(actors_count)]
            add_movie(title, industry, genre, director_industry, actors)
        elif choice == '2':
            title = input("Enter movie title to search: ")
            results = title_search(title)
            if results:
                display(results)
            else:
                print("No movies found with that title.")
        elif choice == '3':
            genre = input("Enter movie genre to search: ")
            results = genre_search(genre)
            if results:
                print("Movies found:")
                display(results)
            else:
                print("No movies found with that genre.")
        elif choice == '4':
            n = int(input("Enter the number of movies to recommend: "))
            results = recomend(n)
            if results:
                print("Top Movies:")
                display(results)
            else:
                print("No recommendation.")
        elif choice == '5':
            title = input("Enter movie title to delete: ")
            delete_movie(title)
        elif choice == '6':
            if movies:
                print("Done.")
                display(movies)
            else:
                print("Nothing to delete")
        elif choice == '7':
            print("BYEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Execute the main menu
main_menu()





