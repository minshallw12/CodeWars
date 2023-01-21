class Movie:
    
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        return self._title

    def get_genre(self):
        return self._genre

    def get_director(self):
        return self._director

    def get_year(self):
        return self._year


movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

class StreamingService:

    def __init__(self, name, catalog={}):
        self._name = name
        self._catalog = catalog

    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie_obj):
        self._catalog[movie_obj.get_title()] = movie_obj
    
    def del_movie(self, title):
        if title in self.get_catalog():
            del self._catalog[title]



stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.del_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

class StreamingGuide:

    def __init__(self):
        self._streaming_list = []

    def add_streaming_service(self, stream_serv_obj):
        self._streaming_list.append(stream_serv_obj)

    def delete_streaming_service(self, stream_serv_name):
        if stream_serv_name in self._streaming_list:
            del self._catalog[stream_serv_name]

    def where_to_watch_movie(self, movie_title):
        data = []
        for streamer in self._streaming_list:
            if movie_title in streamer.get_catalog():
                data.append(movie_title)
                catalog = streamer.get_catalog()
                movie = catalog[movie_title]
                year = movie.get_year()
                data.append(year)
                break
        for streamer in self._streaming_list:
            if movie_title in streamer.get_catalog():
                data.append(streamer.get_name())
        print(data)
        

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch_movie('Home Alone')
print(search_results)
