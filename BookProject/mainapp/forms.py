from dataclasses import fields
from xml.parsers.expat import model
from django import forms
from .models import Post,PostImage
class PostForm(forms.ModelForm):
    images=forms.ImageField(widget=forms.ClearableFileInput(attrs={"multiple":True}))
    class Meta:
        model=Post
        fields=['title','author','price','origin_price','content','images']

# class ImageForm(forms.ModelForm):
#     
#     class Meta:
#         model=PostImage
