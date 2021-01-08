from django.shortcuts import render, HttpResponseRedirect, reverse


from django.views import View

from photo_app.models import Image
from user_app.models import MyUser

from user_app.forms import SignUpForm
from comment_app.forms import CommentForm
from comment_app.models import Comment

class HomePage(View):
    
    html = 'homepage.html'
    form = CommentForm()

    def get(self, request):
        comments = Comment.objects.all()
        img_set = Image.objects.all()
        new = Image.objects.all().order_by('post_time')
        top = Image.objects.all().order_by('likes')
        stories = Image.objects.filter(is_story=True).all()
        return render(request, self.html, {'img_set': img_set, 'new': new, 'top': top, 'comments': comments, 'form': self.form, 'stories':stories   })

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class NewView(View):
    
    html = 'homepage.html'
    form = CommentForm()

    def get(self, request):
        comments = Comment.objects.all()
        img_set = Image.objects.order_by('post_time')[::-1]
        stories = Image.objects.filter(is_story=True).all()
        return render(request, self.html, {'img_set': img_set, 'comments': comments, 'form': self.form, 'stories':stories   })

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class TopView(View):
    
    html = 'homepage.html'
    form = CommentForm()
    likes = []

    def get(self, request):
        comments = Comment.objects.all()
        img_set = Image.objects.order_by('-likes') 
        stories = Image.objects.filter(is_story=True).all()
        return render(request, self.html, {'img_set': img_set, 'comments': comments, 'form': self.form, 'stories':stories   })

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




""" Follow this example to add photos/comments to any view """
class Profile(View):

    html = 'profile.html'
    form = CommentForm()

    def get(self, request, user_id):
        user = MyUser.objects.get(id=user_id)
        """ Need this if you want yo filter photos by which user owns them """
        img_set = Image.objects.filter(myuser=user)
        """ Need this or a way to capture your photos .all() or .get()"""
        comments = Comment.objects.all()
        """ Need this """
        # imgs = [img for img in images]
        return render(request, self.html, {'user':user,  'img_set':img_set, 'comments': comments, 'form': self.form })

    """ Copy the post() function fully """
    def post(self, request, user_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



class SignUp(View):

    form_class = SignUpForm

    def get(self, request):
        html = 'generic_form.html'
        form = self.form_class
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create_user(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password']
            )
            return HttpResponseRedirect(reverse('Homepage'))

