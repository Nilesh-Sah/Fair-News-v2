from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
# Create your views here.

def home(request):
    return render(request, 'myproj/home.html')
     
def index(request):
    articles=Article.objects.order_by('-published_date') #latest article first
    return render(request, 'myproj/index.html', {'articles':articles})     

def article_detail(request, article_id):
    article=get_object_or_404(Article, id=article_id)
    return render(request, 'myproj/details.html', {'article':article})

def create_article(request):
    if request.method =='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, 'myproj/create.html', {'form': form})

def article_list(request):
    articles=Article.objects.order_by('-published_date')
    return render(request, 'myproj/index.html', {'articles':articles})
