from django.shortcuts import render, HttpResponse

from admin_only.models import ArticleItem

# Create your views here.
def home(request):

    article_list = ArticleItem.objects.all()

    context = {
        'articles': article_list
    }
    return render(request, 'home.html', context)


def view_article(request, article_id):

    # get article with relevqnt id

    try:
        article_item = ArticleItem.objects.filter(id=article_id).first()
    except:
        article_item = None
    context = {
        'article' : article_item
    }
    
    return render(request, 'article.html', context)
