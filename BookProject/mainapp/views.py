from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def home(request):
    postlist=Post.objects.all()
    return render(request,'mainapp/index.html',{'postlist':postlist})

def posts(request):
    # if request.method == 'POST':
    #     post = Post()
    #     post.title = request.POST.get('title')
    #     post.content = request.POST.get('contents')
    #     post.author = request.POST.get('author')
    #     post.price = request.POST.get('price')
    #     post.origin_price = request.POST.get('origin_price')
    #     post.seller = request.user
    #     if 'image' in request.FILES:
    #         post.image = request.FILES['image']

    #     post.save()
    #     return redirect('mainapp:home')
    # else:
    #     return render(request, 'mainapp/register_things.html')
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainapp:home')
        else:
            print("errors : {}".format(form.errors))
            return redirect('accounts:signup')
    else:
        form=PostForm()
        return render(request,'mainapp/register_things.html',{'form':form})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'mainapp/posting.html', {'post':post})