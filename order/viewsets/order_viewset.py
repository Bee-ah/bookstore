from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer  # requisito
    queryset = Order.objects.all().order_by("id")  # requisito , padrão para o viewset

    authentication_classes = [TokenAuthentication]  # add Token authentication
    permission_classes = [IsAuthenticated]
