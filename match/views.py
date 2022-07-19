from .models import Match
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MatchSerializer


class getMatches(APIView):
    def get(self, request):
        matches = Match.objects.order_by('-created')
        serializer = MatchSerializer(matches, many=True, context={'request': request})
        return Response(serializer.data)
        
        
        