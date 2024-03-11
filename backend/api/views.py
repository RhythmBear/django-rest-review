from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    
    # POST
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        
        return Response(serializer.data)


    return Response({'invalid': "Bad Data Provided"}, status=400)

    # # Get
    # instance = Product.objects.all().order_by('?').first()
    # data = {}

    # if instance:
    #     data = ProductSerializer(instance).data
        
    # return Response(data)