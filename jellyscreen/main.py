from getCast import getMovieCast
from getCastImages import getPeopleImages, download_images

movie_cast : dict = getMovieCast(603692)
print(movie_cast)

for actor in movie_cast:
    response : dict = getPeopleImages(actor["id"])
    download_images(actor["name"], response)