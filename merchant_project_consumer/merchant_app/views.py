from django.shortcuts import render,redirect
import requests
from django.contrib import messages
import json
from django.views.decorators.cache import cache_control


# Create your views here.

url = "http://192.168.1.29:8000"

def showMerchantIndex(request):
    try:
        if eval(request.COOKIES["status"]):
            m_email = request.COOKIES["m_email"]
            m_old_password = request.COOKIES["m_old_password"]
            try:
                res = requests.get(url + "/check_details/" + m_email + "&" + m_old_password + "/")
                if res.status_code == 200:
                    res = res.json()
                    response = render(request, "merchant_account.html", {"data": res})
                    return response
                else:
                    messages.error(request, "Invalid Username or Password")
                    return redirect('main')
            except requests.exceptions.ConnectionError:
                messages.error(request, "Server Not Available")
                return redirect('main')
        else:
            return render(request, "merchent_login.html")
    except KeyError:
        return render(request,"merchent_login.html")


def changePassword(request):
    return render(request,"merchant_change_password.html")

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def loginCheck(request):
    m_email = request.POST.get('m_email')
    print(m_email)
    print(type(m_email))
    m_old_password = request.POST.get('m_password')
    try:
        res = requests.get(url+"/check_details/"+m_email+"&"+m_old_password+"/")
        # print(res)
        # print(type(res))
        if res.status_code == 200:
            res = res.json()
            # print(res)
            # global merchant_id
            # merchant_id = res.get("id")
            response = render(request,"merchant_account.html",{"data":res})
            response.set_cookie("status",True)
            response.set_cookie("m_email",m_email)
            response.set_cookie("m_old_password",m_old_password)
            response.set_cookie("merchant_id",res.get("id"))
            return response
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect('main')
    except requests.exceptions.ConnectionError:
        messages.error(request,"Server Not Available")
        return redirect('main')


def showHomepage(request):
    m_email = request.COOKIES["m_email"]
    m_old_password = request.COOKIES["m_old_password"]
    try:
        res = requests.get(url+"/check_details/"+m_email+"&"+m_old_password+"/")
        if res.status_code == 200:
            res = res.json()
            response = render(request,"merchant_account.html",{"data":res})
            return response
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect('main')
    except requests.exceptions.ConnectionError:
        messages.error(request,"Server Not Available")
        return redirect('main')


def passwordCheck(request):
    email = request.POST.get('m_email')
    old_password = request.POST.get('m_old_password')
    new_password = request.POST.get('password1')
    repeat_new_password = request.POST.get('password2')
    if new_password == repeat_new_password:
        password_dict = {"merchant_password":new_password}
        json_data = json.dumps(password_dict)
        try:
            res = requests.put(url+"/change_merchant_password/"+email+"&"+old_password+"/",data=json_data)
        except requests.exceptions.ConnectionError:
            messages.error(request, "Server Not Available")
            return redirect('change_password')
        else:
            if res.status_code == 200:
                response = res.json()
                messages.success(request,response)
                return redirect("change_password")
            else:
                response = res.json()
                messages.error(request, "Invalid Username or Password")
                return redirect("change_password")
    else:
        messages.error(request,"Mismatching Of New Password")
        return redirect('change_password')


def addProduct(request):
    merchant_id = request.COOKIES["merchant_id"]
    print(merchant_id)
    print(type(merchant_id))
    return render(request,"product/add_product.html",{"data":merchant_id})


def saveProduct(request):
    m_id = request.POST.get("merchant_id")
    p_no = request.POST.get("p_no")
    p_name = request.POST.get("p_name")
    p_price = request.POST.get("p_price")
    p_quantity = request.POST.get("p_quantity")
    product_details = {"merchant_id":m_id,
                       "p_no":p_no,
                       "p_name":p_name,
                       "p_price":p_price,
                       "p_quantity":p_quantity}
    json_data = json.dumps(product_details)
    try:
        res = requests.post(url+"/save_product/",data=json_data)
    except requests.exceptions.ConnectionError:
        messages.error(request, "Server Lost")
        return redirect('main')
    else:
        if res.status_code == 200:
            res = res.json()
            # print(res)
            messages.success(request,res.get("message"))
            return addProduct(request)
        else:
            res = res.json()
            # print(res)
            messages.error(request,"Product Number is already exist. Please try another one")
            return addProduct(request)


def viewProducts(request):
    merchant_id = request.COOKIES["merchant_id"]
    try:
        res = requests.get(url+"/view_all_products/"+str(merchant_id)+"/")
    except requests.exceptions.ConnectionError:
        messages.error(request, "Server Not Available")
        return redirect('main')
    else:
        if res.status_code == 200:
            res = res.json()
            # print(res)
            return render(request,"product/view_all_products.html",{"data":res})
        else:
            res = res.json()
            # print(res)
            message = "No Products Available"
            return render(request,"product/view_all_products.html",{"message":message})


def updateProduct(request):
    product_id = request.GET.get('product_id')
    res = requests.get(url+"/getone/"+product_id+"/")
    res = res.json()
    # print(res)
    return render(request,"product/update_product.html",{"data":res})


def saveUpdateProduct(request):
    product_id = request.POST.get('product_id')
    product_name = request.POST.get('product_name')
    product_price = request.POST.get('product_price')
    product_quantity = request.POST.get('product_quantity')


    dictionary = {"p_no":product_id,
                  "p_name":product_name,
                  "p_price":product_price,
                  "p_quantity":product_quantity}
    json_data = json.dumps(dictionary)
    try:
        res = requests.put(url+"/updateone/"+product_id+"/",data=json_data)
    except requests.exceptions.ConnectionError:
        messages.error(request, "Server Not Available")
        return redirect('main')
    else:
        if res.status_code == 200:
            response = res.json()
            print(response)
            messages.success(request, response)
            return redirect("view_products")
        else:
            response = res.json()
            messages.error(request, response)
            return redirect("view_products")


def deleteProduct(request):
    product_id = request.GET.get('product_id')
    # print(product_id)
    try:
        res = requests.delete(url+"/delete_product/"+product_id+"/")
    except requests.exceptions.ConnectionError:
        messages.error(request, "Server Not Available")
        return redirect('main')
    else:
        response = res.json()
        messages.success(request, response)
        return redirect("view_products")

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logOut(request):
    response = redirect("main")
    response.set_cookie("status", False)
    response.set_cookie("m_email", None)
    response.set_cookie("m_old_password", None)
    response.set_cookie("merchant_id", None)
    return response


