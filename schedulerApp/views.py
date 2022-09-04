from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Request
from .serializers import RequestSerializer

class SchedulerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    # return list of all Request
    def get(self, request):
        requestItems = Request.objects.all()
        serializer = RequestSerializer(requestItems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # schedule new request
    def post(self, request):
        data = {
            'description': request.data.get('description'),
            'scheduledDateTime': request.data.get('scheduledDateTime'),
            'status': 'pending'
        }
        serializer = RequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 