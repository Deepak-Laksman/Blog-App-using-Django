from django.shortcuts import render

posts = [
    {
        "author" : "CoreyMS",
        "title" : "Blog Post 1",
        "content" : "First Post Content",
        "date_posted" : "Aug 27th 2018"
    },
    {
        "author" : "JaneDoe",
        "title" : "Blog Post 2",
        "content" : "Second Post Content",
        "date_posted" : "Aug 28th 2018"
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {"title" : "About"})