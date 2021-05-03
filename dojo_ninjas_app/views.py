from django.shortcuts import render, redirect
from .models import Dojo, Ninja


# Create your views here.
def index(request):
    context = {
        'all_dojos': Dojo.objects.all(),
        'all_ninja': Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def new_dojo(request):
    new_dojo = Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )
    return redirect('/')

def new_ninja(request):
    new_ninja = Ninja.objects.create(
        first_name = request.POST['firstname'],
        last_name = request.POST['lastname'],
        dojo = Dojo.objects.get(id= request.POST['curr_dojo'])
    )
    return redirect('/')

def delete(request, dojo_id):
    c = Dojo.objects.get(id = dojo_id)
    c.delete()

    return redirect('/')

