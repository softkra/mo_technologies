from django.db import models
from django.forms import IntegerField
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext as _

class Pokemons(TimeStampedModel):
    id = models.IntegerField(primary_key=True, auto_created=False)
    name = models.CharField(verbose_name=_("Pokemon Name"), max_length=100)
    height = models.IntegerField(verbose_name=_("Pokemon Height"))
    weight = models.IntegerField(verbose_name=_("Pokemon Weight"))
    stats = models.JSONField(verbose_name=_("Pokemon Stats"))
    evolution = models.JSONField(verbose_name=_("Pokemon Evolution"))

    class Meta:
        verbose_name = _('Pokemon')
        verbose_name_plural = _('Pokemons')

class Logs(TimeStampedModel):
    request_url = models.CharField(verbose_name=_("URL"), max_length=255, null=True, blank=True)
    response_status = models.CharField(verbose_name=_("response status"), max_length=255, null=True, blank=True)
    response_body = models.TextField(verbose_name=_("response body"), null=True, blank=True)
    message = models.CharField(verbose_name=_("internal message"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('Log')
        verbose_name_plural = _('Logs')