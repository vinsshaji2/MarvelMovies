from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomeView,AddMovieDetailsView,MovieListView,EditMovieDetailsView,DeleteMovieDetails,CustomerDetailsView,CustomerListView,CustomerStatus,TheatreDetailsView,TheatreListView,TheatreStatus,feedback_view

urlpatterns = [
    path('',HomeView,name='admin_home'),
    path('customer_list/',CustomerListView,name='customer_list'),
    path('customer_status/',CustomerStatus,name='customer_status'),
    path('customer_details/',CustomerDetailsView,name='customer_details'),
    path('theatre_list/',TheatreListView,name='theatre_list'),
    path('theatre_status/',TheatreStatus,name='theatre_status'),
    path('theatre_details/',TheatreDetailsView,name='theatre_details'),
    path('add_movie/',AddMovieDetailsView,name='add_movie'),
    path('edit_movie/',EditMovieDetailsView,name='edit_movie'),
    path('delete_movie/',DeleteMovieDetails,name='delete_movie'),
    path('movie_list/',MovieListView,name='movie_list'),
    path("feedback_view/", feedback_view, name="feedback_view")
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)