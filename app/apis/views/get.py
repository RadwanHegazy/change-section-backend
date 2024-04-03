from rest_framework import status,decorators
from rest_framework.response import Response
from ...models import Post
from globals.pagination import PaginationMainClass
from ..serializers import PostSerializer
from django.core.cache import cache
from datetime import timedelta

@decorators.api_view(['GET'])
def GetPosts (request) : 
    try :
        # get cached posts
        cached_posts = cache.get('posts',None)

        if cached_posts is None :
            # get data from db
            posts = Post.objects.all()
            cache.set('posts',posts,timedelta(hours=2).total_seconds())    
        else:
            # get data from cache
            posts = cached_posts

        post_level = request.GET.get('level',None)
        from_section = request.GET.get('from_section',None)
        to_section = request.GET.get('to_section',None)

        if post_level :
            posts = posts.filter(level=post_level)

        if from_section : 
            from_section = int(from_section)
            posts = posts.filter(to_section=from_section)
        
        if to_section :
            to_section = int(to_section) 
            posts = posts.filter(from_section=to_section)
        

        paginator = PaginationMainClass(
            queryset=posts,
            request=request,
            serializer_class=PostSerializer,
        )        
        data = paginator.start()
        return Response(data,status=status.HTTP_200_OK)
    except Exception as error:
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)