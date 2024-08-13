from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.xd1    V1Q-h

posts = [
        {'id':1,'tittle':"Post1","content":"Content of Post1"},
        {'id':2,'tittle':"Post2","content":"Content of Post2"},
        {'id':3,'tittle':"Post3","content":"Content of Post3"},
        {'id':4,'tittle':"Post4","content":"Content of Post4"}
]

def index(request):

    blog_tittle = "Latest Posts"

    try:
        return render(request, "blog/index.html",{'blog_tittle':blog_tittle,'posts':posts})
    except Exception as e:
        print(e)

def details(request,post_id):

    try:
        post = next((item for item in posts if item['id'] == int(post_id)),None)
        return render(request, "blog/detail.html", {'post':post,'posts':posts})  
    except Exception as e:
        print(e)


# for this redirection , using  url name's instead of url's is usefull when we change the url's. for this we use the reverse() funtion from the django.urls.

# 1) without reverse funtion
# def old_url_redirect(request):

#     return redirect('new_url')

# 2) with reverse funtion 
def old_url_redirect(request):

    return redirect(reverse("blog:new_url"))

def new_url(request):

    return HttpResponse("This is an new URL page")