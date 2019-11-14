from django.shortcuts import render
from django.views.generic import DetailView

from .models import BlogPost
# Create your views here.
import string
import random
from django.utils import timezone
from django.core.paginator import Paginator


def post_list(request):
    postlist = BlogPost.objects.all()
    paginator = Paginator(postlist, 5)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'my_blog_app/post_list.html', {'posts': post})


class PostDetailView(DetailView):
    model = BlogPost


def random_number(request):
    n = 6
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    return render(request,'my_blog_app/random_string.html', {'res': str(res)})

