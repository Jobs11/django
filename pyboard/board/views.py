from django.shortcuts import render, redirect
from board.models import Board
from django.views.decorators.csrf import csrf_exempt
import os
from urllib.parse import quote as urlquote
from django.http.response import HttpResponse

# Create your views here.

UPLOAD_DIR = 'c:/upload/'

def list(request):
    boardCount = Board.objects.all().count()
    boardList = Board.objects.all().order_by("-bno")
    return render(request, 'board/list.html', {"boardList": boardList, "boardCount":boardCount})

def register(request):
    return render(request, 'board/register.html')

@csrf_exempt
def insert(request):
    fname=''
    fsize=0
    
    if 'file' in request.FILES:
        
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
         
        fp = open("%s%s"%(UPLOAD_DIR, fname), 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
        
    t = request.POST['title']
    w = request.POST['writer']
    c = request.POST['content']
    dto = Board(title=t, writer=w, content=c, filename=fname, filesize=fsize)
    dto.save()
    return redirect('/list/')
    

def download(request):
    no = request.GET['bno']
    dto = Board.objects.get(bno=no)
    path = UPLOAD_DIR+dto.filename
    filename = os.path.basename(path)
    filename = urlquote(filename)
    with open(path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/actet-stream')
        response['Content-Disposition']="attachment;filename*=UTF-8''{0}".format(filename)
        
    dto.down_up()
    dto.save()
    return response