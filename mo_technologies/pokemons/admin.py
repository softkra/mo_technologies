from django.contrib import admin
from .models import Pokemons, Logs
# Register your models here.

class PokemonsAdmin(admin.ModelAdmin):
    list_filter = ('created',)
    list_display = ('id', 'name', 'height', 'weight')
admin.site.register(Pokemons, PokemonsAdmin)

class logsAdmin(admin.ModelAdmin):
    list_filter = ('request_url', 'response_status', 'created')
    list_display = ('id', 'request_url', 'response_status', 'created')
admin.site.register(Logs, logsAdmin)