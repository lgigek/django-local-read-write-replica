import logging
from typing import Dict

from django.db import transaction
from rest_framework import serializers

from django_local_read_write_replica.apps.my_app.models import Message

logger = logging.getLogger(__name__)


class NewMessageSerializer(serializers.SerializerMethodField):

    text = serializers.CharField(max_length=200)

    @staticmethod
    def create(validated_data: Dict) -> Message:
        with transaction.atomic():  # <- created useless transaction to force read/write evidences
            created_message = Message.objects.create(text=validated_data["text"])
            logger.info("Message created with id: %s", created_message.id)
            return created_message
