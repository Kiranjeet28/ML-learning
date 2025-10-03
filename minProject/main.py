import pandas as pd
import matplotlib.pyplot as plt
from userInput import get_movie_type
from api import fetch_recent_movies

def process_movies(data):
    if not data or not data.get('description'):
        print("No movies found!")
        return None, None
    
    # Convert to DataFrame - the actual movie data is in 'description' key
    df = pd.DataFrame(data['description'])
    
    # Select useful columns
    full_table = df[['#TITLE', '#YEAR', '#RANK', '#ACTORS']]
    
    # Top 3 movies by rank (smallest rank numbers are better)
    top3 = df.nsmallest(3, '#RANK')[['#TITLE', '#YEAR', '#RANK', '#ACTORS']]
    
    return full_table, top3

# Usage
input_type = get_movie_type()
data = fetch_recent_movies(input_type)

full_table, top3 = process_movies(data)

if full_table is not None:
    print("\n--- Full Movies Data ---")
    print(full_table.to_string(index=False))
    
    print("\n--- Top 3 by Ranking ---")
    print(top3.to_string(index=False))

    # Optional: visualization
    plt.figure(figsize=(8,5))
    plt.barh(top3['#TITLE'], top3['#RANK'], color='skyblue')
    plt.xlabel("Ranking (lower = better)")
    plt.title("Top 3 Ranked Movies")
    plt.gca().invert_yaxis()
    plt.show()
