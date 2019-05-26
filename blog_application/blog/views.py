# viwe는 함수의 형태로 작성하며 request를 인자로 받아서 어떤 reponse를 돌려준다.
from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    return render(request,'base.html')