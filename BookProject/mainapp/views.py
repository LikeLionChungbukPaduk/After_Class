from urllib import request
from django.shortcuts import render,redirect
from .models import Post
# Create your views here.
def home(request):
    postlist=Post.objects.all()
    return render(request,'mainapp/index.html',{'postlist':postlist})

def posts(requets):
    if request.method == 'POST':
        if request.POST['mainphoto']: 
            new_article=Post.objects.create(
                title=request.POST['title'],
                author=request.POST['author'],
                price=request.POST['price'],
                origin_price=request.POST['origin_price'],
                seller=request.POST['seller'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('mainapp:home')
    return render(request, 'mainapp/register_things.html')

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})