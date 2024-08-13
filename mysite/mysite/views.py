from django.shortcuts import render
from django.http import HttpResponseServerError

def custom_page_not_found(request, exception):

    # return render(request, '404.html',status=404)
    try:
        return render(request, '404.html', status=404)
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {e}")