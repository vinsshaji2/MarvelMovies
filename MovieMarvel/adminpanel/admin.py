from django.contrib import admin
from .models import Customer, Theatre, ScreenDetails, MovieDetails, ShowDetails, TicketDetails, SlotDetails, BookingDetails, Bank, MovieTheaters,user_seats,seats, feedback


# Registering models with the custom admin classes
admin.site.register(Customer)
admin.site.register(Theatre)
admin.site.register(ScreenDetails)
admin.site.register(MovieDetails)
admin.site.register(ShowDetails)
admin.site.register(TicketDetails)
admin.site.register(SlotDetails)
admin.site.register(BookingDetails)
admin.site.register(Bank)
admin.site.register(MovieTheaters)
admin.site.register(seats)
admin.site.register(user_seats)
admin.site.register(feedback)

