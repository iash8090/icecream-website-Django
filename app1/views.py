from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from app1.models import Contact, ICDetail
from django.contrib import messages
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ICDetailSerializer



# create your views here
def index(request):
    query_set = ICDetail.objects.all()[:9]
    # first = ICDetail.objects.filter(id__range=(6,9))
    context = {'name': None, 'dtls':query_set}
    if request.method == "GET":
        srch_iceCream = request.GET.get("search_iceCream")
        if srch_iceCream :
# __icontains -> when you want to search using even single character
            query_set = ICDetail.objects.filter(name__icontains=srch_iceCream)
            context = {'name': None, 'dtls':query_set, 'srch_iceCream':srch_iceCream}

    if request.user.is_authenticated:
        context['name'] = request.user.username

#    messages.success(request, "Welcome to Our Website!")
    return render(request, 'index.html', context)


def about(request):
#    return HttpResponse("THis is About Page from app1")
    return render(request,'about.html')



def services(request):
    query_set = ICDetail.objects.all()[9:13]
    context = {'dtls': query_set}
    return render(request,'services.html', context)


def contact(request):
    try:
        # catproducts = ICDetail.objects.values('name', 'price')
        # print(catproducts)
        # cats = {item['name'] for item in catproducts}
        # print("\n\ncats - ", cats)
        # for cat in cats:
        #     print(cat)
        #     prod= ICDetail.objects.filter(name = cat)
        #     print(prod)


        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            desc = request.POST['desc']
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, "Data Submitted Successfully!")

        return render(request,'contact.html')
    except:
        pass



def iceCreamDetails(request,slugID):
    try:
        product = ICDetail.objects.get(icecream_slug=slugID)
        if product:
            context = {'product':product}
            d=request.COOKIES.setdefault('recent_items ','')
            if product.name not in d.split('\n'):
                d=d+'\n'+product.name
                d=d.strip('\n')
            response = render(request, "iceCreamDetails.html", context)
            response.set_cookie('recent_items',d)
            return response
        else:
            return HttpResponse("ID Not found")
    except:
        pass    


def cartProduct(request):
    try:    
        return render(request, "cartProduct.html")
    except:
        pass

def checkOut(request):
    try:
        return render(request, "checkOut.html")
    except:
        pass

#  function based views for REST API

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_all_IceCreams(request, id=None):
    if request.method == 'GET':
        if id:
            dtls = ICDetail.objects.get(id=id)
            serializer = ICDetailSerializer(dtls)
            return Response({"staus":"Success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        dtls = ICDetail.objects.all()
        serializer = ICDetailSerializer(dtls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # elif request.method == 'POST' & request.user.is_staff:
    #     serializer = ICDetailSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


# Method 1 for POST Api
# Class based views for REST API
class PostView(APIView):
    permission_classes = [permissions.IsAdminUser]
    def post(self, request):
        serializer = ICDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Method 2 for POST Api

# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# # @parser_classes([MultiPartParser, FormParser])
# def post_new_IceCreams(request):
#     serializer = ICDetailSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
