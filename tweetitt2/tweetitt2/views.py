from django.shortcuts import render

def home(request):
    print request
    v = "mi variable"
    v2 = {"Usuario":"Christian"}
    return render(request, "home.html", {'v':v, 'v2':v2})
