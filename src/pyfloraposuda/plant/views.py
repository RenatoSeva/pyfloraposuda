from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from requests import Response

from .models import Plant
from .forms import EditPlantForm, NewPlantForm

# Create your views here.

def plants(request: HttpRequest) -> HttpResponse:
    """funkcija za prikazivanje biljaka koje je kreirao user

    Args:
        request (HttpRequest): http zahtjev s parametrima za ispis biljaka

    Returns:
        render: vraca plants.html
    """
    plants = Plant.objects.all()

    return render(request, 'plants/plants.html',{
        'plants': plants,
    })

def detail(request: HttpRequest, pk: int) -> HttpResponse:
    """funkcija za ispisivanje detalja biljke

    Args:
        request (HttoRequest): http zahtjev s parametrima za ispisivanje detalja biljke
        pk (primaryKey): Primarni ključ tablice Plant

    Returns:
        render: vraća detail.html
    """
    plant = get_object_or_404(Plant, pk=pk)

    return render(request, 'plants/detail.html', {
        'plant': plant,
    })

@login_required
def delete(request: HttpRequest, pk: int)-> HttpResponse:
    """funkcija za brisanje biljke iz tablice Plants

    Args:
        pk (primaryKey): Primarni ključ tablice Plants

    Returns:
        redirect: plants.html
    """
    plant = get_object_or_404(Plant, pk=pk)
    plant.delete()

    return redirect('plant:plants')


@login_required
def edit(request: HttpRequest, pk: int) -> HttpResponse:
    """Funkcija za uređivanje biljaka

    Args:
        request (HttpRequest): http zahtjev s parametrima za uređivanje biljke
        pk (primaryKey): primarni ključ na tablicu Plants

    Returns:
        render: vraća form.html
    """
    plant = get_object_or_404(Plant, pk=pk)

    if request.method == 'POST':
        form = EditPlantForm(request.POST, request.FILES, instance=plant)

        if form.is_valid():
            form.save()

            return redirect('plant:detail', pk=plant.id)
    else:
        form = EditPlantForm(instance=plant)

    return render(request, 'plants/form.html', {
        'form': form,
        'title': 'Ažuriranje podataka',
        'komanda': 'Ažuriraj',
    })

@login_required
def new(request: HttpRequest) -> HttpResponse:
    """funkcija za kreiranje nove posude

    Args:
        request (HttpRequest): http zahtjev s parametrima za kreiranje nove biljke

    Returns:
        render: vraća form.html
    """
    if request.method == 'POST':
        form = NewPlantForm(request.POST, request.FILES)

        if form.is_valid():
            plant = form.save(commit=False)
            plant.save()

            return redirect('plant:detail', pk=plant.id)
    else:
        form = NewPlantForm()

    return render(request, 'plants/form.html', {
        'form': form,
        'title': 'Nova biljka',
        'komanda': 'Spremi',
    })