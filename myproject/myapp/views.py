from django.shortcuts import render

def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def services(request):
    return render(request, 'myapp/services.html')

def contact(request):
    if request.method == 'POST':
        # Обработка данных формы
        pass
    return render(request, 'myapp/contact.html')