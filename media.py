import webbrowser

class Movie():
    
    def __init__(self, movie_title, poster_image, trailer_youtube):
        #populating attributes of self object
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        #opening trailer of movie in youtube
        webbrowser.open(self.trailer_youtube_url)
        
