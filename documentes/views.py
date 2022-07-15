from django.shortcuts import render
from .models import Documentes
# Create your views here.
from .readerFunc import getDocInfo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .serializers import ImageSerializer
# Create your views here.



@api_view(['POST'])
def CheckIm(request):
    image = Documentes(fileName=request.data['name'], number="6947586943", barcode="5869473859672", codeType="EAN13", image=request.data['photo'])
    image.save()
    print(image.image)
    dict = getDocInfo(image.image)
    number, barcode, codeType = dict['number'], dict['barcode'], dict['codeType']
    image.number = number
    image.barcode = barcode
    image.codeType = codeType

    image.save()

    return Response({'number': number, 'barcode': barcode, 'type': codeType})


@api_view(['GET'])
def GetIm(request):
    docs = Documentes.objects.all()
    num = []
    bar = []
    type = []
    names = []
    for i in docs:
        num.append(i.number)
        bar.append(i.barcode)
        type.append(i.codeType)
        names.append(str(i.image))
        print(i.image)
    return Response({'number': num, 'barcode': bar, 'type': type, 'path': names})