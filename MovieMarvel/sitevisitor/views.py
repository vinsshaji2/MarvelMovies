import datetime
from datetime import date
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm, UserAuthenticationForm, TheatreRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from adminpanel.models import Customer, Theatre, MovieDetails, MovieTheaters, SlotDetails, user_seats, seats,Bank
from adminpanel.models import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from urllib.parse import unquote

# Create your views here.
def HomeView(request):
    feedback_ins = feedback.objects.all()
    for feed in feedback_ins:
        feed.rating = range(feed.rating)
    context = {"feedback": feedback_ins}
    return render(request, 'sitevisitor/home.html', context)


def user_logout(request):
    logout(request)
    return redirect("sitevisitor:home")

# View for registering Customers
def CustomerRegistrationView(request):
    if request.method == 'POST':
        userform = UserAuthenticationForm(request.POST)
        customerdetailsform = CustomerRegistrationForm(request.POST, request.FILES)

        if userform.is_valid() and customerdetailsform.is_valid():
            user = userform.save()  # Save the user first
            customer = customerdetailsform.save(commit=False)
            customer.user = user  # Link the customer to the user
            customer.save()  # Save the customer details

            messages.success(request, 'You are successfully registered as a customer.')
            return redirect('sitevisitor:login')  # Redirect to login page

    else:
        userform = UserAuthenticationForm()
        customerdetailsform = CustomerRegistrationForm()

    return render(request, 'sitevisitor/customer_registration.html', {'form': userform, 'form1': customerdetailsform})


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            customer = Customer.objects.filter(user__username=username, status='Active').count()
            theatre = Theatre.objects.filter(user__username=username, status='Active').count()

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    booking_data = request.session.get("booking")
                    if booking_data and booking_data.get('val') is not None:
                        screen_name = booking_data['screen_name']
                        url = reverse('sitevisitor:movie_booking', kwargs={'screen_name': screen_name})
                        return redirect(url)
                    elif customer != 0:
                        customer = Customer.objects.filter(user__username=username, status='Active').count()
                        if customer != 0:
                            customer_data = Customer.objects.filter(user__username=username, status='Active')
                            context = {
                                'customer': customer_data,
                                'logged_user': request.user,
                            }
                            return redirect('customer_home')

                        else:
                            msg = "Sorry the User doesnot exist. Kindly reach us through complaints@bookaplate.com"
                            return render(request, 'sitevisitor/home.html', {'msg': msg})
                    elif theatre != 0:
                        theatre = Theatre.objects.filter(user__username=username, status='Active').count()
                        if theatre != 0:
                            theatre_data = Theatre.objects.filter(user__username=username, status='Active')
                            context = {
                                'theatre': theatre_data,
                                'logged_user': request.user,
                            }
                            return redirect('theatre_profile')

                        else:
                            msg = "Sorry the User doesnot exist. Kindly reach us through complaints@bookaplate.com"
                            return render(request, 'sitevisitor/home.html', {'msg': msg})
                    else:
                        admin_data = User.objects.filter(username=username, is_superuser=True)
                        context = {
                            'admin': admin_data,
                            'logged_user': request.user,
                        }
                        return redirect('admin_home')

                except Exception as e:
                    print(e)

        else:
            form = LoginForm()
            error = "Invalid username or password"
            return render(request, 'sitevisitor/login.html', {'form': form, 'error': error})
    else:
        form = LoginForm()

    return render(request, 'sitevisitor/login.html', {'form': form})


