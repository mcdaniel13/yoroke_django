import mixins as mixins
import serializers as serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from app.models import Post


def test_page(request):
    posts = Post.objects.all()
    return HttpResponse(posts[0].title + posts[0].content)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'date')


class test_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


def post_list(request):
    template = get_template('post_list.html')
    context = {}

    return template.render(context)
