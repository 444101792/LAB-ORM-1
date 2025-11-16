from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404


# Create your views here.

def home_page(request):
    posts = Post.objects.filter(is_published=True)
    context = {
        'posts_list': posts
    }
    return render(request, 'main/home.html', context)


def add_post(request):
    if request.method == 'POST':

        new_title = request.POST.get('title')
        new_content = request.POST.get('content')
        new_image = request.FILES.get('image') 

        if new_title and new_content:


            Post.objects.create(
                title=new_title,
                content=new_content,
                image=new_image  
            )


            return redirect('home_page')
        else:
            context = {
                'error': 'Title and content fields are required.'
            }
            return render(request, 'main/add_post.html', context)

    else:
        return render(request, 'main/add_post.html')
    

def post_detail(request, pk):


    post = get_object_or_404(Post, pk=pk) 
    
    context = {
        'post': post
    }
    return render(request, 'main/post_detail.html', context)


def update_post(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':

        post.title = request.POST.get('title', post.title)
        post.content = request.POST.get('content', post.content)
        

        new_image = request.FILES.get('image')
        if new_image:
            post.image = new_image
        

        post.save()
        

        return redirect('post_detail', pk=post.pk)

    else:

        context = {
            'post': post
        }
        return render(request, 'main/update_post.html', context)
    
def delete_post(request, pk):

    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':

        post.delete()

        return redirect('home_page')
    else:

        context = {
            'post': post
        }
        return render(request, 'main/delete_post.html', context)