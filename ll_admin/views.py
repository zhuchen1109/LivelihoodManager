from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from models import *

# def add(request, goodsid, count):
#     cartList = CartInfo.objects.filter(id=goodsid)
#     if (len(cartList) > 0):
#         cart = cartList[0]
#         cart.ctoun = cart.ctoun + int(count)
#     else:
#         cart = CartInfo()
#         cart.goods_id = goodsid
#         cart.user_id = request.session.get('user_id')
#         cart.ctoun = count;
#     cart.save()
#     print 'ajax:',request.is_ajax()
#     return JsonResponse({'res' : cart.ctoun})
