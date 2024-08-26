from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def blog_list_view(request):
    return render(
        request,
        'blog_list.html',
        context={
            'articles': Article.objects.all()
        }
    )

def article_view(request, id):
    return render(
        request,
        'article.html',
        context={
            'article' : Article.objects.get(id=id)
        }
    )

def edit_article_view(request, id):
    article = Article.objects.get(id=id)        # Get the article
    form = ArticleForm(instance=article)        # create form with article
    if request.method == 'POST':                # if form is submitted
        form = ArticleForm(request.POST, request.FILES, instance=article) # create form with submitted data
        if form.is_valid():                     # if form is valid
            article = form.save(commit=False)   # save form data to article
            article.author = request.user       # set author to current user
            article.save()                      # save article
            return redirect('blog_list')        # redirect to blog list
    return render(
        request,
        'edit_article.html',
        context = {
            'form': form
        }
    )

def add_article_view(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('blog_list')
    return render(
        request,
        'add_article.html',
        context = {
            'form': form
        }
    )

def delete_article_view(request, id):
    try:
        article = Article.objects.get(id=id)
        article.delete()
    except Article.DoesNotExist:
        print('Article does not exist')
        pass
    return redirect('blog_list')