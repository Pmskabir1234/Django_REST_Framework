from rest_framework import serializers
from .models import Comment, Blog

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__' 

class BlogSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only = True)
    # 'comments' is taken from the related names
    # this is step is required to laod all the comments 
    # related to a blog when we open the blog

    class Meta:
        model = Blog
        fields = '__all__'
