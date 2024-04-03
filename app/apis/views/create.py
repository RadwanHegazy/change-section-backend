from rest_framework import decorators, status
from rest_framework.response import Response
from ..serializers import PostSerializer

@decorators.api_view(['POST'])
def CreatePost (request) : 
    try :
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)