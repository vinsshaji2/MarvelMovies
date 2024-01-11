from django.db import models
from django.contrib.auth.models import User
import json


# Define your models here

class Customer(models.Model):
    # Customer model for storing customer information
    customer_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    STATES_CHOICES = [
        ('', 'Select State'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal')
    ]

    state = models.CharField(max_length=100, choices=STATES_CHOICES, default='')
    status = models.CharField(max_length=10, default='Active')
    profile_photo = models.ImageField(upload_to='profile_pictures/', blank=True)
    id_proof = models.ImageField(upload_to='customer_identifier/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Theatre(models.Model):
    # Theatre model for storing theatre information
    theatre_id = models.AutoField(primary_key=True)
    theatre_name = models.CharField(max_length=234, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    STATES_CHOICES = [
        ('', 'Select State'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal')
    ]

    state = models.CharField(max_length=100, choices=STATES_CHOICES, default='')
    status = models.CharField(max_length=10, default='Inactive')
    pancard = models.ImageField(upload_to='business_pan/', blank=True)
    license_number = models.CharField(max_length=100, unique=True)
    seat_capacity = models.IntegerField(default=260)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.theatre_name


class ScreenDetails(models.Model):
    # Model for storing details about screens in theatres
    screen_id = models.AutoField(primary_key=True)
    screen_name = models.CharField(max_length=100, unique=True)
    seat_count = models.IntegerField(default=100)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)

    def __str__(self):
        return self.screen_name

class MovieDetails(models.Model):
    # Model for storing details about movies
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    banner_photo = models.ImageField(upload_to='movie_banners/', null=True)
    description = models.TextField()

    def __str__(self):
        return self.movie_name

class ShowDetails(models.Model):
    # Model for storing details about movie shows
    show_id = models.AutoField(primary_key=True)
    show_timing = models.TimeField()
    movie = models.ManyToManyField(MovieDetails)
    screen = models.ManyToManyField(ScreenDetails)

    def __str__(self):
        return self.show_timing



class TicketDetails(models.Model):
    # Model for storing details about tickets
    ticket_id = models.AutoField(primary_key=True)
    TICKET_CHOICES = [
        ('Economy', 'Economy'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
        ('VIP', 'VIP'),
        ('Deluxe', 'Deluxe'),
        ('Royal', 'Royal'),
    ]
    ticket_type = models.CharField(max_length=50, choices=TICKET_CHOICES, default='Economy')
    rate = models.IntegerField()
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticket_id

class SlotDetails(models.Model):
    # Model for storing details about slots (seats in a screen)
    ROW_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'J'),
        ('K', 'K'),
        ('L', 'L'),
        ('M', 'M'),
        ('N', 'N'),
        ('O', 'O'),
        ('P', 'P'),
        ('Q', 'Q'),
        ('R', 'R'),
        ('S', 'S'),
        ('T', 'T'),
        ('U', 'U'),
        ('V', 'V'),
        ('W', 'W'),
        ('X', 'X'),
        ('Y', 'Y'),
        ('Z', 'Z'),
    ]
    slot_id = models.AutoField(primary_key=True)
    row = models.CharField(max_length=2, choices=ROW_CHOICES, default='A')
    seat_number = models.IntegerField(default=1)
    screen = models.ForeignKey(ScreenDetails, on_delete=models.CASCADE)
    ticket = models.ForeignKey(TicketDetails, on_delete=models.CASCADE, null=True, blank=True)


class BookingDetails(models.Model):
    # Model for storing details about bookings
    booking_id = models.AutoField(primary_key=True)
    date = models.DateField()
    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Booked')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    slot = models.ManyToManyField(SlotDetails)


class Bank(models.Model):
    # Model for storing details about banks
    bank_id = models.AutoField(primary_key=True)
    BANK_CHOICES = [
        ('State Bank of India', 'SBI'),
        ('HDFC Bank', 'HDFC'),
        ('ICICI Bank', 'ICICI'),
        ('Punjab National Bank', 'PNB'),
        ('Axis Bank', 'Axis'),
        ('Canara Bank', 'Canara'),
        ('Bank of Baroda', 'BoB'),
        ('Union Bank of India', 'UBI'),
        ('IDBI Bank', 'IDBI'),
        ('Kotak Mahindra Bank', 'Kotak'),
        ('IndusInd Bank', 'IndusInd'),
        ('Yes Bank', 'Yes'),
        ('Bank of India', 'BOI'),
        ('Central Bank of India', 'CBI'),
        ('Indian Bank', 'Indian Bank'),
        ('Federal Bank', 'Federal'),
        ('Karur Vysya Bank', 'KVB'),
        ('Punjab & Sind Bank', 'PSB'),
        ('UCO Bank', 'UCO'),
        ('DBS Bank India', 'DBS'),
    ]
    bank_name = models.CharField(max_length=100, choices=BANK_CHOICES)
    account_number = models.CharField(max_length=25)
    ifsc = models.CharField(max_length=25)
    card_number = models.CharField(max_length=25)
    cvv = models.CharField(max_length=3)
    MONTH_CHOICES = [
        ('01', 'JAN'),
        ('02', 'FEB'),
        ('03', 'MAR'),
        ('04', 'APR'),
        ('05', 'MAY'),
        ('06', 'JUN'),
        ('07', 'JUL'),
        ('08', 'AUG'),
        ('09', 'SEP'),
        ('10', 'OCT'),
        ('11', 'NOV'),
        ('12', 'DEC'),
    ]
    expiry_month = models.CharField(max_length=100, choices=MONTH_CHOICES)
    expiry_year = models.IntegerField()
    phone = models.CharField(max_length=13, unique=True)
    email = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)


class MovieTheaters(models.Model):
    theaters = models.ManyToManyField(Theatre)
    movies = models.ForeignKey(MovieDetails, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{', '.join(map(str, self.theaters.all()))} - {self.movies}"


class user_seats(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_name = models.TextField()
    time = models.TextField()
    language = models.CharField(max_length=30)
    date_field = models.DateField(default=None)
    audi_name = models.ForeignKey(ScreenDetails, on_delete=models.CASCADE)

    def set_characters(self, characters_list):
        self.seat_name = f"{self.seat_name}{json.dumps(characters_list)}"

    def get_characters(self):
        try:
            _, characters_json = self.seat_name.split(' - ')
            return json.loads(characters_json)
        except ValueError:
            return []

    def __str__(self):
        return f'Movie with characters: {self.get_characters()}'


class seats(models.Model):
    seat_name = models.TextField(primary_key=True)


class feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=40)
    customer_email = models.EmailField()
    feed_message = models.TextField()
    rating = models.IntegerField()
    date = models.TextField()

    def __str__(self):
        return f"Feedback {self.feed_id}"



    
