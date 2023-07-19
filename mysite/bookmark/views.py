from django.shortcuts import render
from bookmark.models import Bookmark
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


def list(request):
    #select * from bookmark_bookmark order by title
    urlList=Bookmark.objects.all().order_by("title")
    #select count(*) from bookmark_bookmark
    urlCount =Bookmark.objects.all().count()
    return render(request,"bookmark/list.html", {"urlList":urlList, "urlCount":urlCount})
# class BookmarkLV(ListView):
#     model = Bookmark
#
# class BookmarkDV(DetailView):
#     model = Bookmark

def detail(request):
    #get 방식 변수 받아오기 request.GET["변수명"]
    #post 방식 변수 받아오기 request.POST["변수명"]
    addr=request.GET["url"]
    #select * from bookmark_bookmark where url="..."
    dto=Bookmark.objects.get(url=addr)
    #detail.html로 포워딩
    return render(request, "bookmark/detail.html", {"dto":dto})