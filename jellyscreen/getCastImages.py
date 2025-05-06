import requests
from dotenv import load_dotenv
import os

load_dotenv()
TMDB_READ_ACCESS_TOKEN : str = os.getenv("TMDB_READ_ACCESS_TOKEN")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_READ_ACCESS_TOKEN}"
}

def download_images(name : str, profiles : list) -> None:
    clean_name : str = name.replace(" ", "")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    save_path : str = os.path.join(current_dir, "actors", clean_name)
    os.makedirs(save_path, exist_ok=True)

    for index, profile in enumerate(profiles):
        url : str = f"https://image.tmdb.org/t/p/original/{profile["file_path"]}"

        response : requests.Response = requests.get(url, headers=headers)
 
        file_extension : str = os.path.splitext(profile["file_path"])[1]
        file_name : str = f"{clean_name}{index}{file_extension}"
        file_path : str = os.path.join(save_path, file_name)

        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

def formatResponse(response : dict) -> list:
    profiles : list = []
    
    for profile in response:
        profiles.append({
            "file_path": profile["file_path"],
        })

    return profiles

def getPeopleImages(person_id : int) -> dict:
    url : str = f"https://api.themoviedb.org/3/person/{person_id}/images"

    try:
        print(f"Fetching people images from TMDB API: {url}")
        response : requests.Response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"API request to {url} failed with error: {e}")
        quit()
    
    data : dict = response.json()

    return formatResponse(data.get("profiles", []))