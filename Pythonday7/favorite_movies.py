def main():
    # Create an empty list to store the favorite movies
    favorite_movies = []

    # Prompt the user to enter their favorite movies
    print("Enter your favorite movies one by one. Type 'stop' to finish.")
    while True:
        movie = input("Enter a movie: ")
        if movie.lower() == 'stop':
            break
        favorite_movies.append(movie)

    # Print the list of favorite movies
    print("\nList of favorite movies:")
    for movie in favorite_movies:
        print(movie)

if __name__ == "__main__":
    main()
