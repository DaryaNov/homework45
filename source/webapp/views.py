from django.shortcuts import render
from webapp.models import Article, STATUS_CHOICES

def index_view(request):

    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def article_view(request):
    if request.method == "GET":
        return render(request, 'article_view.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_completion = request.POST.get('date_completion')
        article = Article.objects.create(description=description, status=status,date_completion=date_completion)
        context = {'article': article}
        return render(request, 'article_create.html', context)




