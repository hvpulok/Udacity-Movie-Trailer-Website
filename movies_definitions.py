'''
Created on Jul 14, 2016

@author: MdKamrulHasanPulok
'''
# This file contains all the movie objects constructed based on video class

import video  #import video module to use Movie class

# all the movie instances as defined here
the_fountain = video.Movie("The Fountain",
                        """ As a modern-day scientist, Tommy is struggling with mortality, desperately searching for the medical breakthrough that will save the life of his cancer-stricken wife, Izzi.""",
                        "http://ia.media-imdb.com/images/M/MV5BMTU5OTczMTcxMV5BMl5BanBnXkFtZTcwNDg3MTEzMw@@._V1_SX640_SY720_.jpg",
                        "https://youtu.be/dAuxryJ6pv8")

print the_fountain.storyline

