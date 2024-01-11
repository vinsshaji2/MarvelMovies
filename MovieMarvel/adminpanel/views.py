from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Theatre, User, MovieDetails, feedback
from .forms import MovieDetailsForm, movies_form
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def superuser_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'adminpanel/oops_page.html')

    return _wrapped_view


# Create your views here.
# @superuser_required
# @login_required
def HomeView(request):
    logged_user = request.user
    print(logged_user)
    context = {
        'logged_user': logged_user,
    }
    return render(request, 'adminpanel/admin_home.html', context)


@superuser_required
def CustomerListView(request):
    logged_user = request.user
    customers = Customer.objects.all()
    active_customers = Customer.objects.filter(status='Active')
    inactive_customers = Customer.objects.filter(status='Inactive')
    context = {
        'customers': customers,
        'active_customers': active_customers,
        'inactive_customers': inactive_customers,
        'today': datetime.now(),
        'logged_user': logged_user
    }
    return render(request, 'adminpanel/customer_list.html', context)


@superuser_required
def CustomerStatus(request):
    if request.method == 'POST':
        status = request.POST.get("status")
        customer_id = int(request.POST.get('customer_id', 0))

        customer = get_object_or_404(Customer, customer_id=customer_id)

        if status == 'Active':
            customer.status = 'Active'
            # Add a success message
            messages.success(request, 'The customer is successfully Activated.')

        else:
            customer.status = 'Inactive'
            # Add a success message
            messages.success(request, 'The customer is successfully Deactivated.')
        customer.save()
    return redirect('customer_list')


@superuser_required
def CustomerDetailsView(request):
    logged_user = request.user
    if request.method == 'POST':
        customer_id = int(request.POST.get('customer_id', 0))

        customer = get_object_or_404(Customer, customer_id=customer_id)
        context = {
            'customer': customer,
            'today': datetime.now(),
            'logged_user': logged_user,
        }
    return render(request, 'adminpanel/customer_details.html', context)


@superuser_required
def TheatreListView(request):
    logged_user = request.user
    theatres = Theatre.objects.all()
    active_theatres = Theatre.objects.filter(status='Active')
    inactive_theatres = Theatre.objects.filter(status='Inactive')
    context = {
        'theatres': theatres,
        'active_theatres': active_theatres,
        'inactive_theatres': inactive_theatres,
        'today': datetime.now(),
        'logged_user': logged_user,
    }
    return render(request, 'adminpanel/theatre_list.html', context)


@superuser_required
def TheatreStatus(request):
    if request.method == 'POST':
        status = request.POST.get("status")
        theatre_id = int(request.POST.get('theatre_id', 0))
        theatre = get_object_or_404(Theatre, theatre_id=theatre_id)
        if status == 'Active':
            theatre.status = 'Active'
            theatre.save()
            # Add a success message
            messages.success(request, 'The theatre is successfully Activated.')

        else:
            theatre.status = 'Inactive'
            theatre.save()
            # Add a success message
            messages.success(request, 'The theatre is successfully Deactivated.')

        return redirect('theatre_list')


@superuser_required
def TheatreDetailsView(request):
    logged_user = request.user
    if request.method == 'POST':
        theatre_id = int(request.POST.get('theatre_id', 0))
        theatre = get_object_or_404(Theatre, theatre_id=theatre_id)
        context = {
            'theatre': theatre,
            'today': datetime.now(),
            'logged_user': logged_user,
        }
    return render(request, 'adminpanel/theatre_details.html', context)


@superuser_required
def AddMovieDetailsView(request):
    logged_user = request.user
    registered = False
    if request.method == 'POST':
        form = MovieDetailsForm(request.POST, request.FILES)
        form_1 = movies_form(request.POST)
        if form.is_valid():
            movies = form.save()
            movies.save()  # Save the movie detail
            messages.success(request, 'You have successfully added new movie.')
            registered = True
        if form_1.is_valid():
            form_1.save(commit=True)
            messages.success(request,
                             f'You have successfully Linked new movie to Theater.')
            return redirect('admin_home')  # Redirect to home page
    else:
        form = MovieDetailsForm()
        form_1 = movies_form()

    context = {
        'logged_user': logged_user,
        'form': form,
        'register': registered,
        'form_1': form_1

    }

    return render(request, 'adminpanel/add_movie.html', context)


@superuser_required
def MovieListView(request):
    logged_user = request.user
    movies = MovieDetails.objects.all()
    context = {
        'logged_user': logged_user,
        'movies': movies,
    }
    return render(request, 'adminpanel/movielist.html', context)


@superuser_required
def EditMovieDetailsView(request):
    logged_user = request.user

    if request.method == 'POST':
        movie_id = request.POST['movie_id']
        movie = get_object_or_404(MovieDetails, movie_id=movie_id)
        form = MovieDetailsForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movies = form.save()
            movies.save()  # Save the movie detail            
            messages.success(request, 'You have successfully edited movie.')
            return redirect('movie_list')

        else:
            form = MovieDetailsForm(instance=movie)
    context = {
        'logged_user': logged_user,
        'form': form,
        'movie': movie,
    }
    return render(request, 'adminpanel/edit_movie.html', context)


@superuser_required
def DeleteMovieDetails(request):
    logged_user = request.user

    if request.method == 'POST':
        movie_id = request.POST['movie_id']
        movie = get_object_or_404(MovieDetails, movie_id=movie_id)
        movie.delete()
        messages.success(request, 'You have successfully deleted movie.')

    return redirect('movie_list')


def feedback_view(request):
    feedback_ins = feedback.objects.all()
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        print(feedback_id)
        if feedback_id:
            feedback_to_delete = get_object_or_404(feedback, feed_id=feedback_id)
            feedback_to_delete.delete()
            return redirect('feedback_view')

    for feed in feedback_ins:
        feed.rating = range(feed.rating)
    context = {"feedback": feedback_ins}
    return render(request, 'adminpanel/feedback_view.html', context)
