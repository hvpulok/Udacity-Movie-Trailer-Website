'''
Created on Jul 14, 2016

@author: MdKamrulHasanPulok
'''

# define Movie class here
class Movie():
    """ This class provides a way to store Movie related information
    Attributes:
    title (str): Title of the Movie
    storyline (str): Short Story of the Movie
    poster_image_url: Image url link like http://sample_image.com/das32ds32.png
    trailer_youtube_url: trailer video link """
        
    def __init__(self, title, story, poster_url, trailer_url):
        self.title = title
        self.storyline = story
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
        
