import random

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import MerchantModal
from admin_project_provider import settings as se
from django.views.generic import ListView


# Create your views here.
def showHomepage(request):
    username = request.POST.get('admin_username')
    password = request.POST.get('admin_password')

    if username == "ravi" and password == "Ravi@1993":
        return render(request, "admin/homepage.html")
    else:
        messages.error(request, "Invalid Username or Password")
        return redirect('logout')


def merchantRegistration(request):
    try:
        res = MerchantModal.objects.all()[::-1][0]
        idno = int(res.id) + 1
        return render(request, "merchant/merchant_registration.html", {"idno": idno})
    except IndexError:
        idno = 10000001
        return render(request, "merchant/merchant_registration.html", {"idno": idno})


def saveMerchant(request):
    idno = request.POST.get('idnumber')
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    email = request.POST.get('email')

    # Auto Password Generation
    password = contact[0] + (str(int(idno) + len(name))) + contact[-1]
    password = email[0] + password[:(int(len(password) / 2))] + email[1] + password[(int(len(password) / 2)):] + email[2]
    #--------------------------

    MerchantModal(id=idno, merchant_name=name, merchant_contact=contact, merchant_email=email,merchant_password=password).save()
    subject = "Login Details Of RJ Online Shopping"
    message = "Thanks for registered with RJ Online Shopping. Your Registered ID : "+idno+ " Username : " + email + " and Password : " + password
    send_mail(subject, message, se.EMAIL_HOST_USER, [email])
    messages.success(request,name + " is registered successfully")
    return merchantRegistration(request)


class ViewAllMerchants(ListView):
    model = MerchantModal
    template_name = "merchant/merchants_list.html"


def deleteMerchant(request):
    id = request.GET.get('merchentid')
    MerchantModal.objects.filter(id=id).delete()
    return redirect('view_merchant')