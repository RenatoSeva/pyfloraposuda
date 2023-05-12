from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SingupForm, MyprofileForm, ChangePasswordForm
# Create your views here.

def index(request):

    return render(request, 'core/index.html')

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SingupForm()
    form = SingupForm()


    return render(request, 'core/signup.html',{
        'form': form
    })

@login_required
def myprofile(request):
    if request.method == 'POST':
        form = MyprofileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('/mojprofil/')
    else:
        form = MyprofileForm(instance=request.user)
    return render(request, 'core/myprofile.html',{
        'form': form
    })

# @login_required
# def changepassword(request,*args, **kwargs):
#     if request.method == 'POST':
#         form = ChangePasswordForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()

#             return redirect('/mojprofil/')
#     else:
#         form = ChangePasswordForm(instance=request.user)
#     return render(request, 'core/changepassword.html',{
#         'form': form
#     })

def changepassword(self, request):
    instance_user = get_object_or_404(User, id=int(user_id))
    form_edit_password = ChangePasswordForm(instance_user)
    context={'form_edit_password': form_edit_password}

    return render(request, self.template_name, context)
