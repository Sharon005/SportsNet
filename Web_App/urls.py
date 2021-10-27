from django.urls import path 
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),    
    path('signout', views.signout, name='signout'),

    path('home', views.home, name="home"),
    path('sports', views.sports, name="sports"),
    path('organise', views.organise, name="organise"),
    path('event', views.event, name="event"),
    path('store', views.store, name="store"),
    path('storef', views.storef, name="storef"),
    path('eventform', views.eventform, name="eventform"),
    path('organizer', views.organizer, name="organizer"),
    
]
