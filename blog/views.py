from rest_framework.views import APIView
from .models import Post
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import pagination

class getPosts(APIView):
    def get(self,request):
        posts = Post.objects.order_by('-created')
        paginator = pagination.PageNumberPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class getPost(APIView):
    def get(self,request,pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)