from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {'movie_list':movie}
    return render(request,'index.html',context)

def detail(request,id):
    # return HttpResponse("This is movie id %s" % movie_id)
    movie=Movie.objects.get(id=id)
    return render(request,'detail.html',{'movie':movie})
def add_movie(request):
    if request.POST:
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form, "movie": movie}
    return render(request,'edit.html',context)
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
