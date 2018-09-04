from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from  src.exchange.models import Exchange
from  src.rate.models import Rate
from src.exchange.serializers import ExchangeSerializer
from django.db import transaction
import datetime

@method_decorator(csrf_exempt, name='dispatch')
class ExchangeView(APIView):
    def get(self, request, id='', format=None):
        if request.method == 'GET':
            exchange = Exchange.objects.all()
            res = []

            for x in exchange:
                rate = Rate.objects.get(pk=x.rate_id)
                data = {
                    "id": x.id,
                    "fromRate": rate.fromRate,
                    "toRate": rate.toRate,
                    "value": x.value,
                    "date": x.date.strftime('%d %b %Y')
                }
                res.append(data)
            # serializer = ExchangeSerializer(exchange, many=True)
            return JsonResponse(res, safe=False)

    @method_decorator(transaction.atomic, name='dispatch')
    def post(self, request, *args, **kwargs):
        """
        Create account
        """

        if request.method == 'POST':
            data = JSONParser().parse(request)
            data['date'] = data['date'] + "T23:59:59"

            serializer = ExchangeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)