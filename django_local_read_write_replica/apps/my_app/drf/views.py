import logging

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet

from django_local_read_write_replica.apps.my_app.drf.serializers import NewMessageSerializer
from django_local_read_write_replica.apps.my_app.models import Message

logger = logging.getLogger(__name__)


class MessageViewSet(ModelViewSet):

    queryset = Message.objects.all().order_by("-created_at")

    def create(self, request, *args, **kwargs):

        logger.info("Received a request to create a new message with data: %s.", request.data)
        serializer = NewMessageSerializer(data=request.data)

        logger.info("Validating the serialized data.")
        if not serializer.is_valid():
            logger.warning("There were some errors during validation: %s", serializer.errors)
            raise ValidationError(serializer.errors)

        logger.info("Data is valid, saving Message...")
        created_message = serializer.create(serializer.validated_data)

        return Response({"id": str(created_message.id)}, HTTP_201_CREATED)
