from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')
def error404(request, exception):
    return render(request, 'error_pages/e404')

def error403(request, exception):
    return render(request, 'error_pages/e403')

def error400(request, exception):
    return render(request, 'error_pages/e400')

def error500(request):
    return render(request, 'error_pages/e500')
