from django.urls import path,include
from .views import HomeView,ticket_info


urlpatterns = [
    path('sitevistor/', include('sitevisitor.urls',namespace='sitevisitor')),
    path('',HomeView,name='customer_home'),
    path("ticket_info/", ticket_info, name="ticket_info")
    ]