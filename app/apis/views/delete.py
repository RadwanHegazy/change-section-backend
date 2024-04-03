from rest_framework import status,decorators
from rest_framework.response import Response
from ...models import Post

@decorators.api_view(['DELETE'])
def DeletePost(request,post_id):
    try : 
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({
                'message' : "post not found"
            },status=status.HTTP_204_NO_CONTENT)
        
        student_collage_id = request.data.get('student_id',None)
        if student_collage_id is None : 
            return Response({
                'message' : 'student_id not found'
            },status=status.HTTP_400_BAD_REQUEST)
        
        if int(student_collage_id) != post.student_collage_id : 
            return Response({
                'message' : 'invalid student_id for this post'
            },status=status.HTTP_400_BAD_REQUEST)
        
        post.delete()
        return Response({
            'message' : 'post deleted successfully'
        },status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)