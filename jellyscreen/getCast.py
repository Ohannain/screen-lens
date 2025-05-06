import requests
from dotenv import load_dotenv
import os

load_dotenv()
TMDB_READ_ACCESS_TOKEN : str = os.getenv("TMDB_READ_ACCESS_TOKEN")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_READ_ACCESS_TOKEN}"
}

def formatResponse(response : dict) -> list:
    actors : list = []
    
    for actor in response:
        actors.append({
            "id": actor["id"],
            "name": actor["name"],
            "character": actor["character"],
            "profile_path": actor["profile_path"]
        })

    return actors

def getMovieCast(movie_id : int) -> dict:
    url : str = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"

    try:
        print(f"Fetching movie cast from TMDB API: {url}")
        response : requests.Response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"API request to {url} failed with error: {e}")
        quit()

    data : dict = response.json()

    return formatResponse(data.get("cast", []))