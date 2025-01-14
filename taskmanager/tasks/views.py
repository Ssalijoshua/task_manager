from django.shortcuts import render


def home(request):
    return render(request, 'tasks/home.html')  # Renders the home.html template

def help(request):
    return render(request, 'tasks/help.html')  # Renders the help.html template
