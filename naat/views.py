from django.shortcuts import render
from django.http import HttpResponse
from naat.models import Album,Song
from django.template import loader
from django.shortcuts import render
from django.http import Http404
"""def index(request):
    all_album=Album.objects.all()
    html=''
    for album in all_album:
        url='/naat/'+str(album.id)+'/'
        html+='<a href="'+url+'">'+album.album_title+'</a><br>'
    return HttpResponse(html)

    return HttpResponse("<h1> this is </h1>"+str(a.album_title)+" ok ")
"""
def detail(request,album_id):
    album_sp = Album.objects.get(pk=album_id)
    template = loader.get_template('naat/detail.html')
    fruits = [1, 2, 3, 4]
    context = {
        'album_sp': album_sp,
        'fruits': fruits
    }
    return HttpResponse(template.render(context, request))


def index(request):
    all_albums=Album.objects.all()
    template=loader.get_template('naat/index.html')
    fruits = [1 ,2, 3 ,4]
    context={
        'all_albums':all_albums,
        'fruits':fruits
    }
    return HttpResponse(template.render(context,request))


