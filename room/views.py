from django.shortcuts import render, redirect

from .forms import RoomForm
from .models import Room


def room_list(request):
    room = Room.objects.all()
    context = {
        'rooms': room
    }

    return render(request, 'room/room_list.html', context=context)

def room_detail(request, pk):
    room = Room.objects.get(id=pk)
    context = {'rooms': room}
    return render(request, 'room/room_detail.html', context=context)

def room_create(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
        return redirect('room_list')
    context = {
        'form': form
    }
    return render(request, 'room/room_create.html', context=context)

def room_edit(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(
            request.POST,
            request.FILES,
            instance=room
        )
        if form.is_valid():
            form.save(commit=True)
        return redirect('room_list')
    context = {
        'form': form
    }

    return render(request, 'room/room_edit.html', context=context)

def room_delete(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return redirect('room_list')