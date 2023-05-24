from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Pot, Senzors
from .forms import NewPotForm, EditPotForm

# Create your views here.

def pots(request):
    pots = Pot.objects.filter(user=request.user)

    return render(request, 'pots/pots.html',{
        'pots': pots,
    })



@login_required
def new(request):
    if request.method == 'POST':
        form = NewPotForm(request.POST, request.FILES)

        if form.is_valid():
            pot = form.save(commit=False)
            senzor1 = Senzors()
            senzor1.type = "Senzor temperature"
            pot.senzorTmp = senzor1
            senzor1.save()

            senzor2 = Senzors()
            senzor2.type = "Senzor Ph"
            pot.senzorPh = senzor2
            senzor2.save()

            senzor3 = Senzors()
            senzor3.type = "Senzor osvjetljenja"
            pot.senzorBrightness = senzor3
            senzor3.save()

            senzor4 = Senzors()
            senzor4.type = "Senzor vlaznosti"
            pot.senzorHumidity = senzor4
            senzor4.save()

            pot.user = request.user
            pot.save()

            return redirect('pot:detail', pk=pot.id)
    else:
        form = NewPotForm()

    return render(request, 'pots/form.html', {
        'form': form,
        'title': 'Nova posuda',
        'komanda': 'Spremi',
    })

def detail(request, pk):
    pot = get_object_or_404(Pot, pk=pk)

    return render(request, 'pots/detail.html', {
        'pot': pot,
    })

@login_required
def delete(request, pk):
    pot = get_object_or_404(Pot, pk=pk)
    pot.delete()

    return redirect('pot:pots')


@login_required
def edit(request, pk):
    pot = get_object_or_404(Pot, pk=pk)

    if request.method == 'POST':
        form = EditPotForm(request.POST, request.FILES, instance=pot)

        if form.is_valid():
            form.save()

            return redirect('pot:detail', pk=pot.id)
    else:
        form = EditPotForm(instance=pot)

    return render(request, 'pots/form.html', {
        'form': form,
        'title': 'Ažuriranje podataka',
        'komanda': 'Ažuriraj',
    })