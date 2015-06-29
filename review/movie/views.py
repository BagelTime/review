from django.shortcuts import render
from review.movie.forms import SearchForm
import tmdbsimple as tmdb
from django.conf import settings


#workaround for now for images
image_base_size = 'http://image.tmdb.org/t/p/w342'

def search(request):
    form = SearchForm(request.POST)

    if form.is_valid():
        query = form.cleaned_data['search']
        print "QUERY: %s" % query

        tmdb.API_KEY = settings.TMDB_APIKEY
        movieSearch = tmdb.Search()
        movieSearch.movie(query=query)
        results = []
        for s in movieSearch.results:
            result={'title': s['title'],
                    'desc': s['overview'],
                    'release_date': s['release_date'][:4],
                    'poster': "%s%s" % (image_base_size, s['poster_path'])
            }
            results.append(result)

        return render(request, 'movie/search_result.html', {'results': results})