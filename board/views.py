from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views import generic
from django.views.generic.edit import ModelFormMixin
# Create your views here.

class PostandBoard(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'board/board.html'

class IndexView(generic.ListView):
    model = Post