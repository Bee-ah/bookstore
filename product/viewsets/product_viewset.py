from rest_framework.viewsets import ModelViewSet

from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer #requisito
    
    def get_queryset(self):
        return Product.objects.all().order_by("id")