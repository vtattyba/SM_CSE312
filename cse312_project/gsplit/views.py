from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from . import forms
# from braces.views import SelectRelatedMixin
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_model


User = get_user_model()
from django.contrib import messages

from .forms import CommentForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    ads = [('gsplit/images/IMG_7781.JPG',
            'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s.'),
           ('gsplit/images/IMG_7781.JPG',
            'Some quick example text to build on the card title and make up the bulk of the card\'s content.'),
           ('gsplit/images/IMG_7781.JPG',
            'Some quick example text to build on the card title and make up the bulk of the card\'s content.')]
    c = {'ads': ads}
    return render(request, 'gsplit/index.html', context=c)



    


def friends(request):
    ads = [('gsplit/images/IMG_7781.JPG',
            'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s.'),
           ('gsplit/images/IMG_7781.JPG',
            'Some quick example text to build on the card title and make up the bulk of the card\'s content.'),
           ('gsplit/images/IMG_7781.JPG',
            'Some quick example text to build on the card title and make up the bulk of the card\'s content.')]
    c = {'ads': ads}
    return render(request, 'gsplit/friends.html', context=c)


def chat(request):
    return render(request, 'gsplit/chat.html')


class createAcc(CreateView):
    form_class = forms.UserForm
    success_url = reverse_lazy('gsplit-login')
    template_name = 'gsplit/create_acc.html'


class TestPage(TemplateView):
    template_name = 'gsplit/test.html'


class ThanksPage(TemplateView):
    template_name = 'gsplit/thanks.html'


class PostList(ListView):
    model = models.Post
    template_name = "gsplit/posts/post_list.html"


class UserPostsDetail(DetailView):
    model = models.Post
    template_name = 'gsplit/posts/post_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner__username__iexact=self.kwargs.get("username"))

@login_required
def comment_work(request, pk):
    print(request.POST.get('data'))
    print(pk)
    _post = get_object_or_404(models.Post, pk=pk)
    comment = request.POST.get('data').split('=')[1]
    comment = ' '.join(comment.split('%20'))
    new_comment = models.Comment(post=_post, author=request.user, text=comment)
    print("new comment obj", new_comment.post)
    new_comment.save()
    return JsonResponse({'comment': comment, 'author' : new_comment.author.__str__(), 'created_at' : new_comment.created_date}, status=200)

    # post = get_object_or_404(models.Post, pk=pk)
    # form = CommentForm(request.POST)
    # if form.is_valid():
    #     comment = form.save(commit=False)
    #     comment.post = post
    #     comment.save()
    # return render(request, 'gsplit/posts/comment_form.html', {'form': form})

@login_required
def likes(request, pk):
    print(request.POST.get('data'))
    print(pk)
    _post = get_object_or_404(models.Post, pk=pk)
    like_count = _post.like()
    _post.save()
    return JsonResponse({'like_count': like_count}, status=200)


class CreatePost(LoginRequiredMixin, CreateView):
    fields = ['message', 'cover']
    template_name = 'gsplit/posts/post_form.html'
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class UserProfile(LoginRequiredMixin, DetailView):
    model = models.UserProfile
    template_name = 'gsplit/test.html'
    # queryset = models.User.objects.all()
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
       
    #     print('-------------',self.kwargs.get('username'))
    #     return queryset.filter(user__username = self.kwargs.get('username'))

    def get_object(self):
        username_ = self.kwargs.get('username')
        return get_object_or_404(models.UserProfile, user__username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        user_posts = models.Post.objects.filter(owner__username=self.kwargs.get('username'))
        context['user_posts'] = models.Post.objects.filter(owner__username=self.kwargs.get('username'))
        return context

def EditProfile(request):
    if request.method == "POST":
        user_form = forms.UserEditForm(request.POST, instance=request.user)
        profile_form = forms.UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            profile.user = user
            user.save()
            profile.save()
            return redirect(reverse_lazy('all'))
    else:
        profile_form = forms.UserProfileForm(instance=request.user.userprofile)
        user_form = forms.UserEditForm(instance=request.user)

        return render(request, 'gsplit/EditProfile.html',{'u_form': user_form, 
                                                          'p_form':profile_form})



class DeletePost(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy("all")
    template_name = 'gsplit/posts/post_confirm_delete.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)


class HomePageView(ListView):
    model = models.Post
    template_name = 'gsplit/posts/post_list.html'

# def login(request):
#     return render(request, 'gsplit/login.html')
