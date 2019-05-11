from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import NewUserCreationForm, ProfileImageViewForm, UserUpdateForm
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View

# Create your views here.


class RegisterView(CreateView):
    model = User
    template_name = "users/register.html"
    form_class = NewUserCreationForm

    success_url = '/login/'


class ProfileView(View):

    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'profile'})

    def post(self,request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance= request.user)
        p_form = ProfileImageViewForm(request.POST, request.FILES, instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():

            u_form.save()
            p_form.save()
            messages.success(request, 'your profile successfully updated')
            return redirect('profile')

        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileImageViewForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form,
            'title': 'profile',
        }

        return render(request, 'users/profile.html', context)