def TheatreRegistrationView(request):
    if request.method == 'POST':
        userform = UserAuthenticationForm(request.POST)
        theatredetailsform = TheatreRegistrationForm(request.POST, request.FILES)

        if userform.is_valid() and theatredetailsform.is_valid():
            user = userform.save()  # Save the user first
            theatre = theatredetailsform.save(commit=False)
            theatre.user = user  # Link the theatre to the user
            theatre.save()  # Save the theatre details

            messages.success(request,
                             'You are successfully registered as a Theatre. Kindly wait for us to review the details and once we approve you will receive an email in your given email id. Thank you')
            return redirect('sitevisitor:login')  # Redirect to login page

    else:
        userform = UserAuthenticationForm()
        theatredetailsform = TheatreRegistrationForm()

    return render(request, 'sitevisitor/theatre_registration.html', {'form': userform, 'form1': theatredetailsform})


def mail(request, recipient_email, seatnumber):
    subject = 'Marvel Movie Ticket Confirmation'
    message = f'Hi, Enjoy the Movies with Loved Once! :\n\nYour Seats are: {seatnumber}'
    from_email = 'harishmarsekhar93@gmail.com'
    recipient_list = [recipient_email]
    send_mail(subject, message, from_email, recipient_list)
    # request.session['reset_code'] = random_code
    return HttpResponse('Email sent successfully.')


def Movies(request):
    movies = MovieDetails.objects.all()

    return render(request, 'sitevisitor/Movie_list_page.html', {'movies': movies})


def Movie_booking(request, screen_name):
    ScreenDetails_ins = get_object_or_404(ScreenDetails, screen_name=screen_name)
    Theatre_capacity = range(ScreenDetails_ins.seat_count)
    hole_booked_seats = []
    seats_list = []

    def seat_labels(capacity):
        seat_labels = []
        rows = capacity // 10

        for row in range(rows):
            for seat_num in range(1, 11):
                seat_labels.append(f"{chr(65 + row)}{seat_num}")

        return seat_labels

    Theatre_capacity_label = seat_labels(len(Theatre_capacity))

    if request.user.is_authenticated:
        user = request.user
        user_email = user.email
        print(user_email)
        if request.method == 'POST':
            selected_seats = request.POST.getlist('selected_seats')
            print("Selected seats:", selected_seats)
            user_selected_seats = [j for j in selected_seats if j != ""]
            seats_list.extend(user_selected_seats)
            print("Selected seats_final", user_selected_seats)
            request.session['selected_seats'] = user_selected_seats
            time = request.session.get("time")
            lang = request.session.get("lang")
            date = request.session.get("date")
            seat_instance = user_seats(user_id=user, seat_name='', time=time, language=lang, date_field=date, audi_name=ScreenDetails_ins)
            seat_instance.set_characters(user_selected_seats)
            seat_instance.save()
            return redirect("sitevisitor:payment")
    else:
        request.session['booking'] = {"val": True, "screen_name": screen_name}
        messages.success(request,"You are not logged in, please login if you have existing account else please "
                                 "regiseter and"
                         "Login")

        return render(request, "sitevisitor/customer_registration.html")

    seat_details = user_seats.objects.filter(audi_name=ScreenDetails_ins)
    # print("seatdetails using audi",seat_details)
    for i in seat_details:
        # retrieved_characters = i.seat_name.split("-")
        # print("retrived",retrieved_characters)
        for k in eval(i.seat_name):
            hole_booked_seats.append(str(k))
    print("booked seats", hole_booked_seats)
    context = {"screen_name":screen_name, "booked_seats": hole_booked_seats, "seat_capacity":Theatre_capacity_label}
    return render(request, 'sitevisitor/movie_booking.html',context)


def movies_in_theaters(request):
    movie_theaters = MovieTheaters.objects.all()
    movies_in_theaters = []

    for movie_theater in movie_theaters:
        # print(movie_theater)
        movie = movie_theater.movies
        license_numbers = [theater.license_number for theater in movie_theater.theaters.all()]
        # print(theater_ids[0])
        # status = [theater.status for theater in movie_theater.theaters.all()]
        movies_in_theaters.append({
            'theater_id': license_numbers[0],
            'theaters': ', '.join(map(str, movie_theater.theaters.all())),
            'movie_name': movie.movie_name if movie else 'No Movie Available',
            'movie_poster': movie.banner_photo.url if movie and movie.banner_photo else None,
        })
        print(movies_in_theaters)

    context = {'movies_in_theaters': movies_in_theaters}
    return render(request, 'sitevisitor/movies_in_theaters.html', context)

