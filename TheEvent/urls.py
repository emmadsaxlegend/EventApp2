from django.urls import path
from . import views

#from . import views
from .views import HomeView, ArticleDetailView, AddEventView, AddFreeEventView, UpdateEventView, DeleteEventView
urlpatterns = [
    #path('', views.home, name='home')
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add-event/', AddEventView.as_view(), name="add_event"),
    path('add-free-event/', AddFreeEventView.as_view(), name="add_free_event"),
    path('event/edit/<int:pk>/', UpdateEventView.as_view(), name= "update_event" ),
    path('event/<int:pk>/delete', DeleteEventView.as_view(), name= "delete_event" )

]
