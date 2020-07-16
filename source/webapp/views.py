from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')

    elif request.method == 'POST':
        add=''
        action = request.POST.get('act')
        one = int(request.POST.get('Firstnumber'))
        two =int(request.POST.get('Secondnumber'))
        print(one)
        print(two)
        if action == "add":
            add=one + two
        elif action =="subtract":
            add=one - two
        elif action=="multiply":
            add = one * two
        elif action=='divide':
            add = one / two
        return render(request, 'article_create.html', {"result":add})




