from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse
from .models import Post, Comment, Category, LikePost
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, LikePostSerializer
# Create your views here.

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.settings import api_settings


class CategoryListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes =[IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CategoryDetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


# class PostCatergories(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     pagination_class = PageNumberPagination
#
#     def get_queryset(self):
#         catergories = self.request.category
#         return

class UserOnlyPostList(generics.ListAPIView):
    """
        This end point filters the post to show only the entered user's post
        These are the posts that will show on their profiles
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        """
            this view returns the user's posts as determined by the username entered in the url
        """
        username = self.kwargs['username']
        return Post.objects.filter(author__user__username=username)


class CurrentUserPostListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        """
        This end point filters to show the loggedin user's posts
        """
        current_user = self.request.user.profile
        return Post.objects.filter(author=current_user)


class PostListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('title', 'description', 'author__user__username', 'category__name')


class PostCreateView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)


class PostUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        owner = self.request.user.profile.user

        if owner == instance.author.user:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class PostDetailView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)


class PostDeleteView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        owner = self.request.user.profile.user
        if owner == instance.author.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            # return HttpResponse('You are not allowed to remove this post')
            return Response(status=status.HTTP_403_FORBIDDEN)


class CommentListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)


class CommentUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        owner = self.request.user.profile.user

        if owner == instance.author.user:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            sts = status.HTTP_201_CREATED
            return Response(serializer.data, sts)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class CommentDetailView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDestroyView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        current_user = self.request.user.profile.user
        if current_user == instance.author.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class LikePostListView(generics.ListAPIView):
    queryset = LikePost.objects.all()
    serializer_class = LikePostSerializer


class LikePostCreateView(generics.CreateAPIView):
    queryset = LikePost.objects.all()
    serializer_class = LikePostSerializer

    def perform_create(self, serializer):
        serializer.save(liker=self.request.user.profile)


class LikePostDeleteView(generics.DestroyAPIView):
    queryset = LikePost.objects.all()
    serializer_class = LikePostSerializer

    def perform_destroy(self, instance):
        instance = self.get_object()
        current_user = self.request.user.profile

        if instance != current_user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            self.perform_destroy(instance)
