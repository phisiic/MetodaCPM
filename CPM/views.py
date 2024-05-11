import csv
import os
import shutil
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CPMForm, ActivityForm, CsvForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Czynnosc, Zdarzenie
import Node
import CPMclass
import subprocess

# Create your views here.
activity_count = 0
event_count = 0

def index(request):
    czynnosci = Czynnosc.objects.all().order_by('name')
    context = {'form' : ActivityForm(), 'activities': czynnosci}
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


def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST or None)
        if form.is_valid():
            activity = form.save()
            context = {'activity': activity}
            czynnosc = f"{activity.name} - {activity.duration} - {activity.before} - {activity.after}"
            print(czynnosc)

    return render(request, 'partials/form.html', {"form": ActivityForm()})


def generate_diagram(request):
    zdarzenia = []
    czynnosci = []
    activity_count = Czynnosc.objects.count()
    event_count = max(activity.after for activity in Czynnosc.objects.all())
    activities = []
    Node.clear_folder("nodes")

    diagram_path = r"C:\Users\marci\PycharmProjects\djangoProject\CPM\static\CPM_diagram.png"

    os.remove(diagram_path)

    zdarzenia.append(Node.Zdarzenie(id="0"))
    zdarzenia.append(Node.Zdarzenie(id="1", ti=0))
    for i in range(2, event_count + 1):
        zdarzenia.append(Node.Zdarzenie(id=str(i)))

    sorted_czynnosci = Czynnosc.objects.all().order_by('name')

    for activity in sorted_czynnosci:
        czynnosc = Node.Czynnosc(activity.name, activity.duration, zdarzenia[int(activity.before)], zdarzenia[int(activity.after)])
        czynnosci.append(czynnosc)

    print(f"Czynnosci: {len(czynnosci)}, Sorted czynnosci: {sorted_czynnosci.count()}")

    CPMclass.CPM(event_count, zdarzenia, activities, czynnosci, "CPM Diagram")

    source = r"C:\Users\marci\PycharmProjects\djangoProject\CPM_diagram.png"
    destination = r"C:\Users\marci\PycharmProjects\djangoProject\CPM\static\CPM_diagram.png"

    shutil.move(source, destination)

    return render(request, 'partials/diagram-info.html', {'activity_count': activity_count, 'event_count': event_count})


def delete_activity(request, activity_id):
    activity = Czynnosc.objects.get(pk=activity_id)
    activity.delete()
    return redirect('/')


def generate_from_csv(request):
    if request.method == 'POST':
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']

            # Decode the uploaded file as UTF-8
            decoded_file = uploaded_file.read().decode('utf-8').splitlines()

            # Parse the CSV data
            csv_data = csv.reader(decoded_file)
            num_activities = int(next(csv_data)[0])
            num_events = int(next(csv_data)[0])

            # Create Activity objects
            activities = []
            for _ in range(num_activities):
                name, duration, event_before, event_after = next(csv_data)
                activity = Czynnosc(name=name, duration=int(duration), before=int(event_before), after=int(event_after))
                activities.append(activity)

            # Bulk create Activity objects
            Czynnosc.objects.bulk_create(activities)

            return redirect('/')
    else:
        form = CsvForm()

    return render(request, 'upload_csv.html', {'form': form})
