import json
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .forms import SingupForm, MyprofileForm, ChangingPasswordForm
from .scripts.sync import sync as sy
from pot.models import Pot, SenzorValues, Senzors
from plant.models import Plant
# Create your views here.

def index(request):
    plants = Plant.objects.all()

    return render(request, 'core/index.html',{
        'plants': plants,
    })

@login_required
def sync(request):
    pots = Pot.objects.filter(user=request.user, plant__isnull=False)
    for pot in pots:
        data = sy(pot.indoor)
        save_data(pot,data)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def save_data(pot: Pot, data):
    dict_json = json.loads(data)
    senzor_value = SenzorValues()
    senzor_value.senzor = pot.senzorTmp
    senzor_value.value = dict_json["tmp"]
    senzor_value.date = datetime.now()
    senzor_value.save()
    senzor = get_object_or_404(Senzors, pk=pot.senzorTmp.id)
    senzor.date = datetime.now()
    senzor.currentValue = dict_json["tmp"]
    senzor.save()
    senzor_value1 = SenzorValues()
    senzor_value1.senzor = pot.senzorBrightness
    senzor_value1.value = dict_json["brightness"]
    senzor_value1.date = datetime.now()
    senzor_value1.save()
    senzor1 = get_object_or_404(Senzors, pk=pot.senzorBrightness.id)
    senzor1.date = datetime.now()
    senzor1.currentValue = dict_json["brightness"]
    senzor1.save()
    senzor_value2 = SenzorValues()
    senzor_value2.senzor = pot.senzorHumidity
    senzor_value2.value = dict_json["humidity"]
    senzor_value2.date = datetime.now()
    senzor_value2.save()
    senzor2 = get_object_or_404(Senzors, pk=pot.senzorHumidity.id)
    senzor2.date = datetime.now()
    senzor2.currentValue = dict_json["humidity"]
    senzor2.save()
    senzor_value3 = SenzorValues()
    senzor_value3.senzor = pot.senzorPh
    senzor_value3.value = dict_json["ph"]
    senzor_value3.date = datetime.now()
    senzor_value3.save()
    senzor3 = get_object_or_404(Senzors, pk=pot.senzorPh.id)
    senzor3.date = datetime.now()
    senzor3.currentValue = dict_json["ph"]
    senzor3.save()

    if dict_json["humidity"] < 100:
        pot.status = "Dodati vode"
    else:
        pot.status = "OK"
    pot.save()


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

class PasswordsChangeView(PasswordChangeView):
    from_class = ChangingPasswordForm

