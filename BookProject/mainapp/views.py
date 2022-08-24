import urllib.request as request
from django.shortcuts import render,redirect
from .models import Post,Photo
# Create your views here.
def home(request):
    postlist=Post.objects.all()
    return render(request,'mainapp/index.html',{'postlist':postlist})

def posts(requets):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.author = request.POST['author']
        post.price = request.POST['price']
        post.origin_price = request.POST['origin_price']
        post.seller = request.user
        post.save()
        for img in request.FILES.getlist('imgs'):
          # Photo 객체를 하나 생성한다.
          photo = Photo()
          # 외래키로 현재 생성한 Post의 기본키를 참조한다.
          photo.post = post
          # imgs로부터 가져온 이미지 파일 하나를 저장한다.
          photo.image = img
          # 데이터베이스에 저장
          photo.save()
        return redirect('/detail/' + str(post.id))
    else:
        return render(request, 'mainapp:register_things.html')

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'mainapp:posting.html', {'post':post})