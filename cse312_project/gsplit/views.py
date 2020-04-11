from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from . import forms
from braces.views import SelectRelatedMixin
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib import messages


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


def profile(request):
    return render(request, 'gsplit/profile.html')


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


class UserPosts(ListView):
    model = models.Post
    template_name = 'gsplit/profile.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:

            raise Http404
        else:
            return self.post_user.posts.all()

    def context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user


class UserPostsDetal(DetailView):
    model = models.Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get("username"))


class CreatePost(LoginRequiredMixin, CreateView):
    fields = ('message')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy("all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)

# def login(request):
#     return render(request, 'gsplit/login.html')
