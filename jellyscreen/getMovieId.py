import requests

def splitFileName(file_name: str) -> tuple:
    return file_name.split(" (")

def getMovieId(file_name: str) -> int:
    title, year = splitFileName(file_name)

    url : str = f"https://api.themoviedb.org/3/search/movie?query={title}&primary_release_year={year}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {readAccessToken}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data