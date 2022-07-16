from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import *


# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = 'vlog_app/index.html'
    
    