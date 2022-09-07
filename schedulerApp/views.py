from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Request
from .serializers import RequestSerializer
from .task import reverse_request_title
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

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
            'title': request.data.get('title'),
            'scheduledDateTime': request.data.get('scheduledDateTime'),
            'status': 'pending'
        }
        serializer = RequestSerializer(data=data)
        if data['scheduledDateTime'] >= datetime.now().strftime('%Y-%m-%d %H:%M:%S'): 
            if serializer.is_valid():
                serializer.save()
                try:
                    scheduler = BackgroundScheduler()
                    scheduler.add_job(reverse_request_title, 'date', run_date=data['scheduledDateTime'], args=[serializer.data['id']], name=str(serializer.data['id']))
                    scheduler.start()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"You must insert a datetime in the future"}, status=status.HTTP_400_BAD_REQUEST) 