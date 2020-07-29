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
            'form': ArticleForm()
         })
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                description=form.cleaned_data['description'],
                maxdescription=form.cleaned_data['maxdescription'],
                status=form.cleaned_data['status'],
                date_completion=form.cleaned_data['date_completion']
            )
            return redirect('article_create', pk=article.pk)
        else:
            return render(request, 'article_view.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        form = ArticleForm(initial={
            'description': article.description,
            'maxdescription': article.maxdescription,
            'status': article.status,
            'date_completion': article.date_completion
        })
        return render(request, 'article_update.html', context={
            'form': form,
            'article': article
        })
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            # Article.objects.filter(pk=pk).update(**form.cleaned_data)
            article.description = form.cleaned_data['description']
            article.maxdescription = form.cleaned_data['maxdescription']
            article.status = form.cleaned_data['status']
            article.date_completion = form.cleaned_data['date_completion']
            article.save()
            return redirect('article_create', pk=article.pk)
        else:
            return render(request, 'article_update.html', context={
                'article': article,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
       return render(request, 'article_delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')





