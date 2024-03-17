from rest_framework import generics, mixins

from .models import Product
from .serializers import ProductSerializer


# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         print("I'm Here!!!!!!!")
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)
#         # send a Django signal
#         print(serializer.validated_data)


# product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # lookup Field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup Field = 'pk'   

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title
    
product_update_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup Field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()



# Using Mixings and a Generic API VIew(Class Based View)

class ProductMixinView(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs): #HTTP 
        pk = kwargs.get("pk")

        if pk:
            return(self.retrieve(request, *args, **kwargs))
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        print(*args, **kwargs)
        return self.create(request, *args, **kwargs)
    
    def update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title
    

product_mixin_view = ProductMixinView.as_view()