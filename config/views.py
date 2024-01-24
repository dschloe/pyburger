# -*- coding:utf-8 -*-
# 주문을 처리하는 직원
# 백엔드 영역

# from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    # return HttpResponse("안녕하세요, pyburger입니다.") # 이 코드를 HTML로 처리
    return render(request, "main.html")

#p.48
def burger_list(request):
    return render(request, "burger_list.html")