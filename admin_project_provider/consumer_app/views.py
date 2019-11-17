from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import ConsumerDetailsModel
import json
from .forms import ConsumerDetailsForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from merchant_app.models import ProductDetailsModal
from django.core.serializers import serialize


class ShowAllProducts(View):
    def get(self,request):
        res = ProductDetailsModal.objects.all()
        if res:
            json_data = serialize("json",res,fields=("p_name","p_price"))
            return HttpResponse(json_data, content_type="application/json", status=200)
        else:
            json_data = json.dumps("No Products Available")
            return HttpResponse(json_data, content_type="application/json", status=500)


class GetLastConsumerId(View):
    def get(self, request):
        try:
            res = ConsumerDetailsModel.objects.all()[::-1][0]
            dict = {"consumer_id":res.consumer_id+1}
            json_data = json.dumps(dict)
            return HttpResponse(json_data,content_type="application/json")
        except IndexError:
            res = 10000001
            dict = {"consumer_id": res}
            json_data = json.dumps(dict)
            return HttpResponse(json_data, content_type="application/json")

@method_decorator(csrf_exempt,name="dispatch")
class ConsumerDetails(View):
    def post(self,request):
        data = request.body
        consumer_details = json.loads(data)
        consumer_form = ConsumerDetailsForm(consumer_details)

        if consumer_form.is_valid():
            consumer_form.save()
            json_data = json.dumps("Consumer Details Saved Successfully")
            return HttpResponse(json_data,content_type="application/json",status=200)
        if consumer_form.errors:
            json_data = json.dumps(consumer_form.errors)
            return HttpResponse(json_data, content_type="application/json", status=500)


class CheckLoginDetails(View):
    def get(self,request,email_or_mobile,password):
        try:
            res=ConsumerDetailsModel.objects.get(consumer_email=email_or_mobile,consumer_password=password)
            json_data= serialize("json",[res])
            return HttpResponse(json_data,content_type="application/json",status=200)
        except ConsumerDetailsModel.DoesNotExist:
            try:
                res= ConsumerDetailsModel.objects.get(consumer_contact_no=email_or_mobile,consumer_password=password)
                json_data = serialize("json", [res])
                return HttpResponse(json_data, content_type="application/json", status=200)
            except ConsumerDetailsModel.DoesNotExist:
                json_data=json.dumps("Invalid Login Details")
                return HttpResponse(json_data, content_type="application/json", status=500)
            except ValueError:
                json_data = json.dumps("Invalid Login Details")
                return HttpResponse(json_data, content_type="application/json", status=500)