from rest_framework.viewsets import ModelViewSet

from product.models.product import Category
from product.serializers.category_serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer  # requisito

    def get_queryset(self):
        return Category.objects.all().order_by("id")
