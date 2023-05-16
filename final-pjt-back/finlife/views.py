from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Max

import requests

from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

API_KEY = settings.API_KEY

# Create your views here.
@api_view(['GET'])
def deposit_products(request):
    URL = f'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(URL).json()
    base = response.get('result')['baseList']
    options = response.get('result')['optionList']
    
    DepositProducts.objects.all().delete()
    for b in base:
        deposit = DepositProducts()
        deposit.dcls_month = b.get('dcls_month')
        deposit.fin_prdt_cd = b.get('fin_prdt_cd')
        deposit.kor_co_nm = b.get('kor_co_nm')
        deposit.fin_prdt_nm = b.get('fin_prdt_nm')
        deposit.etc_note = b.get('etc_note')
        deposit.join_deny = b.get('join_deny')
        deposit.join_member = b.get('join_member')
        deposit.join_way = b.get('join_way')
        deposit.spcl_cnd = b.get('spcl_cnd')
        
        deposit.save()
        
    for o in options:
        fin_prdt_cd = DepositProducts.objects.get(fin_prdt_cd=o.get('fin_prdt_cd'))
        option = DepositOptions()
        option.fin_prdt_cd = fin_prdt_cd
        option.intr_rate_type_nm = o.get('intr_rate_type_nm')
        option.intr_rate = o.get('intr_rate')
        option.intr_rate2 = o.get('intr_rate2')
        option.save_trm = o.get('save_trm')
        
        option.save()
    
    # return Response({'message': 'Okay'})
    
# @api_view(['GET', 'POST'])
# def deposit_products(request):
    if request.method == 'GET':
        deposits = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposits, many=True)
        return Response(serializer.data)
    
    # elif request.method == 'POST':
    #     serializer = DepositProductsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response({ "message" : "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def deposit_product_options(request, fin_prdt_cd):
#     deposit_product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
#     serializer = DepositOptionsSerializer(deposit_product.options.all(), many=True)
#     return Response(serializer.data)
    

# @api_view(['GET'])
# def top_rate(request):
#     max_intr_rate2 = DepositOptions.objects.aggregate(Max('intr_rate2'))['intr_rate2__max']
#     top_deposit_product = DepositOptions.objects.filter(intr_rate2=max_intr_rate2).first().fin_prdt_cd
#     deposit_product_serializer = DepositProductsSerializer(top_deposit_product)
#     deposit_options_serializer = DepositOptionsSerializer(DepositOptions.objects.filter(fin_prdt_cd=top_deposit_product), many=True)
#     return Response({'product': deposit_product_serializer.data, 'options': deposit_options_serializer.data})