from django.urls import path
from .views import HomeView, AddScreenDetailsView,DeleteScreenDetails,EditScreenDetailsView,ScreenDetailsView,ShowDetailsView,AddShowDetailsView,TicketDetailsView,AddSlotDetailsView,SlotDetailsView,EditSlotDetailsView,DeleteSlotDetailsView

urlpatterns = [
    path('',HomeView,name='theatre_profile'),
    path('add_screen/', AddScreenDetailsView,name='add_screen_details'),
    path('edit_screen/', EditScreenDetailsView,name='edit_screen_details'),
    path('delete_screen/', DeleteScreenDetails,name='delete_screen_details'),
    path('screen_details/', ScreenDetailsView,name='screen_details'),
    path('slot_details/', SlotDetailsView,name='slot_details'),
    path('add_slot_details/', AddSlotDetailsView,name='add_slot_details'),
    path('edit_slot_details/', EditScreenDetailsView,name='edit_slot_details'),
    path('delete_slot_details/', DeleteSlotDetailsView,name='delete_slot_details'),
    path('ticket_details/', TicketDetailsView,name='ticket_details'),
    path('show_details/', ShowDetailsView,name='show_details'),
    path('add_show_details/', AddShowDetailsView,name='add_show_details'),
    ]