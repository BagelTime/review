from django.shortcuts import render
from review.movie.forms import SearchForm
import tmdbsimple as tmdb
from django.conf import settings


#w        return render(request, 'movie/search_result.html', {'results': results})orkaround for now for images
image_base_size = 'http://image.tmdb.org/t/p/w342'

def search(request):
    print "START SEARCH"
    form = SearchForm(request.POST)

    if form.is_valid():
        query = form.cleaned_data['search']
        print "QUERY: %s" % query

        tmdb.API_KEY = settings.TMDB_APIKEY
        movieSearch = tmdb.Search()
        movieSearch.movie(query=query)

        results = []
        for s in movieSearch.results:
            result = {}

            movie = tmdb.Movies(s['id'])
            rating_list = filter(lambda c: c['iso_3166_1'] == 'US', movie.releases()['countries'])
            rating = rating_list[0]['certification'] if rating_list and rating_list[0]['certification'] else None

            result['title'] = s['title'] if s.has_key('title') and s['title'] != None else None
            result['desc'] = s['overview'] if s.has_key('overview') and s['overview'] != None else None
            result['release_date'] = s['release_date'][:4] if s.has_key('release_date') and s[
                                                                                                'release_date'] != None else None
            result['poster_path'] = s['poster_path'] if s.has_key('poster_path') and s['poster_path'] != None else None
            result['rating'] = rating



            results.append(result)

        if results:
            return render(request, 'movie/search_result.html', {'results': results, 'poster_base': image_base_size})
        else:
            return render(request, 'movie/search_result.html', {'results': '', 'poster_base': image_base_size})
    else:
        return render(request, 'movie/search_result.html', {'results': []})