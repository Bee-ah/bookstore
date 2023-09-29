from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer #requisito
    queryset = Order.objects.all() #requisito , padrão para o viewset 
