from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Article, STATUS_CHOICES
from django.http import HttpResponseNotAllowed, Http404

from webapp.models import Article, STATUS_CHOICES
from webapp.forms import ArticleForm

def index_view(request):

    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def article_create(request, pk):
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     raise Http404

    article = get_object_or_404(Article, pk=pk)

    context = {'article': article}
    return render(request, 'article_create.html', context)


def article_view(request):
    if request.method == "GET":
        return render(request, 'article_view.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get('description')
        maxdescription = request.POST.get('maxdescription')
        status = request.POST.get('status')
        date_completion = request.POST.get('date_completion')
        article = Article.objects.create(description=description,maxdescription=maxdescription, status=status,date_completion=date_completion)
        return redirect('article_create', pk=article.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={'article': article})
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.author = request.POST.get('author')
        article.text = request.POST.get('text')
        article.save()
        return redirect('article_view', pk=article.pk)




