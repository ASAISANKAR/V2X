from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 align='center'>Hello, Django in Codespaces! 🎉</h1>")

from django.shortcuts import render, redirect
from .models import Title
from .forms import TitleForm

def add_title(request):
    if request.method == "POST":
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_titles')  # Redirect to display page after adding
    else:
        form = TitleForm()
    return render(request, 'add_title.html', {'form': form})

def view_titles(request):
    titles = Title.objects.all()
    return render(request, 'view_titles.html', {'titles': titles})
