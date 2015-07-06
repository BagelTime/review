from django.shortcuts import render
from django.conf import settings
from django.db.models.expressions import Q
from review.movie.forms import SearchForm
from review.movie.models import Genre
import tmdbsimple as tmdb

#TODO replace with immage config later
image_base_size = 'http://image.tmdb.org/t/p/w342'

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
            result = {}

            # get movie rating for US only default to NR
            movie = tmdb.Movies(s['id'])
            rating_list = filter(lambda c: c['iso_3166_1'] == 'US', movie.releases()['countries'])
            rating = rating_list[0]['certification'] if rating_list and rating_list[0]['certification'] else None

            #get genres
            genre_ids = s['genre_ids']
            genres = None
            if genre_ids:
                genre_query = Q(pk=genre_ids.pop())
                for g in genre_ids:
                    genre_query |=Q(pk=g)
                genre_list = Genre.objects.filter(genre_query)
                genres = [g.name for g in genre_list]

            result['title'] = s['title'] if s.has_key('title') and s['title'] != None else None
            result['desc'] = s['overview'] if s.has_key('overview') and s['overview'] != None else None
            result['release_date'] = s['release_date'][:4] if s.has_key('release_date') and s[
                                                                                                'release_date'] != None else None
            result['poster_path'] = s['poster_path'] if s.has_key('poster_path') and s['poster_path'] != None else None
            result['rating'] = rating
            result['genres'] = genres if genres else None


            results.append(result)

        if results:
            return render(request, 'movie/search_result.html', {'results': results, 'poster_base': image_base_size})
        else:
            return render(request, 'movie/search_result.html', {'results': '', 'poster_base': image_base_size})
    else:
        return render(request, 'movie/search_result.html', {'results': []})