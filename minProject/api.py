import requests

def fetch_recent_movies(query):
    url = f"https://imdb.iamidiotareyoutoo.com/search?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)  # <-- Debug: see the structure
        return data
    else:
        print("Failed to retrieve data")

__all__ = ["fetch_recent_movies"]
fetch_recent_movies("action")
