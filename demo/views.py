# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views import View
from .models import Book
from .serializers import BookSerializer, BookMiniSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# class Another(View):
#     books = Book.objects.all()
#     output = ''
#     for book in books:
#         output += f"We have {book.title} that many books in DB"
#     def get(self, request):
#         return HttpResponse(self.output)


# def first(request):
#     books = Book.objects.all()
#     return render(request, 'first_temp.html', {'data': books})

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookMiniSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)

