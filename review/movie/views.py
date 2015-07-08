from django.shortcuts import render
from django.conf import settings
from django.db.models.expressions import Q
from review.movie.forms import SearchForm
from review.movie.models import Genre, Movie
import tmdbsimple as tmdb


#TODO replace with immage config later
image_base_size = 'http://image.tmdb.org/t/p/w342'

#TODO combine common pares of db and remote functions

def db_resulte(item):
    movie_list = Movie.objects.filter(db_id=item['id']).prefetch_related()
    if not movie_list:
        print "Did not find  %s %s in DB" % (item['id'], item['title'])
        return False
    else:
        movie = movie_list[0]
        print "Found %s %s in DB" % (movie.title, movie.db_id)
        result = {
            'title' : movie.title,
            'rating': movie.rating,
            'genres': [g.name for g in movie.genres.all()],
            'desc': item['overview'] if item.has_key('overview') and item['overview'] != None else None,
            'release_date': item['release_date'][:4] if item.has_key('release_date') and item['release_date'] != None else None,
             'poster_path':  item['poster_path'] if item.has_key('poster_path') and item['poster_path'] != None else None,
        }
        ranks = {'ranks': movie.averages()}
        result.update(ranks)
        return result


def remote_result(item):
    print "Looking Up %s %s" % (item['id'], item['title'])
    movie = tmdb.Movies(item['id'])
    rating_list = filter(lambda c: c['iso_3166_1'] == 'US', movie.releases()['countries'])
    rating = rating_list[0]['certification'] if rating_list and rating_list[0]['certification'] else None

    #get genresgenre_ids
    genre_ids = item['genre_ids']
    print "Genres: %s" % genre_ids
    genres = None
    if genre_ids:
        genre_query = Q(pk=genre_ids.pop())
        print genre_query
        for g in genre_ids:
            genre_query |= Q(pk=g)
        genre_list = Genre.objects.filter(genre_query)
        genres = [g.name for g in genre_list]

    result = {
        'title': item['title'] if item.has_key('title') and item['title'] != None else None,
        'desc': item['overview'] if item.has_key('overview') and item['overview'] != None else None,
        'release_date': item['release_date'][:4] if item.has_key('release_date') and item['release_date'] != None else None,
        'poster_path': item['poster_path'] if item.has_key('poster_path') and item['poster_path'] != None else None,
        'rating': rating,
        'genres': genres if genres else [],
    }
    return result

def search(request):
    print "START SEARCH"
    form = SearchForm(request.POST)

    if form.is_valid():
        query = form.cleaned_data['search']
        print "QUERY: %s" % query

        #init tmdb object with API KEY
        tmdb.API_KEY = settings.TMDB_APIKEY

        #do search
        movieSearch = tmdb.Search()
        movieSearch.movie(query=query)

        # build results for template
        results = []
        for s in movieSearch.results:
            # get movie rating for US only default to NR
            print "%s: %s" % (s['id'], s['title'])
            result = db_resulte(s)
            if result:
                results.append(result)
            else:
                result = remote_result(s)
                results.append(result)

        #TODO simplify below

        if results:
            return render(request, 'movie/search_result.html', {'results': results, 'poster_base': image_base_size})
        else:
            return render(request, 'movie/search_result.html', {'results': '', 'poster_base': image_base_size})
    else:
        return render(request, 'movie/search_result.html', {'results': []})