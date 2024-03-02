from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}

    if instance:
        # data = model_to_dict(instance, fields=['id', 'title','content', 'price'])
        # Serialization model_instace >> PythonDictionary >> return json

        data = ProductSerializer(instance).data
        
    return Response(data)