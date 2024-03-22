from django.shortcuts import render, redirect

from .forms import HotelForm
from .models import Hotel

def home_page(request):
    return render(request, 'hotel/home_page.html')

def hotel_list(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }

    return render(request, 'hotel/hotel_list.html', context=context)

def hotel_detail(request, pk):
    hotel = Hotel.objects.get(id=pk)
    context = {'hotel': hotel}
    return render(request, 'hotel/hotel_detail.html', context=context)

def hotel_create(request):
    form = HotelForm()
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
        return redirect('hotel_list')
    context = {
        'form': form
    }
    return render(request, 'hotel/hotel_create.html', context=context)

def hotel_edit(request, pk):
    hotel = Hotel.objects.get(id=pk)
    form = HotelForm(instance=hotel)
    if request.method == 'POST':
        form = HotelForm(
            request.POST,
            request.FILES,
            instance=hotel
        )
        if form.is_valid():
            form.save(commit=True)
        return redirect('hotel_list')
    context = {
        'form': form
    }

    return render(request, 'hotel/hotel_edit.html', context=context)

def hotel_delete(request, pk):
    hotel = Hotel.objects.get(id=pk)
    hotel.delete()
    return redirect('hotel_list')