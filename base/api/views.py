from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
from base.api import serializers

@api_view(['GET' , 'PUT' , 'POST'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET / api/rooms',
        'GET / api/rooms/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) #many means are there going to be multiple objects to be serialized.
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) #many means are there going to be multiple objects to be serialized.
    return Response(serializer.data)    