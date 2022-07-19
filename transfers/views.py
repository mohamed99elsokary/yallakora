from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transfer
from .serializers import TransferSerializer

class getTransfers(APIView):
    def get(self, request):
        transfers = Transfer.objects.all()
        serializer = TransferSerializer(transfers, many=True, context={'request': request})
        return Response(serializer.data)
