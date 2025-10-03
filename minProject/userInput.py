def get_movie_type():
    options = {
        1: "Action",
        2: "Love",
        3: "Comedy",
        4: "Drama",
        5: "Horror",
        6: "Sci-Fi"
    }
    print("Select the type of movie:")
    for key, value in options.items():
        print(f"{key}. {value}")
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice in options:
                return options[choice]
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a number.")

chos = get_movie_type()
print(f"You selected: {chos}")
# Export the function
__all__ = ['get_movie_type']