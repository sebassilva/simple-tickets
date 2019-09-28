from rest_framework import serializers
from ticket_manager.models import Ticket
from rest_framework.response import Response
from rest_framework import status



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'price', 'is_sold', 'is_available', 'user']

    def update(self, instance, validated_data):
        # Validamos si el ticket no ha sido apartado o comprado
        if not instance.is_available:
            raise serializers.ValidationError("El ticket ya está apartado y no se puede comprar. Intenta en un par de minutos.")

        if instance.is_sold:
            raise serializers.ValidationError("El ticket ya ha sido comprado.")

        if instance.user is not None and instance.user != validated_data['user']:
            raise serializers.ValidationError("No eres el propietario de este ticket. Intenta de nuevo")

        if validated_data['is_sold'] == True:
            validated_data['is_available'] = False
        
        return super(TicketSerializer, self).update(instance, validated_data)



class BuyTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'price', 'is_sold', 'is_available']
