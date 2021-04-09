from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


class TicketListView(GenericAPIView):
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request):
        objects = Ticket.objects.all()
        serializer = TicketSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_200_OK) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetailView(GenericAPIView): 

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request, pk, *args, **kwargs):
        objects = Ticket.objects.get(pk=pk)
        serializer = TicketSerializer(objects)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        objects = Ticket.objects.get(pk=pk)
        Postobjects = JSONParser().parse(request) 
        serializer = TicketSerializer(objects, data=Postobjects)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, pk, *args, **kwargs):
        objects = Ticket.objects.get(pk=pk)
        objects.delete()
        return Response(status.HTTP_200_OK)
