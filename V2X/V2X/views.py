from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 align='center'>Hello, Django in Codespaces! 🎉</h1>")
