from django.http import HttpResponse
from django.shortcuts import render


def home_view(request) -> HttpResponse:
    """View для страницы home."""
    return render(request, 'menu/home.html')


def about_view(request) -> HttpResponse:
    """View для страницы about."""
    return render(request, 'menu/about.html')


def careers_view(request) -> HttpResponse:
    """View для страницы careers."""
    return render(request, 'menu/careers.html')


def our_team_view(request) -> HttpResponse:
    """View для страницы our_team."""
    return render(request, 'menu/our_team.html')
