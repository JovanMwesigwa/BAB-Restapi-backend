from rest_framework import serializers
from .models import Post, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        lookup_field = 'id'
        fields = ['id', 'name', 'color', 'slug']
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    # post = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'body', 'author', 'date_commented']
        # depth = 2
        # fields = ('id', 'author')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'author', 'category', 'title', 'description', 'image', 'price', 'offer', 'price', 'available',
                  'comments']
        depth = 2
