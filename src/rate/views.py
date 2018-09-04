from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from  src.rate.models import Rate
from src.rate.serializers import RateSerializer
from django.db import transaction

@method_decorator(csrf_exempt, name='dispatch')
class RateView(APIView):
    def get(self, request, id='', format=None):
        if request.method == 'GET':
            rate = Rate.objects.all()
            serializer = RateSerializer(rate, many=True)
            return JsonResponse(serializer.data, safe=False)

    @method_decorator(transaction.atomic, name='dispatch')
    def post(self, request, *args, **kwargs):
        """
        Create account
        """

        if request.method == 'POST':
            data = JSONParser().parse(request)

            serializer = RateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id='', *args, **kwargs):
        res = {
            "message": ''
        }
        try:
            rate = Rate.objects.get(pk=id)
            res['message'] = 'success delete rate'
            rate.delete()
            return JsonResponse(res, status=204)
        except Rate.DoesNotExist:
            res['message'] = "rate doesn't exist"
            return JsonResponse(res, status=404)