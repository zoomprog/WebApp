from django.shortcuts import render

posts = [
    {
        'author': 'CorresyMS',
        'title': 'Blog Post1',
        'content': 'First post content',
        'data_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post1',
        'content': 'Second post content',
        'data_posted': 'August 28, 2018'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

