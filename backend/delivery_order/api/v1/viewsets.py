from rest_framework import authentication
from delivery_order.models import PaymentMethod, Order, Bill
from .serializers import PaymentMethodSerializer, OrderSerializer, BillSerializer
from rest_framework import viewsets


class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Bill.objects.all()


class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PaymentMethod.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Order.objects.all()
