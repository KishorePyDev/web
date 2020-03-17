from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
from bs4 import BeautifulSoup


# Create your views here.
def home(request):
    
    url = "https://www.bankbazaar.com/gold-rate-trichy.html"
    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html5lib')
    article = soup.find(class_='table table-curved tabdetails')
    for cont in article.find_all('span'):
        result = cont.text
        res = str(result)
        #print(res)
    article1 = soup.find(class_='bigfont')
    txt = str(article1.text)
    print(txt)
    print(res)
   
    return render(request,'index.html',{'price':txt,'gold':res})
