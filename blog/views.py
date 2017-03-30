from django.shortcuts import redirect
import datetime
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import PostForm



# Create your views here.
from .forms import UploadImageForm

def upload_image_view(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=profile)
        form = UploadImageForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
    else:
        form = UploadImageForm()

    return render(request, 'upload.html', {'form': form})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.timestamp = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})






def home_view(request):
    return render_to_response('base.html')
