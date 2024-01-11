from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from adminpanel.models import Customer,User,user_seats


# Create your views here.
def HomeView(request):
    logged_user= request.user
    customer= get_object_or_404(Customer, user=logged_user) 
    context={
        'logged_user':logged_user,
        'customer':customer,
    }
    return render(request,'customers/customer_profile.html',context)


def ticket_info(request):
    global user_email, user_name, user_id
    if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id
        user_email = request.user.email
        user_name = request.user.username
    user_org = get_list_or_404(user_seats, user_id=user)
    lis = []
    dict = {}
    # for i in user_org:


    context = {
        "details": user_org,
        "username": user_name,
        "email": user_email,
    }


    return render(request, 'customers/ticket_info.html', context)