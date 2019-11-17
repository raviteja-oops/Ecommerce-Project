from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
from admin_app.models import MerchantModal
import json
from django.core.serializers import serialize
from .forms import MerchantForm,ProductForm
from merchant_app.models import ProductDetailsModal



class CheckMerchantLoginDetails(View):
    def get(self,request,email,password):
        try:
            res = MerchantModal.objects.get(merchant_email=email,merchant_password=password)
            # json_data = serialize('json',[res])
            dict = {"id":res.id,
                    "merchant_name":res.merchant_name,
                    "merchant_contact":res.merchant_contact,
                    "merchant_email":res.merchant_email,
                    "merchant_password":res.merchant_password}
            json_data = json.dumps(dict)
            # print(json_data)
            return HttpResponse(json_data,content_type="application/json",status=200)
        except MerchantModal.DoesNotExist:
            d1 = {"message":"Invalid Username or Password"}
            json_data = json.dumps(d1)
            return HttpResponse(json_data,content_type="application/json",status=500)

@method_decorator(csrf_exempt,name="dispatch")
class ChangeMerchantPassword(View):
    def put(self,request,email,password):
        # print(email)
        # print(password)
        try:
            old_details = MerchantModal.objects.get(merchant_email=email,merchant_password=password)
        except MerchantModal.DoesNotExist:
            d1 = {"message":"Invalid Username or Password"}
            json_data = json.dumps(d1)
            return HttpResponse(json_data,content_type="application/json",status=500)
        else:
            old_details_dictionary = {"id":old_details.id,
                                      "merchant_name":old_details.merchant_name,
                                      "merchant_contact":old_details.merchant_contact,
                                      "merchant_email":old_details.merchant_email,
                                      "merchant_password":old_details.merchant_password}
            data = request.body
            new_details = json.loads(data)
            old_details_dictionary.update(new_details)
            merchant_data = MerchantForm(old_details_dictionary,instance=old_details)

            if merchant_data.is_valid():
                merchant_data.save()
                json_message =json.dumps("Merchant Password Changed Successfully")
                return HttpResponse(json_message,content_type="application/json",status=200)
            if merchant_data.errors:
                json_message = json.dumps(merchant_data.errors)
                return HttpResponse(json_message,content_type="application/json",status=500)

@method_decorator(csrf_exempt,name="dispatch")
class ProductDetails(View):
    def post(self,request):
        data = request.body
        product_details = json.loads(data)
        pf = ProductForm(product_details)

        if pf.is_valid():
            pf.save()
            json_data =json.dumps({"message":"Product Details Saved Successfully"})
            return HttpResponse(json_data,content_type="application/json",status=200)
        if pf.errors:
            json_data = json.dumps(pf.errors)
            return HttpResponse(json_data, content_type="application/json", status=500)

    def get(self,request,merchant_id):
        # print(merchant_id)
        res = ProductDetailsModal.objects.filter(merchant_id = merchant_id)
        # print(res)
        # print(type(res))
        if res:
            json_data = serialize('json',res,fields=("p_no","p_name","p_price","p_quantity"))
            # print(json_data)
            return HttpResponse(json_data,content_type="application/json",status=200)
        else:
            d1 = {"message": "No Data Available"}
            json_data = json.dumps(d1)
            return HttpResponse(json_data, content_type="application/json", status=500)

@method_decorator(csrf_exempt,name="dispatch")
class ModifyProductDetails(View):
    def get(self,request,product_id):
        res = ProductDetailsModal.objects.get(p_no=product_id)
        json_data = serialize('json',[res])
        print(json_data)
        return HttpResponse(json_data,content_type="application/json")


    def put(self,request,p_no):
        res = ProductDetailsModal.objects.get(p_no=p_no)
        old_data = {"p_no":res.p_no,
                  "p_name":res.p_name,
                  "p_price":res.p_price,
                  "p_quantity":res.p_quantity,
                  "merchant_id":res.merchant_id_id}
        data = request.body
        new_data = json.loads(data)
        old_data.update(new_data)
        # print(old_data)
        pf = ProductForm(old_data,instance=res)
        if pf.is_valid():
            pf.save()
            json_data = json.dumps("Product Updated Successfully")
            # print(json_data)
            return HttpResponse(json_data,content_type="application/json",status=200)
        if pf.errors:
            json_data=json.dumps(pf.errors)
            # print(json_data)
            return HttpResponse(json_data, content_type="application/json", status=500)


    def delete(self,request,p_no):
        res = ProductDetailsModal.objects.get(p_no=p_no).delete()
        json_data = json.dumps("Product Deleted Successfully")
        # print(json_data)
        return HttpResponse(json_data,content_type="application/json")
