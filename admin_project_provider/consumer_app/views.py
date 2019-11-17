from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import ConsumerDetailsModel


class GetLastConsumerId(View):
    def get(self, request):
        try:
            res = ConsumerDetailsModel.objects.all()[::-1][0]
            print(res)
            print(type(res))
        except IndexError:
            res = 10000001
            print(res)
            print(type(res))
        return None