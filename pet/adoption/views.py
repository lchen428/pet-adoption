from adoption.serializers import AdSerializer, OwnerSerializer
from adoption.models import Ad, Owner
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AdList(APIView):
    """
    List all adoption ads, or create a new adoption ad.
    """
    def get(self, request, format=None):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdDetail(APIView):
    """
    Retrieve, Update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Ad.objects.get(pk=pk)
        except Ad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ad = self.get_object(pk)
        serializer = AdSerializer(ad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ad = self.get_object(pk)
        serializer = AdSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ad = self.get_object(pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OwnerList(APIView):
    """
    List all adoption ads, or create a new adoption ad.
    """
    def get(self, request, format=None):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OwnerDetail(APIView):
    """
    Retrieve, Update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Owner.objects.get(pk=pk)
        except Owner.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        owner = self.get_object(pk)
        serializer = OwnerSerializer(owner)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        owner = self.get_object(pk)
        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        owner = self.get_object(pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def ownerlogin(request):
    context = {
        'request': request,
        'user': request.user
    }
    return render(request, 'adoption/ownerlogin.html', context)

def adpost(request):
    return render(request, 'adoption/adpost.html')

def adpostinfo(request):
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
    #request.data ={
    #    'name':name,
    #    'phone_number': phone_number,
    #    'email': email
    #}

    #ab = OwnerList()
    #ab.post(request)

    #owner = Owner.objects.get(name='hello')

    title = request.POST.get('title')
    description = request.POST.get('description')
    type_of_pet = request.POST.get('type_of_pet')
    birth_date = request.POST.get('birth_date')
    neutered = request.POST.get('neutered')
    gender = request.POST.get('gender')
    #owner_id = owner.id

    #request.data = {
    #    'title': title,
    #    'description': description,
    #    'type_of_pet': type_of_pet,
    #    'birth_date': birth_date,
    #    'neutered': neutered,
    #    'gender': gender,
    #    'owner_id': owner_id
    #}

    #cd = AdList()
    #cd.post(request)

    context = {
        'name': name,
        'gender': gender
    }
    return render(request, 'adoption/adpostinfo.html', context)
