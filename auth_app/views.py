from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import render, HttpResponseRedirect, reverse


from django.views import View
# Create your views here.


class LoginFormView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "generic_form.html", {'cont': "You can login in here", 'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('Homepage')))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("Homepage"))
