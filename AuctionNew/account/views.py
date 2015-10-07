from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import LoginForm, SignupForm,ForgotPasswordForm, ResetPasswordForm
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import MyUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
import base64
from django.conf import settings
import json
from django.db.models import Q
from products.forms import ProductUploadForm, BidPostForm, SearchProductForm, CategorySearchForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from products.models import Product
from django.http import JsonResponse
from products.models import *


# Create your views here.

@require_GET
def base(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        #form = SearchProductForm()
       # return render (request, "index.html", {'form' : form});
        return redirect('search')

@require_GET
def search(request):
    form = SearchProductForm()
    form1 = CategorySearchForm()
    data = { 'form' : form, 'form1' : form1 }
    return render(request, "account/authentication/index.html", data);


#@require_POST
@require_http_methods(['GET', 'POST'])
def handleLogin(request):
    if request.user.is_authenticated():
        return redirect('home')  
    if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():
         user = form.get_user();
         login(request, user);
         return redirect('home')
    else:
        form = LoginForm()
    data = { 'form' : form }
    return render(request, 'account/authentication/login.html', data);

@require_http_methods(['GET', 'POST'])
#@require_POST
def handleSignup(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == "POST":
      form = SignupForm(request.POST,initial = {'phone' : '+91'})
      #nexturl = request.POST.get('next')
      if form.is_valid():
        user = form.save();
        user.is_active = False;
        user.is_staff = True;
        user.is_superuser = True;
        user.save();
        url = request.build_absolute_uri(reverse('activate'));
        url = url + "?user=" + base64.b64encode(user.username.encode('utf-8')).decode('utf-8')
        message = ''' welcome to my Auction King!. Click %s to activate your account ''' % url
        email = EmailMessage('Welcome', message, to=[user.email])
        email.send()
        return render(request, 'account/authentication/postsignup.html')
    else:
        #signupform = f
        #loginform = LoginForm()
        #data = { 'loginform' : loginform, 'signupform' : signupform , 'next' : nexturl }
        form = SignupForm(initial = {'phone' : '+91'})
    data = { 'form': form }
    return render(request, 'account/authentication/signup.html', data);

@require_GET
def activateaccount(request):
    if request.user.is_authenticated():
        return redirect('home')
    username = base64.b64decode(request.GET.get('user').encode('utf-8')).decode('utf-8')
    user = get_object_or_404(MyUser, username = username);
    user.is_active = True
    user.save()
    return render(request, 'account/authentication/login.html', { 'form': LoginForm(), 'act' : True})

@require_GET
@login_required
def home(request):
    f = ProductUploadForm()
    form1 = BidPostForm();
    products = Product.objects.all();
    return render(request, 'product/product_upload.html',{'form' : f, 'form1': form1, 'products' : products})

@require_GET
@login_required
def otherhome(request):
    all_users = MyUser.objects.filter(~Q(id = request.user.id), is_active = True)
    return render(request, 'account/otherhome.html', {'users' : all_users});

@require_GET
def logoutview(request):
    logout(request)
    return redirect('base')

#def add(request):


@require_http_methods(['GET', 'POST'])
def forgot_password(request):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            opts = {
                    'token_generator' : default_token_generator,
                    'from_email' : settings.DEFAULT_FROM_EMAIL,
                    'email_template_name' : 'account/email/password_reset/password_reset_email_text.txt',
                    'subject_template_name' : 'account/email/password_reset/password_reset_subject.txt',
                    'request' : request,
                    'html_email_template_name' : None
            }
            form.save(**opts)
            return render(request, 'account/authentication/password_reset_email_sent.html')
    else:
        form = ForgotPasswordForm()
    context = {'form' : form}
    return render(request, 'account/authentication/password_reset_form.html', context)


@require_http_methods(['GET', 'POST'])
@sensitive_post_parameters()
@never_cache
def reset_password(request, uidb64=None, token=None):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)

    assert uidb64 is not None and token is not None

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        validlink = True
        if request.method == 'POST':
            form = ResetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'account/authentication/password_reset_complete.html')
        else:
            form = ResetPasswordForm(user)
    else:
        validlink = False
        form = None
    context = { 'validlink' : validlink, 'form' : form }
    return render(request, 'account/authentication/password_reset_confirm_form.html', context)

@require_GET
def search_product(request):
    name = request.GET.get('name')
    data = []
    if name:
        products = Product.objects.filter(Title__icontains = name)
        print(products)
        data = [{'id': item.id, 'title' : item.Title } for item in products ]
    print(data);
    return JsonResponse(data = { 'items' : data });

