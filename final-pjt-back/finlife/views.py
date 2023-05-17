from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Max

import requests

from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, ExchangeInfos
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer, ExchangeInfosSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from datetime import datetime

API_KEY = settings.API_KEY
EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY

# Create your views here.
@api_view(['GET'])
def deposit_products(request):  # 정기예금 데이터 저장 및 전체 조회
    URL = f'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(URL).json()
    base = response.get('result')['baseList']
    options = response.get('result')['optionList']
    
    query = DepositProducts.objects.all()
    if not query.exists():
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
    
@api_view(['GET'])    
def saving_products(request):  # 정기적금 데이터 저장 및 전체 조회
    URL = f'https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(URL).json()
    base = response.get('result')['baseList']
    options = response.get('result')['optionList']
    
    query = SavingProducts.objects.all()
    if not query.exists():
        for b in base:
            saving = SavingProducts()
            saving.fin_prdt_cd = b.get('fin_prdt_cd')
            saving.kor_co_nm = b.get('kor_co_nm')
            saving.fin_prdt_nm = b.get('fin_prdt_nm')
            saving.etc_note = b.get('etc_note')
            saving.join_deny = b.get('join_deny')
            saving.join_member = b.get('join_member')
            saving.join_way = b.get('join_way')
            saving.spcl_cnd = b.get('spcl_cnd')
            
            saving.save()
            
        for o in options:
            fin_prdt_cd = SavingProducts.objects.get(fin_prdt_cd=o.get('fin_prdt_cd'))
            option = SavingOptions()
            option.fin_prdt_cd = fin_prdt_cd
            option.intr_rate_type_nm = o.get('intr_rate_type_nm')
            option.intr_rate = o.get('intr_rate')
            option.intr_rate2 = o.get('intr_rate2')
            option.save_trm = o.get('save_trm')
            option.rsrv_type_nm = o.get('rsrv_type_nm')
            
            option.save()
            
    savings = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(savings, many=True)
    return Response(serializer.data)

@api_view(['GET'])  # 오늘의 환율 정보 불러오기
def exchangeinfo(request):
    date_today = datetime.today().strftime('%Y%m%d')
    URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={EXCHANGE_API_KEY}&searchdate={date_today}&data=AP01'
    response = requests.get(URL).json()
    
    ExchangeInfos.objects.all().delete()
    
    for data in response:
        exchangeinfo = ExchangeInfos()
        exchangeinfo.cur_unit = data.get('cur_unit')
        exchangeinfo.cur_nm = data.get('cur_nm')
        exchangeinfo.exchange = data.get('deal_bas_r')
        exchangeinfo.bkpr = data.get('bkpr')
        
        exchangeinfo.save()
        
    exchangeinfos = ExchangeInfos.objects.all()
    serializer = ExchangeInfosSerializer(exchangeinfos, many=True)
    return Response(serializer.data)