from django.shortcuts import render, redirect
from .forms import CPMForm, ActivityForm
from django.http import HttpResponseRedirect
from .models import Czynnosc, Zdarzenie
from Node import Czynnosc, Zdarzenie

# Create your views here.
zdarzenia = []
czynnosci = []
activity_count = 0
event_count = 0

def index(request):
    context = {'form' : ActivityForm()}
    return render(request, 'enter_activities.html', context)

def get_diagram_info(request):
    global activity_count
    global event_count
    if request.method == "POST":
        form = CPMForm(request.POST)
        if form.is_valid():
            activity_count = form.cleaned_data['no_activities']
            event_count = form.cleaned_data['no_events']
            diagram_name = form.cleaned_data['file_name']
            return HttpResponseRedirect(f"/data/")

    else:
        form = CPMForm()

    return render(request, 'get_size.html', {"form" : form})

def activity_form(request):
    global activity_count, event_count

    if request.method == "POST":
        forms = [ActivityForm(request.POST, prefix=str(i)) for i in range(activity_count)]
        if all(form.is_valid() for form in forms):
            for form in forms:
                form.save()
            return redirect('index')
    else:
        forms = [ActivityForm(prefix=str(i)) for i in range(activity_count)]
    return render(request, 'enter_activities.html', {"activity_form": forms})
