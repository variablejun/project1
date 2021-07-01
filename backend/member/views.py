from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from member.models import MemberVO
from member.serializers import MemberSerializers
from rest_framework.decorators import api_view, parser_classes
from icecream import ic
from member.serializers import MemberSerializers

@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def members(request):
    print('=== 여기까지는 왔다 !! ')
    if request.method == 'GET':
        all_members = MemberVO.objects.all()
        serializer = MemberSerializers(all_members, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == 'POST':
        new_member = request.data['body']
        ic(new_member)
        serializer = MemberSerializers(data = new_member)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result':f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def member(request, pk):
    if request.method == 'GET':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)