def payment(request):
    bank = Bank.BANK_CHOICES
    print([j for j in bank])

    selected_seats = request.session.get('selected_seats')
    print("selected_seats: in payment", selected_seats)
    total_Ammount = 0
    for seat in selected_seats:
        if seat[0] in range(1,17):
            total_Ammount += 300
        elif seat[0] in range(17,51):
            total_Ammount += 250
        elif seat[0] in range(51,61):
            total_Ammount += 200
        else:
            total_Ammount += 150
    context = {"bank_choice": bank, "month_choice": Bank.MONTH_CHOICES, "total_amount": total_Ammount}
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        account_number = request.POST['account_no']
        bank_name = request.POST['bank']
        card_no = request.POST['card_no']
        ifsc = request.POST['ifsc']
        exp_year = request.POST['exp_year']
        exp_month = request.POST['month']
        cvv = request.POST['cvv']
        if Bank.objects.filter(phone=phone).exists():
            error_msg = True
            return render(request, 'sitevisitor/payment.html', {"error_msg": error_msg, "phone": phone, "total_amount": total_Ammount, "bank_choice": bank, "month_choice": Bank.MONTH_CHOICES})
        else:
            Bank.objects.create(
                bank_name=bank_name,
                account_number=account_number,
                ifsc=ifsc,
                card_number=card_no,
                cvv=cvv,
                expiry_month=exp_month,
                expiry_year=exp_year,
                email=email,
                phone=phone
            )

            saved_successfully = True
            context_1 = {'saved_successfully': saved_successfully}

            html_message = render_to_string('sitevisitor/email_template.html', {'variable': 'value'})
            plain_text = strip_tags(html_message)

            email = EmailMultiAlternatives(
                subject='Marvel Movie Ticket Confirmation',
                body=plain_text,
                from_email='vinsshaji2@gmail.com',
                to=[email],
            )
            email.attach_alternative(html_message, "text/html")
            email.send()
            ####Feedback#### -
            # user = request.user
            # print()
            # seat = user_seats.objects.filter(user_id=user)
            # print(seat)
            # print("current user", seat)
            # current_date = date.today()
            # if seat.date_field < current_date:
            #     context_2 = {"data": True}
            #     return render(request, "sitevisitor/payment.html", context_2)
            return render(request, 'sitevisitor/payment.html', context_1)

    return render(request, "sitevisitor/payment.html", context)


def feedback_info(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        messages = request.POST['message']
        rating = request.POST['rating']
        current_datetime = datetime.datetime.now()
        formatted_date = current_datetime.strftime("%B %d, %Y")

        feedback.objects.create(
            customer_name=name,
            customer_email=email,
            feed_message=messages,
            rating=rating,
            date=formatted_date

        )
        thanks = True
        context_1 = {'saved_successfully': thanks}
        return render(request, 'sitevisitor/home.html', context_1)
    return render(request, "sitevisitor/feedback.html")

def screen(request, theater_id):
    theater = get_object_or_404(Theatre, license_number=theater_id)
    screens = ScreenDetails.objects.filter(theatre=theater)
    context = {
        'theater': theater,
        'screens': screens,
    }
    print(context)
    if request.method == 'POST':
        screen_name = request.POST.get("screen", "")
        date = request.POST.get("date", "")
        time = request.POST.get("time", "")
        language = request.POST.get("lang", "")
        request.session["time"] = time
        request.session["lang"] = language
        request.session["date"] = date
        if screen_name:
            redirect_url = reverse('sitevisitor:movie_booking', kwargs={'screen_name': screen_name})
            return redirect(redirect_url)
    return render(request, "sitevisitor/screen_selection.html", context)