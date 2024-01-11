from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomeView, CustomerRegistrationView, LoginView, TheatreRegistrationView, Movies, movies_in_theaters, Movie_booking, payment, feedback_info, screen,user_logout

app_name = 'sitevisitor'
urlpatterns = [
    path('', HomeView, name='home'),
    path('Customer Registration/', CustomerRegistrationView, name='customer_registration'),
    path('Theatre Registration/', TheatreRegistrationView, name='theatre_registration'),
    path('Login/', LoginView, name='login'),
    path('movie_booking/<str:screen_name>/', Movie_booking, name='movie_booking'),
    path('movies/', movies_in_theaters, name="movies_in_theaters"),
    path('payment/', payment, name="payment"),
    path("feedback/", feedback_info, name="feedback"),
    path("screen_selection/<int:theater_id>/", screen, name="screen"),
    path("logout/", user_logout, name="user_logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
