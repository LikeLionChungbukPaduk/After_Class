from tkinter import Image
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,PostImage
from .forms import PostForm
# Create your views here.
def home(request):
    postlist=Post.objects.all().prefetch_related('postimage_set')
    return render(request,'mainapp/index.html',{'postlist':postlist})


def posts(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.seller=request.user
            obj.save()
            image_list=request.FILES.getlist('images')
            for item in image_list:
                images=PostImage.objects.create(post=obj,images=item)
            return redirect('mainapp:home')
        else:
            print("errors : {}".format(form.errors))
            return redirect('accounts:signup')
    else:
        postform=PostForm()
        return render(request,'mainapp/register_things.html',{'postform':postform})

# def posts(request):
#     if request.method=='POST':
#         form=PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             obj=form.save(commit=False)
#             obj.seller=request.user
#             obj.save()
#             form=PostForm()
#             return redirect('mainapp:home')
#         else:
#             print("errors : {}".format(form.errors))
#             return redirect('accounts:signup')
#     else:
#         form=PostForm()
#         return render(request,'mainapp/register_things.html',{'form':form})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post_detail = get_object_or_404(Post,pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'mainapp/posting.html', {'post':post_detail})

def PostDelete(requset,pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('mainapp:home')