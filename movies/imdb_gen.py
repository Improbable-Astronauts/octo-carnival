import random
import time 

import omdb
from .models import Movie



def rando_imdb_id_stab():
    number = random.randint(10**(4), (10**5)-1)
    return "tt00" + str(number)

def propagate_db(num_movies):
    for i in range(num_movies):
        #try:
        movie_dict = omdb.imdbid(rando_imdb_id_stab())
    
        new_movie = Movie.objects.create(title=movie_dict['title'],year=movie_dict['year'],
                        imdb_id=movie_dict['imdb_id'],runtime=movie_dict['runtime'],
                        rated=movie_dict['rated'],)
        #time.sleep(1)
        print("$$$$$$$$$$$$$$$$$$" + new_movie.title)
        new_movie.save()
        print("SAVED")
        #except:

# if __name__ == "__main__":
#     #print(rando_imdb_id_stab())
#     propagate_db(3)
