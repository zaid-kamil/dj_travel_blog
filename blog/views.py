from django.shortcuts import render, redirect

# Create your views here.
def blog_list_view(request):
    return render(
        request,
        'blog_list.html'
    )

def article_view(request, id):
    return render(
        request,
        'article.html'
    )

def edit_article_view(request, id):
    return render(
        request,
        'edit_article.html'
    )

def add_article_view(request):
    return render(
        request,
        'add_article.html'  
    )

def delete_article_view(request, id):
    return redirect('blog_list')