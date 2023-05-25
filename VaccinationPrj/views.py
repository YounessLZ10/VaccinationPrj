from django.http import HttpResponse

def pageUneVue(request):
    return HttpResponse('<h1>Notre première page</h1>')
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, VaccineForm
from .models import Vaccine
from django.db import models

def accueil(request):
    return render(request, 'accueil.html')

def vaccination(request):
    return render(request, 'vaccination.html')

def myappoints(request):
    return render(request, 'myappoints.html')
def appoint(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        # Save appointment details to the database or perform other actions

        # Render a success page or redirect to a success URL
        return HttpResponse('Appointment booked successfully!')
    
    return render(request, 'appoint.html')


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


from django.shortcuts import render, get_object_or_404

def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    # Pass the appointment object to the template and render the HTML
    return render(request, 'myappoints')



def contact(request):
    return render(request, 'contact.html')


def get_queryset(self):
        query = self.request.GET.get('search', '')
        if query:
            queryset = Vaccine.objects.filter(
                Q(vaccine_type__icontains=query) |
                Q(date_of_vaccination__icontains=query)
            )
        else:
            queryset = Vaccine.objects.all().order_by('-date_of_vaccination')
        return queryset





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


from django.contrib import messages
from django.contrib.auth import authenticate, login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # User credentials are correct, log in the user
                login(request, user)
                return redirect('accueil.html')
            else:
                # User credentials are incorrect, display an error message
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    logout(request)
    return render(request, '/logout.html/')

@login_required
def vaccine_form(request):
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            vaccine = form.save(commit=False)
            vaccine.user = request.user
            vaccine.save()
            return redirect('vaccine_history')
    else:
        form = VaccineForm()
    return render(request, 'vaccine_form.html', {'form': form})

@login_required
def vaccine_history(request):
    vaccines = Vaccine.objects.filter(user=request.user).order_by('-date_of_vaccination')
    return render(request, 'vaccine_history.html', {'vaccines': vaccines})