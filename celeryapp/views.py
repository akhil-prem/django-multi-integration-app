from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .tasks import add


@api_view(['GET'])
def add_view(request):
    result = add.delay(4, 4)
    return Response({'task_id': result.id})
