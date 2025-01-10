from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import redirect
from .forms import TimeTravelerForm
from .models import TimeTraveler

# Create your views here.
def timetraveler_list(request):
    time_traveler = TimeTraveler.objects.all()
    context = {'time_traveler': time_traveler}
    return render(request, 'traveler_list.html', context)

def add_timetraveler_form(request):
    if request.method == 'POST':
        form = TimeTravelerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TimeTravelerForm

    context = {'form': form}
    return render(request, 'add_timetraveler_form.html', context)


def traveler_edit(request, id):
    traveler = get_object_or_404(TimeTraveler, id=id)
    if request.method == 'GET':
        form = TimeTravelerForm(instance=traveler)

    else:
        form = TimeTravelerForm(request.POST, instance=traveler)
        if form.is_valid():
            form.save()
            return redirect('traveler')

    context = {'form': form}
    return render(request, 'edit_traveler.html', context)


def traveler_delete(request, id):
    traveler = get_object_or_404(TimeTraveler, id=id)
    traveler.delete()
    return HttpResponseRedirect('/traveler/')


def traveler_detail(request, id):
    traveler = get_object_or_404(TimeTraveler, id=id)
    context = {'traveler': traveler}
    return render(request, 'traveler_detail.html', context)
