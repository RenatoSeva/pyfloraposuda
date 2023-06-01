from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Pot, Senzors, SenzorValues
from .forms import NewPotForm, EditPotForm

# Create your views here.

def pots(request: HttpRequest) -> HttpResponse:
    """funkcija za prikazivanje posuda koje je kreirao user

    Args:
        request (HttpRequest): http zahtjev s parametrima za ispis posuda

    Returns:
        render: vraca pots.html
    """
    pots = Pot.objects.filter(user=request.user)

    return render(request, 'pots/pots.html',{
        'pots': pots,
    })



@login_required
def new(request:HttpRequest) -> HttpResponse:
    """funkcija za kreiranje nove posude

    Args:
        request (HttpRequest): http zahtjev s parametrima za kreiranje nove posude

    Returns:
        render: vraća form.html
    """
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
        'command': 'Spremi',
    })

def detail(request: HttpRequest, pk: int) -> HttpResponse:
    """funkcija za ispisivanje detalja posude

    Args:
        request (HttoRequest): http zahtjev s parametrima za ispisivanje detalja posude
        pk (primaryKey): Primarni ključ tablice Pot

    Returns:
        render: vraća detail.html
    """
    pot = get_object_or_404(Pot, pk=pk)
    senzorvaluestpm = SenzorValues.objects.filter(senzor_id=pot.senzorTmp.id)
    senzorvaluesph = SenzorValues.objects.filter(senzor_id=pot.senzorPh.id)
    senzorvaluesbrightness = SenzorValues.objects.filter(senzor_id=pot.senzorBrightness.id)
    senzorvalueshumidity = SenzorValues.objects.filter(senzor_id=pot.senzorHumidity.id)
    #senzorvalues = SenzorValues.objects.all()

    return render(request, 'pots/detail.html', {
        'pot': pot,
        'senzorvaluestpm' : senzorvaluestpm,
        'senzorvaluesph'  : senzorvaluesph,
        'senzorvaluesbrightness' : senzorvaluesbrightness,
        'senzorvalueshumidity' : senzorvalueshumidity,
    })

@login_required
def delete(pk: int) -> HttpResponse:
    """funkcija za brisanje posude iz tablice Pot

    Args:
        pk (primaryKey): Primarni ključ tablice Pot

    Returns:
        redirect: pots.html
    """
    pot = get_object_or_404(Pot, pk=pk)
    pot.delete()

    return redirect('pot:pots')


@login_required
def edit(request:HttpRequest, pk: int) -> HttpResponse:
    """Funkcija za uređivanje posuda

    Args:
        request (HttpRequest): http zahtjev s parametrima za uređivanje posude
        pk (primaryKey): primarni ključ na tablicu Pot

    Returns:
        render: vraća form.html
    """
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
        'command': 'Ažuriraj',
    })