import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tickets.settings")
import django
django.setup()
from ticket_manager.models import Ticket



for i in range(0, 100):

    ticket = Ticket(is_sold=False, is_available=True, price=499)
    ticket.save()
    print("Creando Ticket: ", i)


