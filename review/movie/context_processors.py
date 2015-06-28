from review.movie.forms import SearchForm

def search(request):
    return {'search_form': SearchForm()}