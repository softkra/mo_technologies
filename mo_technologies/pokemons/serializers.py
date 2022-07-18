from rest_framework import serializers
from .models import Pokemons, Logs

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemons
        fields = '__all__'

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'