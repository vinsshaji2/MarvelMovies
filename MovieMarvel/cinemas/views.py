from django.shortcuts import render, redirect, get_object_or_404
from .forms import ScreenDetailsForm, SlotDetailsForm, ShowDetailsForm, TicketDetailsForm
from adminpanel.models import Theatre, User, ScreenDetails, SlotDetails, ShowDetails, TicketDetails
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def HomeView(request):
    logged_user = request.user
    theatre = Theatre.objects.filter(user=logged_user)
    if theatre:
        context = {
            'logged_user': logged_user,
            'theatre': theatre,

        }
        print("Available")
    else:
        context = {
            'error': True
        }
        return redirect("sitevisitor:login")
    return render(request, 'cinemas/theatre_profile.html', context)


def AddScreenDetailsView(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)
    if request.method == 'POST':
        form = ScreenDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            screen = form.save(commit=False)
            screen.theatre = theatre
            screen.save()  # Save the movie detail            
            messages.success(request, 'You have successfully added new screen.')
            return redirect('screen_details')  # Redirect to home page
    else:
        form = ScreenDetailsForm()

    context = {
        'logged_user': logged_user,
        'theatre': theatre,
        'form': form
    }

    return render(request, 'cinemas/add_screen_details.html', context)


def ScreenDetailsView(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)
    screens = ScreenDetails.objects.all()
    context = {
        'logged_user': logged_user,
        'theatre': theatre,
        'screens': screens,
    }
    return render(request, 'cinemas/screen_details.html', context)


def EditScreenDetailsView(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)

    if request.method == 'POST':
        screen_id = request.POST['screen_id']

        screen = get_object_or_404(ScreenDetails, screen_id=screen_id)
        form = ScreenDetailsForm(request.POST, request.FILES, instance=screen)
        if form.is_valid():
            screens = form.save()
            screens.save()  # Save the Screen detail            
            messages.success(request, 'You have successfully edited Screen.')
            return redirect('screen_details')

        else:
            form = ScreenDetailsForm(instance=screen)
    context = {
        'logged_user': logged_user,
        'form': form,
        'screen': screen,
        'theatre': theatre,
    }
    return render(request, 'cinemas/edit_screen_details.html', context)


def DeleteScreenDetails(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)

    if request.method == 'POST':
        screen_id = request.POST['screen_id']
        screen = get_object_or_404(ScreenDetails, screen_id=screen_id)
        screen.delete()
        messages.success(request, 'You have successfully deleted Screen.')

    return redirect('screen_details')


def SlotDetailsView(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)
    slot = SlotDetails.objects.all()
    context = {
        'logged_user': logged_user,
        'theatre': theatre,
        'slot': slot,
    }
    return render(request, 'cinemas/slot_details.html', context)


def AddSlotDetailsView(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)
    if request.method == 'POST':
        form = SlotDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.theatre = theatre
            slot.save()  # Save the movie detail
            messages.success(request, 'You have successfully added new screen.')
            return redirect('slot_details')  # Redirect to home page
    else:
        form = SlotDetailsForm()

    context = {
        'logged_user': logged_user,
        'theatre': theatre,
        'form': form
    }

    return render(request, 'cinemas/add_slot_details.html', context)


def EditSlotDetailsView(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)

    if request.method == 'POST':
        slot_id = request.POST['slot_id']

        slot = get_object_or_404(SlotDetails, slot_id=slot_id)
        form = SlotDetailsForm(request.POST, request.FILES, instance=slot)
        if form.is_valid():
            slots = form.save()
            slots.save()  # Save the Screen detail
            messages.success(request, 'You have successfully edited Screen.')
            return redirect('slot_details')

        else:
            form = SlotDetailsForm(instance=slot)
    context = {
        'logged_user': logged_user,
        'form': form,
        'slot': slot,
        'theatre': theatre,
    }
    return render(request, 'cinemas/edit_slot_details.html', context)


def DeleteSlotDetailsView(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)

    if request.method == 'POST':
        slot_id = request.POST['slot_id']
        slot = get_object_or_404(SlotDetails, slot_id=slot_id)
        slot.delete()
        messages.success(request, 'You have successfully deleted Screen.')

    return redirect('slot_details')


def TicketDetailsView(request):
    if request.method == 'POST':
        form = TicketDetailsForm(request.POST)
        if form.is_valid():
            # Process the form data if needed
            form.save()  # Save the ticket details
            # Redirect or show a success message
    else:
        form = TicketDetailsForm()

    return render(request, 'cinemas/ticket_details.html', {'form': form})


def ShowDetailsView(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)
    shows = ShowDetails.objects.all()
    context = {
        'logged_user': logged_user,
        'theatre': theatre,
        'shows': shows,
    }
    for j in shows:
        for actor in j.movie.all():
            print(actor.movie_name)
    return render(request, 'cinemas/show_details.html', context)


def EditShowDetailsView(request):
    logged_user = request.user
    theatre = get_object_or_404(Theatre, user=logged_user)

    if request.method == 'POST':
        show_id = request.POST['show_id']

        show = get_object_or_404(ShowDetails, show_id=show_id)
        form = ShowDetailsForm(request.POST, request.FILES, instance=show)
        if form.is_valid():
            shows = form.save()
            shows.save()  # Save the Screen detail
            messages.success(request, 'You have successfully edited Shows.')
            return redirect('show_details')

        else:
            form = ShowDetailsForm(instance=show)
    context = {
        'logged_user': logged_user,
        'form': form,
        'show': show,
        'theatre': theatre,
    }
    return render(request, 'cinemas/edit_show_details.html', context)


def AddShowDetailsView(request):
    # logged_user = request.user
    # theatre = get_object_or_404(Theatre, user=logged_user)
    if request.method == 'POST':
        form = ShowDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            # show = form.save(commit=False)
            # show.theatre = theatre
            show.save()  # Save the movie detail
            messages.success(request, 'You have successfully added new show.')
            return redirect('show_details')  # Redirect to home page
    else:
        form = ShowDetailsForm()

    # context = {
    #   'logged_user': logged_user,
    #   'theatre': theatre,
    #   'form': form
    # }

    return render(request, 'cinemas/add_show_details.html', {'form': form})

