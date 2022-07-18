from rest_framework.views import APIView
from .models import Pokemons
from rest_framework.response import Response
from rest_framework import status
from .serializers import PokemonSerializer
from django.http import Http404

class PokemonDetails(APIView):
    def get_queryset(self, name):
        """
        Get queryset by name.

        Keyword arguments:
        name -- Pokemon name
        """
        queryset = Pokemons.objects.filter(name__icontains=name)
        if len(queryset) > 0:
            return queryset 
        else:
            raise Http404
    def get(self, request, name):
        """
        Return data of pokemon by name.

        Keyword arguments:
        name -- Pokemon name
        """
        pokemon = self.get_queryset(name)
        serializer = PokemonSerializer(pokemon, many=True)
        return Response(serializer.data)