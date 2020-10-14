from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article, Category, Picture, Service


def gestion_index(request):

    articles=Article.objects.all()
    images = Picture.objects.filter(title__startswith='about')
    services = Service.objects.all()

    return render(request, 'index.html',  {
                                            'articles':articles,
                                            'images':images,
                                            'services':services
                                           })


def gestion_service(request):
    return render(request, 'services.html', {})


def gestion_blog(request):
    return render(request, 'blogs.html', {})


def gestion_partner(request):
    return render(request, 'partners.html', {})


def gestion_contact(request):
    return render(request, 'contacts.html', {})


def gestion_project(request):
    return render(request, 'projects.html', {})
