from django.shortcuts import render,redirect
import requests
from django.contrib import messages
import json


url = "http://192.168.43.61:8000"

def showHomepage(request):
    try:
        res = requests.get(url+"/all_products/")

    except requests.exceptions.ConnectionError:
        messages.error(request, "Server Not Available")
        return redirect('homepage')
    else:
        if res.status_code==200:
            dict = res.json()
            return render(request, "homepage.html", {"data":dict})
        else:
            json_data=res.json()
            messages.error(request,json_data)
            return redirect('homepage')

def consumerLogin(request):
    return render(request,"consumer_login.html")


def consumerLoginCheck(request):
    email_or_mobile = request.POST["email_or_mobile"]
    password = request.POST["password"]

    try:
        res = requests.get(url+"/login/"+email_or_mobile+"&"+password+"/")
    except requests.exceptions.ConnectionError:
        messages.error(request, "Server Not Available")
        return redirect('homepage')
    else:
        if res.status_code==200:
            data1 = res.json()
            return render(request,"consumer_account.html",{"details":data1})
        else:
            json_data = res.json()
            messages.error(request,json_data)
            return redirect("consumer_login")

def consumerRegistration(request):
    try:
        res = requests.get(url+"/get_last_consumer_id/")
    except requests.exceptions.ConnectionError:
        messages.error(request, "Server Not Available")
        return redirect('homepage')
    else:
        dict = res.json()
        return render(request, "consumer_registration.html", dict)



def saveConsumer(request):
    consumer_id = request.POST['consumer_id']
    consumer_name = request.POST['consumer_name']
    consumer_contact_no = request.POST['consumer_contact']
    consumer_address = request.POST['consumer_address']
    consumer_email = request.POST['consumer_email']
    consumer_password = request.POST['consumer_password']
    consumer_status = request.POST['status']

    dict = {"consumer_id":consumer_id,
            "consumer_name":consumer_name,
            "consumer_contact_no":consumer_contact_no,
            "consumer_address":consumer_address,
            "consumer_email":consumer_email,
            "consumer_password":consumer_password,
            "consumer_status":consumer_status}
    json_data=json.dumps(dict)
    try:
        res = requests.post(url+"/save_consumer/",data=json_data)
    except requests.exceptions.ConnectionError:
        messages.error(request, "Server Not Available")
        return redirect('homepage')
    else:
        if res.status_code == 200:
            result = res.json()
            messages.success(request,result)
            return redirect('consumer_registration')
        else:
            result = res.json()
            messages.success(request, result)
            return redirect('consumer_registration')


