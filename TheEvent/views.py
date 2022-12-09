from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Event
from .forms import EventForm
from django.contrib import messages

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Event
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Event
    template_name = 'article_details.html'

class AddEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'add_event.html'
    # fields = '__all__'
    # fields = ('author', 'title', 'location', 'price', 'space_capacity', 'description', 'event_date', 'event_end_date')

class AddFreeEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'add_free_event.html'
    # fields = '__all__'
    #fields = ('author', 'title', 'location', 'description', 'event_date')

