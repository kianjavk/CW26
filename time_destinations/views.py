
from django.http import HttpResponseRedirect
from django.shortcuts import render ,get_object_or_404

from .forms import TimeDestinationform
from .models import TimeDestination

# Create your views here.
def timedestinations_list(request):
    time_destinations = TimeDestination.objects.all()
    context = {'time_destinations': time_destinations}
    return render(request, 'destinations_list.html', context)

def add_timedestination_form(request):
    if request.method == 'POST':
        form = TimeDestinationform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TimeDestinationform

    context = {'form': form}
    return render(request, 'add_timedestination_form.html', context)


def destination_edit(request, id):
    destination = get_object_or_404(TimeDestination, id=id)
    if request.method == 'GET':
        form = TimeDestinationform(instance=destination)

    else:
        form = TimeDestinationform(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/destinations/')
    context = {'form': form}
    return render(request, 'edit_destination.html', context)


def destination_delete(request, id):
    destination = get_object_or_404(TimeDestination, id=id)
    destination.delete()
    return HttpResponseRedirect('/destinations/')

def destination_detail(request, id):
    destination = get_object_or_404(TimeDestination, id=id)
    context = {'destination': destination}
    return render(request, 'destination_detail.html', context)