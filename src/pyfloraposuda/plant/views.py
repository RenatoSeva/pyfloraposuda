from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Plant
from .forms import EditPlantForm, NewPlantForm

# Create your views here.

def plants(request):
    plants = Plant.objects.all()

    return render(request, 'plants/plants.html',{
        'plants': plants,
    })

def detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)

    return render(request, 'plants/detail.html', {
        'plant': plant,
    })

@login_required
def delete(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    plant.delete()

    return redirect('plant:plants')


@login_required
def edit(request, pk):
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
def new(request):
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