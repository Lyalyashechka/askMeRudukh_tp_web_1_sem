from django.shortcuts import render

questions = [
    {
        'id' : idx,
        'title' : f'Title number {idx}',
        'text' : f'Some text for question #{idx}'
    } for idx in range (10)
]


def index(request):
    return render(request, 'index.html', {'questions': questions})

def ask(request):
    return render(request, 'ask.html', {})

def login(request):
    return render(request, 'login.html', {})

def question(request, pk):
     question = questions[pk]
     return render(request, "question.html", {"question": question})

def registration(request):
    return render(request, 'registration.html', {})

def settings(request):
    return render(request, 'settings.html', {})

def tag(request):
    return render(request, 'tag.html', {})

