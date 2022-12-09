from django.urls import path
from . import views

#from . import views
from .views import HomeView, ArticleDetailView, AddEventView, AddFreeEventView
urlpatterns = [
    #path('', views.home, name='home')
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add-event/', AddEventView.as_view(), name="add_event"),
    path('add-free-event/', AddFreeEventView.as_view(), name="add_free_event"),
]
