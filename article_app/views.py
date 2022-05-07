from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


class ArticleUserWritePermission(BasePermission):
    message = 'Editing articles is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user


class ArticleList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView, ArticleUserWritePermission):
    permission_classes = [ArticleUserWritePermission]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer