from django.db import models

# Modelo de Tickets
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.TextField(null=True)