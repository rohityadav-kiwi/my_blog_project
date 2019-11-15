from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import BlogPost
# Create your views here.
import string
import random

from django.core.paginator import Paginator


def post_list(request):
    postlist = BlogPost.objects.all()
    paginator = Paginator(postlist, 4)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'my_blog_app/post_list.html', {'posts': post})





def myblogs(request):
    my_posts = BlogPost.objects.filter(author=request.user).order_by('-published_date')

    return render(request, 'my_blog_app/random_string.html', {'my_posts': my_posts})


class PostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('post_list')


class PostDetailView(DetailView):
    model = BlogPost


class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'post_content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def random_number(request):
    n = 6
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    return render(request,'my_blog_app/random_string.html', {'res': str(res)})

