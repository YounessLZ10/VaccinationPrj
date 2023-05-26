from django.http import HttpResponse

def pageUneVue(request):
    return HttpResponse('<h1>Notre première page</h1>')
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from .models import Vaccine
from django.db import models

def accueil(request):
    return render(request, 'accueil.html')

def vaccination(request):
    return render(request, 'vaccination.html')
def myappoints(request):
    appointments = Appointment.objects.all()

    context = {
        'Appointments': appointments,
    }

    return render(request, 'myappoints.html', context)


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm

def appoint(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()  # Save the appointment to the database
            messages.success(request, 'Appointment booked successfully.')
            return redirect('myappoints')
    else:
        form = AppointmentForm()
        print(form.errors)
    return render(request, 'appoint.html', {'form': form})

from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Vaccine

class VaccineListView(ListView):
    model = Vaccine
    template_name = 'vaccination.html'
    context_object_name = 'vaccinations'
    paginate_by = 10

def apropos(request):
    return render(request, 'apropos.html')

from django.shortcuts import render
from .models import Appointment

def my_appointments(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'myappoints.html', context)


from django.shortcuts import render, get_object_or_404

def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    # Pass the appointment object to the template and render the HTML
    return render(request, 'myappoints')



def contact(request):
    return render(request, 'contact.html')






from django.shortcuts import redirect, render
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomAuthenticationForm

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # User credentials are correct, log in the user
                auth_login(request, user)
                return redirect('accueil')
            else:
                # User credentials are incorrect, display an error message
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm(request)
        
    return render(request, 'login.html', {'form': form})




def logout(request):
    logout(request)
    return render(request, '/logout.html/')


