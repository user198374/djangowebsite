from django.shortcuts import render
from .models import Article

# Create your views here.

def blog_index(request):
    articles = Article.objects.all()  # Récupère tous les articles de la base de données
    data = {'articles': articles}  # Prépare les données à envoyer au template
    return render(request, 'blog/blog_index.html', data)  # Transmets les articles au template

def article(request, name):
    try:
        article = Article.objects.get(title=name)
        data = {'article': article}
    except:
        data = {'message': "l'article demandé n'existe pas."}
    return render(request, 'blog/article.html', data)

