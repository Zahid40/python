def movieDb(movie):
    try:
        if len(movie) < 3:
            raise ValueError("Movie name is too short")
        print("Hello fetching movie details......")
    except Exception as e:
        print(e)
    finally:
        print("Closing !")


movie = input("Enter Movie name : ")
movieDb(movie)
