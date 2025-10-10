from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
# Create your views here.


class CarsView(View):

    def get(self, request):
        cars = Car.objects.all().order_by('brand__name')
        search = request.GET.get('search')
 
        if search:
            cars = cars.filter(model__icontains=search) #icontains ignora uppercase ou lower, sem o i ele leva em consideração

        return render(
            request, 
            'cars.html', 
            {'cars': cars }
        )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else: 
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})

