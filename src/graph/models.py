from __future__ import unicode_literals
from django.conf import settings
from colorful.fields import RGBColorField

from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class Graph(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField()
    color_code = RGBColorField()
    single_data = models.IntegerField(_("Single Data"), default=0, null=True)
    multipe_data = models.BooleanField(_("Multipe Data"), default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = _("Graph")
        verbose_name_plural = _("Graph")

    def __unicode__(self):
        return smart_unicode(self.name)


class GraphData(models.Model):
    graph = models.ForeignKey(Graph, related_name='graph_data', on_delete=models.CASCADE)
    label = models.CharField(_("Label"), max_length=250)
    data = models.IntegerField(_("Data"), default=0)

    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Graph Data'
        verbose_name_plural = 'Graph Data'

    def __unicode__(self):
        return "{}".format(self.label)