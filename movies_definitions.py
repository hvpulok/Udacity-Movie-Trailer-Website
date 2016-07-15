'''
Created on Jul 14, 2016

@author: MdKamrulHasanPulok
'''
# This file contains all the movie objects constructed based on video class

import video  #import video module to use Movie class
import fresh_tomatoes  #import fresh_tomatoes script to generate html

# all the movie instances are defined here
the_fountain = video.Movie("The Fountain",
                        "As a modern-day scientist," 
                        " Tommy is struggling with mortality, desperately"
                        "searching for the medical breakthrough that will"
                        "save the life of his cancer-stricken wife, Izzi.",
                        "http://ia.media-imdb.com/images/M/MV5BMTU5OTczMTcxMV5BMl5BanBnXkFtZTcwNDg3MTEzMw@@._V1_SX640_SY720_.jpg",
                        "https://youtu.be/dAuxryJ6pv8")

avatar = video.Movie("Avatar",
                   "A paraplegic marine dispatched to the moon Pandora on"
                   " a unique mission becomes torn between following his"
                   " orders and protecting the world he feels is his home.",
                   "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                   "https://youtu.be/d1_JBMrrYw8")

school_of_rock = video.Movie("School of Rock",
                   "After being kicked out of a rock band, Dewey Finn"
                   " becomes a substitute teacher of a strict elementary"
                   " private school, only to try and turn it into a rock band.",
                   "http://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_.jpg",
                   "https://youtu.be/XCwy6lW5Ixc")

ratatouille = video.Movie("Ratatouille",
                   "A rat who can cook makes an unusual alliance with a "
                   "young kitchen worker at a famous restaurant.",
                   "http://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://youtu.be/c3sBBRxDAqk")

midnigh_in_paris = video.Movie("Midnight in Paris",
                   "While on a trip to Paris with his fiances family, "
                   "a nostalgic screenwriter finds himself mysteriously "
                   "going back to the 1920s everyday at midnight.",
                   "http://ia.media-imdb.com/images/M/MV5BMTM4NjY1MDQwMl5BMl5BanBnXkFtZTcwNTI3Njg3NA@@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
                   "https://youtu.be/BYRWfS2s2v4")

hunger_games = video.Movie("The Hunger Games",
                   "Katniss Everdeen voluntarily takes her younger sister's "
                   "place in the Hunger Games, a televised competition in "
                   "which two teenagers from each of the twelve Districts of"
                   " Panem are chosen at random to fight to the death.",
                   "http://ia.media-imdb.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://youtu.be/mfmrPu43DF8")

avengers = video.Movie("Avengers: Age of Ultron",
                   "When Tony Stark and Bruce Banner try to jump-start a "
                   "dormant peacekeeping program called Ultron, things go "
                   "horribly wrong and it's up to Earth's Mightiest Heroes "
                   "to stop the villainous Ultron from enacting his "
                   "terrible plans.",
                   "http://ia.media-imdb.com/images/M/MV5BMTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_SY1000_SX675_AL_.jpg",
                   "https://youtu.be/tmeOjFno6Do")

ant_man= video.Movie("Ant-Man",
                   "Armed with a super-suit with the astonishing ability to "
                   "shrink in scale but increase in strength, cat burglar "
                   "Scott Lang must embrace his inner hero and help his "
                   "mentor, Dr. Hank Pym, plan and pull off a heist that "
                   "will save the world.",
                   "http://ia.media-imdb.com/images/M/MV5BMjM2NTQ5Mzc2M15BMl5BanBnXkFtZTgwNTcxMDI2NTE@._V1_.jpg",
                   "https://youtu.be/pWdKf3MneyI")

insideOut = video.Movie("Inside Out",
                   "After young Riley is uprooted from her Midwest life "
                   "and moved to San Francisco, her emotions - Joy, Fear, "
                   "Anger, Disgust and Sadness - conflict on how best to "
                   "navigate a new city, house, and school.",
                   "http://ia.media-imdb.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://youtu.be/seMwpP0yeu4")

# define all the movie objects in a list so that it can pass through function
# easily
movies = [the_fountain, avengers, ant_man, avatar, school_of_rock, insideOut, ratatouille, midnigh_in_paris, hunger_games]
#pass movies list to the html generator script
fresh_tomatoes.open_movies_page(movies)

