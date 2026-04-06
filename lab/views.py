from django.shortcuts import render, redirect
from .models import Comment

def reflected_xss(request):
    query = request.GET.get('q', '')
    return render(request, 'reflected.html', {'query': query})

def stored_xss(request):
    if request.method == "POST":
        content = request.POST.get('content')
        Comment.objects.create(text=content)
        return redirect('stored_xss')

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'stored.html', {'comments': comments})
def index(request):
    return render(request, 'index.html')