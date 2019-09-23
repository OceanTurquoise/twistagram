from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth import login


from .forms import SignUpForm
from .models import User


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        form = self.get_form()
        user = User.objects.get(username=form.data.get('username'))

        login(self.request, user)
        return reverse(
            'accounts:userDetail',
            kwargs={'username': user.username })

class AccountsDetailView(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['login_user'] = self.request.user
        return context

class IconEdit(UpdateView):
    model = User
    template_name = 'accounts/icon_edit.html'
    fields = ['icon']

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        form = self.get_form()
        return reverse(
            'accounts:userDetail',
            kwargs={'username': self.request.user.username}
        )
