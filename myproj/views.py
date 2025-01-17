from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializers
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

@api_view(['GET'])
def get_articles(request):
    articles= Article.objects.all()
    serializer=ArticleSerializers(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_article(request):
    serializer=ArticleSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)





