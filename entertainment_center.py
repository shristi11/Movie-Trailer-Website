import fresh_tomatoes
import media

# creating instances of Class Movie from media
the_commuter = media.Movie("THE COMMUTER",
                      "https://upload.wikimedia.org/wikipedia/en/4/4a/The_Commuter_film_poster.jpg",
                      "https://www.youtube.com/watch?v=lPB2FCMg0vI")
                      
wonder_woman = media.Movie("WONDER WOMAN",
                     "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                     "https://www.youtube.com/watch?v=VSB4wGIdDwo")

beauty = media.Movie("Beauty and the Beast",
                     "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                     "https://www.youtube.com/watch?v=e3Nl_TCQXuw")


wonderstruck = media.Movie("Wonderstruck",
                     "https://upload.wikimedia.org/wikipedia/en/0/0c/Wonderstruck_film_poster.jpg",
                     "https://www.youtube.com/watch?v=nu8X9ALV4fo")

chef = media.Movie("Chef",
                     "https://upload.wikimedia.org/wikipedia/en/b/b8/Chef_2014.jpg",
                     "https://www.youtube.com/watch?v=FF_rYNupPwg")

the_snowman = media.Movie("The SnowMan",
                          "https://upload.wikimedia.org/wikipedia/en/0/08/The_Snowman_%282017%29_poster.jpg",
                          "https://www.youtube.com/watch?time_continue=2&v=LkD_Z3ujqIc")

# assign all the Movie instances to movies list
movies = [the_commuter, wonder_woman, beauty, wonderstruck, chef, the_snowman]

# call open page method and assign movies list as argument
fresh_tomatoes.open_movies_page(movies)


