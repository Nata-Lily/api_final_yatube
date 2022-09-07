from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, GroupSerializer
from .serializers import PostSerializer, FollowSerializer
from posts.models import Group, Post
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['user__username', 'following__username']

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
