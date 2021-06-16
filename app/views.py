import random

from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from app.models import *
from django.contrib import auth


def paginate(objects_list, request, per_page=5):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    question = paginate(Question.objects.newest(), request)
    return render(request, 'index.html', {'questions': question})


def hot(request):
    question = paginate(Question.objects.most_popular(), request)
    return render(request, 'index.html', {'questions': question})


def ask(request):
    return render(request, 'ask.html', {})


def login(request):
    return render(request, 'login.html', {})


def question(request, pk):
     question = Question.objects.by_id(pk).first()
     answers = question.answers.hot()
     return render(request, "question.html", {"question": question, "answers": answers})


def registration(request):
    return render(request, 'registration.html', {})

def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('next', '/'))

def settings(request):
    return render(request, 'settings.html', {})


def tag(request, tag):
    question = paginate(Tag.objects.question_by_tag(tag), request)
    return render(request, 'tag.html', {'questions': question, "tag": tag})

