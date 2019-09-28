from rest_framework import generics
from ticket_manager.models import Ticket
from ticket_manager.serializers import TicketSerializer, BuyTicketSerializer

class TicketView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# Operaciones para comprar y dejar el ticket
class BuyTicket(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = BuyTicketSerializer


class ReleaseTicket(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer