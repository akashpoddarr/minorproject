from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def mainhome(request):
    return render(request, "mainhome.html",{})

def about_team(request):
    return render(request, 'about_team.html', {})