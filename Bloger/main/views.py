from django.shortcuts import render, redirect
from .models import Post


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
        

        if new_title and new_content:

            Post.objects.create(
                title=new_title,
                content=new_content
            )
            # أعد توجيه المستخدم للصفحة الرئيسي
            return redirect('home_page')
        else:

            context = {
                'error': 'Title and content fields are required.'
            }
            return render(request, 'main/add_post.html', context)

    else:

        return render(request, 'main/add_post.html')