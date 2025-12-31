from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required

from .models import ArticleItem
from django.utils import timezone

# Create your views here.
@login_required
def user_admin(request):

    articles = ArticleItem.objects.all()

    context = {
        'articles' : articles
    }

    return render(request, 'user_admin.html', context)
    # return HttpResponse("ADMIN VIEW")


@login_required
def edit_article(request, article_id):

    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")

        

    article = ArticleItem.objects.filter(id=article_id).first()

    context = {
        'article' : article
    }

    return render(request, 'edit_article.html', context)
    # return HttpResponse(f"admin edit of article {article_id}")


@login_required
def new_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            ArticleItem.objects.create(
                title=title,
                content=content,
                published_date=timezone.now()
            )

    return render(request, 'new_article.html')
    # return HttpResponse('new article')