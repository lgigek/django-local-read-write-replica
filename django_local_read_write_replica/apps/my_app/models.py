from uuid import uuid4

from django.db import models


class StandardModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name="ID")
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name="Updated at")

    class Meta:
        abstract = True


class Message(StandardModelMixin):
    text: models.CharField(max_length=200, blank=False, null=False)
