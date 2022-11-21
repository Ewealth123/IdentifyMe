from django.shortcuts import redirect, render,  get_object_or_404
from django.conf import settings
from django.http.request import  HttpRequest
from django.http.response import HttpResponse
from django.contrib import messages
from account.models import agent
from .models import Payment
import requests
import json
import os
import PIL.Image as Image
from io import BytesIO
import io
import base64
from . import forms
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.models import User


# Create your views here.
def index_nin(request):
    return render(request, 'index_nin.html')

def v_by_ninw(request):
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    oo = int(nn)
    
    

    
    
    if oo < 200:
        messages.info(request,"Insufficient balance", extra_tags='ans')
        
    else:
        
        if request.method == 'POST':
            me=request.POST["nin_number"]
            # url = "https://api.verified.africa/sfx-verify/v3/id-service/"

            # payload = {
            #     "searchParameter": me,
            #     "verificationType": "NIN-SEARCH"
            # }
            # headers = {
            #     "accept": "application/json",
            #     "userid": "1647784769854",
            #     "apiKey": "OiJ8EYBw98vaDWClMZLO",
            #     "content-type": "application/json"
            # }

            # res = requests.post(url, json=payload, headers=headers).json()
            # ress = res['response']
            # vs = res['verificationStatus']
            # print(vs)
            urll = "https://ad1x.idcheck.ng/api/triangle/token/create"
            payload={
                    'username': 'igbonekwuifeanyi18@gmail.com',
                    'password' : 'Igbonekwu1#'
                    
            }
            files=[

            ]
            

            response = requests.request("POST", urll,  data=payload, files=files).json()
            
            ggt = response['access_token']
            
            url = "https://ad1x.idcheck.ng/api/triangle/nin/verify"
            payload={'nin': '20731396857',
                    'searchType': 'nin',
                    'data' : me
                    
            }
            files=[

            ]
            headers = {
            'Authorization': ggt
            }
            res = requests.request("POST", url, headers=headers,  data=payload, files=files).json()
            print(res)
            resss =res['data']
            ress=resss['data']
            print(ress)
            sin=ress['signature']
            vs = res['status']
            #vss =res['message']
            # vsss = res['message']
            # vr = vsss['0']
            #print(vsss)
            print(vs)
            # if vsss == "0":
            #     messages.info(request,"Nin must be 11 digits", extra_tags='ans')
            # else:
            if vs == "False":
                messages.info(request,"No Record Found", extra_tags='ans')
                # math = int(nn) 
                # i = int(100)
                # done  =  math - i
                # print(done)
                # agent.objects.filter(email = user.username).update(wallet_bal = done)
                # rr = agent.objects.filter(email= user.username).values("wallet_bal")
                # ss=rr[0]['wallet_bal']
            # else:
            #     if vs == "FAILED":
            #         messages.info(request,"Third Party System is Unavailable", extra_tags='ans')
            else:
                if sin == '***':
                    math = int(nn) 
                    i = int(200)
                    done  =  math - i
                    print(done)
                    agent.objects.filter(email = user.username).update(wallet_bal = done)
                    rr = agent.objects.filter(email= user.username).values("wallet_bal")
                    ss=rr[0]['wallet_bal']
                    
                    nin_Surname =ress['surname']
                    nin_firstname =ress['firstname']
                    nin_middlename =ress['middlename']
                    nin_gender =ress['gender']
                    nin_dateofbirth =ress['birthdate']
                    nin_nin =ress['nin']
                    nin_phonenumber =ress['telephoneno']
                    #nin_email =ress[0]['heigth']
                    nin_trackingid =ress['trackingId']
                    nin_town =ress['residence_Town']
                    nin_address =ress['residence_AdressLine1']
                    nin_residencelga =ress['residence_lga']
                    nin_residencestate =ress['residence_state']
                    
                    
                    request.session['nin_Surname'] = nin_Surname
                    request.session['nin_firstname'] = nin_firstname
                    request.session['nin_middlename'] = nin_middlename
                    request.session['nin_gender'] = nin_gender
                    request.session['nin_nin'] = nin_nin
                    request.session['nin_trackingid'] = nin_trackingid
                    request.session['nin_address'] = nin_address
                    request.session['nin_town'] = nin_town
                    request.session['nin_residencelga'] = nin_residencelga
                    
                    # nin_stateoforigin =ress[0]['self_origin_state']
                    # nin_noksurname =ress[0]['nok_surname']
                    # nin_nokfirstname =ress[0]['nok_firstname']
                    # nin_nokmiddlename =ress[0]['nok_middlename']
                    # nin_noktown =ress[0]['nok_town']
                    # nin_nokstate =ress[0]['nok_state']
                    # nin_country =ress[0]['birthcountry']
                    # nin_title =ress[0]['title']
                    
                    # request.session['nin_Surname'] = nin_Surname
                    # request.session['nin_firstname'] = nin_firstname
                    # request.session['nin_middlename'] = nin_middlename
                    # request.session['nin_gender'] = nin_gender
                    # request.session['nin_nin'] = nin_nin
                    # request.session['nin_trackingid'] = nin_trackingid
                    # request.session['nin_address'] = nin_address
                    # request.session['nin_town'] = nin_town
                    # request.session['nin_residencelga'] = nin_residencelga
                    
                    messages.info(request,nin_Surname,extra_tags='m1')
                    messages.info(request,nin_firstname,extra_tags='m2')
                    messages.info(request,nin_middlename,extra_tags='m3')
                    messages.info(request,nin_gender,extra_tags='m4')
                    messages.info(request,nin_dateofbirth,extra_tags='m5')
                    messages.info(request,nin_nin,extra_tags='m6')
                    messages.info(request,nin_phonenumber,extra_tags='m7')
                    #messages.info(request,nin_email,extra_tags='m8')
                    messages.info(request,nin_trackingid,extra_tags='m8')
                    messages.info(request,nin_town,extra_tags='m9')
                    messages.info(request,nin_address,extra_tags='m10')
                    messages.info(request,nin_residencelga,extra_tags='m11')
                    messages.info(request,nin_residencestate,extra_tags='m12')
                    # messages.info(request,nin_stateoforigin,extra_tags='m14')
                    # messages.info(request,nin_noksurname,extra_tags='m15')
                    # messages.info(request,nin_nokfirstname,extra_tags='m16')
                    # messages.info(request,nin_nokmiddlename,extra_tags='m17')
                    # messages.info(request,nin_noktown,extra_tags='m18')
                    # messages.info(request,nin_nokstate,extra_tags='m19')
                    # messages.info(request,nin_country,extra_tags='m20')
                    # messages.info(request,nin_title,extra_tags='m21')
                    
                    #image 
                    photo = ress['photo']
                    byte_data =f"'{photo}'"
                    b= base64.b64decode(byte_data)
                    data = io.BytesIO(b)
                    data.seek(0)
                    pp = Image.open(data)
                    pp.save(data, "PNG")
                    end = base64.b64encode(data.getvalue())
                    img  = end.decode('utf-8')
                    request.session['img'] = img
                    return render(request,'v_by_ninw.html',{"img_data":img,"wallet":ss})
                else:
                    math = int(nn) 
                    i = int(200)
                    done  =  math - i
                    print(done)
                    agent.objects.filter(email = user.username).update(wallet_bal = done)
                    rr = agent.objects.filter(email= user.username).values("wallet_bal")
                    ss=rr[0]['wallet_bal']
                    
                    nin_Surname =ress['surname']
                    nin_firstname =ress['firstname']
                    nin_middlename =ress['middlename']
                    nin_gender =ress['gender']
                    nin_dateofbirth =ress['birthdate']
                    nin_nin =ress['nin']
                    nin_phonenumber =ress['telephoneno']
                    #nin_email =ress[0]['heigth']
                    nin_trackingid =ress['trackingId']
                    nin_town =ress['residence_Town']
                    nin_address =ress['residence_AdressLine1']
                    nin_residencelga =ress['residence_lga']
                    nin_residencestate =ress['residence_state']
                    
                    
                    request.session['nin_Surname'] = nin_Surname
                    request.session['nin_firstname'] = nin_firstname
                    request.session['nin_middlename'] = nin_middlename
                    request.session['nin_gender'] = nin_gender
                    request.session['nin_nin'] = nin_nin
                    request.session['nin_trackingid'] = nin_trackingid
                    request.session['nin_address'] = nin_address
                    request.session['nin_town'] = nin_town
                    request.session['nin_residencelga'] = nin_residencelga
                    
                    # nin_stateoforigin =ress[0]['self_origin_state']
                    # nin_noksurname =ress[0]['nok_surname']
                    # nin_nokfirstname =ress[0]['nok_firstname']
                    # nin_nokmiddlename =ress[0]['nok_middlename']
                    # nin_noktown =ress[0]['nok_town']
                    # nin_nokstate =ress[0]['nok_state']
                    # nin_country =ress[0]['birthcountry']
                    # nin_title =ress[0]['title']
                    
                    # request.session['nin_Surname'] = nin_Surname
                    # request.session['nin_firstname'] = nin_firstname
                    # request.session['nin_middlename'] = nin_middlename
                    # request.session['nin_gender'] = nin_gender
                    # request.session['nin_nin'] = nin_nin
                    # request.session['nin_trackingid'] = nin_trackingid
                    # request.session['nin_address'] = nin_address
                    # request.session['nin_town'] = nin_town
                    # request.session['nin_residencelga'] = nin_residencelga
                    
                    messages.info(request,nin_Surname,extra_tags='m1')
                    messages.info(request,nin_firstname,extra_tags='m2')
                    messages.info(request,nin_middlename,extra_tags='m3')
                    messages.info(request,nin_gender,extra_tags='m4')
                    messages.info(request,nin_dateofbirth,extra_tags='m5')
                    messages.info(request,nin_nin,extra_tags='m6')
                    messages.info(request,nin_phonenumber,extra_tags='m7')
                    #messages.info(request,nin_email,extra_tags='m8')
                    messages.info(request,nin_trackingid,extra_tags='m8')
                    messages.info(request,nin_town,extra_tags='m9')
                    messages.info(request,nin_address,extra_tags='m10')
                    messages.info(request,nin_residencelga,extra_tags='m11')
                    messages.info(request,nin_residencestate,extra_tags='m12')
                    # messages.info(request,nin_stateoforigin,extra_tags='m14')
                    # messages.info(request,nin_noksurname,extra_tags='m15')
                    # messages.info(request,nin_nokfirstname,extra_tags='m16')
                    # messages.info(request,nin_nokmiddlename,extra_tags='m17')
                    # messages.info(request,nin_noktown,extra_tags='m18')
                    # messages.info(request,nin_nokstate,extra_tags='m19')
                    # messages.info(request,nin_country,extra_tags='m20')
                    # messages.info(request,nin_title,extra_tags='m21')
                    
                    #image 
                    photo = ress['photo']
                    byte_data =f"'{photo}'"
                    b= base64.b64decode(byte_data)
                    data = io.BytesIO(b)
                    data.seek(0)
                    pp = Image.open(data)
                    pp.save(data, "PNG")
                    end = base64.b64encode(data.getvalue())
                    img  = end.decode('utf-8')
                    request.session['img'] = img
                    #sig  
                    photo1 = ress['signature']
                    byte_data1 =f"'{photo1}'"
                    b1= base64.b64decode(byte_data1)
                    data1 = io.BytesIO(b1)
                    data1.seek(0)
                    pp1 = Image.open(data1)
                    pp1.save(data1, "PNG")
                    end1 = base64.b64encode(data1.getvalue())
                    img1  = end1.decode('utf-8')
                
                
                
                    return render(request,'v_by_ninw.html',{"img_data":img,"img_data1":img1,"wallet":ss})
        
        
    return render(request, 'v_by_ninw.html',{"wallet":nn})

def v_by_phone(request):
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    oo = int(nn)
    if oo < 200:
        messages.info(request,"Insufficient balance", extra_tags='ans')
        
    else:
        if request.method == 'POST':
            me=request.POST["nin_phone"]
            # url = "https://api.verified.africa/sfx-verify/v3/id-service/"

            # payload = {
            #     "searchParameter": me,
            #     "verificationType": "NIN-PHONE-SEARCH"
            # }
            # headers = {
            #     "accept": "application/json",
            #     "userid": "1647784769854",
            #     "apiKey": "fv6LUVnQGNcp4eEPdK5A",
            #     "content-type": "application/json"
            # }

            # res = requests.post(url, json=payload, headers=headers).json()
            # ress = res['response']
            # vs = res['verificationStatus']
            # print(vs)
            
            urll = "https://ad1x.idcheck.ng/api/triangle/token/create"
            payload={
                    'username': 'igbonekwuifeanyi18@gmail.com',
                    'password' : 'Igbonekwu1#'
                    
            }
            files=[

            ]
            

            response = requests.request("POST", urll,  data=payload, files=files).json()
            
            ggt = response['access_token']
            
            url = "https://ad1x.idcheck.ng/api/triangle/nin/verify"
            payload={'nin': '20731396857',
                    'searchType': 'phone',
                    'data' : me
                    
            }
            files=[

            ]
            headers = {
            'Authorization': ggt
            }
            res = requests.request("POST", url, headers=headers,  data=payload, files=files).json()
            print(res)
            resss =res['data']
            ress=resss['data']
            sin=ress['signature']
            print(ress)
            vs = res['status']
            #vss =res['message']
            # vsss = res['message']
            # vr = vsss['0']
            #print(vsss)
            print(vs)
            
            if vs == "False":
                messages.info(request,"No Record Found", extra_tags='ans')
                # math = int(nn) 
                # i = int(100)
                # done  =  math - i
                # print(done)
                # agent.objects.filter(email = user.username).update(wallet_bal = done)
                # rr = agent.objects.filter(email= user.username).values("wallet_bal")
                # ss=rr[0]['wallet_bal']
            # else:
            #     if vs == "FAILED":
            #         messages.info(request,"Third Party System is Unavailable", extra_tags='ans')
            else:
                if sin == '***':
                    math = int(nn) 
                    i = int(200)
                    done  =  math - i
                    print(done)
                    agent.objects.filter(email = user.username).update(wallet_bal = done)
                    rr = agent.objects.filter(email= user.username).values("wallet_bal")
                    ss=rr[0]['wallet_bal']
                    
                    nin_Surname =ress['surname']
                    nin_firstname =ress['firstname']
                    nin_middlename =ress['middlename']
                    nin_gender =ress['gender']
                    nin_dateofbirth =ress['birthdate']
                    nin_nin =ress['nin']
                    nin_phonenumber =ress['telephoneno']
                    #nin_email =ress[0]['heigth']
                    nin_trackingid =ress['trackingId']
                    nin_town =ress['residence_Town']
                    nin_address =ress['residence_AdressLine1']
                    nin_residencelga =ress['residence_lga']
                    nin_residencestate =ress['residence_state']
                    
                    
                    request.session['nin_Surname'] = nin_Surname
                    request.session['nin_firstname'] = nin_firstname
                    request.session['nin_middlename'] = nin_middlename
                    request.session['nin_gender'] = nin_gender
                    request.session['nin_nin'] = nin_nin
                    request.session['nin_trackingid'] = nin_trackingid
                    request.session['nin_address'] = nin_address
                    request.session['nin_town'] = nin_town
                    request.session['nin_residencelga'] = nin_residencelga
                    
                    # nin_stateoforigin =ress[0]['self_origin_state']
                    # nin_noksurname =ress[0]['nok_surname']
                    # nin_nokfirstname =ress[0]['nok_firstname']
                    # nin_nokmiddlename =ress[0]['nok_middlename']
                    # nin_noktown =ress[0]['nok_town']
                    # nin_nokstate =ress[0]['nok_state']
                    # nin_country =ress[0]['birthcountry']
                    # nin_title =ress[0]['title']
                    
                    # request.session['nin_Surname'] = nin_Surname
                    # request.session['nin_firstname'] = nin_firstname
                    # request.session['nin_middlename'] = nin_middlename
                    # request.session['nin_gender'] = nin_gender
                    # request.session['nin_nin'] = nin_nin
                    # request.session['nin_trackingid'] = nin_trackingid
                    # request.session['nin_address'] = nin_address
                    # request.session['nin_town'] = nin_town
                    # request.session['nin_residencelga'] = nin_residencelga
                    
                    messages.info(request,nin_Surname,extra_tags='m1')
                    messages.info(request,nin_firstname,extra_tags='m2')
                    messages.info(request,nin_middlename,extra_tags='m3')
                    messages.info(request,nin_gender,extra_tags='m4')
                    messages.info(request,nin_dateofbirth,extra_tags='m5')
                    messages.info(request,nin_nin,extra_tags='m6')
                    messages.info(request,nin_phonenumber,extra_tags='m7')
                    #messages.info(request,nin_email,extra_tags='m8')
                    messages.info(request,nin_trackingid,extra_tags='m8')
                    messages.info(request,nin_town,extra_tags='m9')
                    messages.info(request,nin_address,extra_tags='m10')
                    messages.info(request,nin_residencelga,extra_tags='m11')
                    messages.info(request,nin_residencestate,extra_tags='m12')
                    # messages.info(request,nin_stateoforigin,extra_tags='m14')
                    # messages.info(request,nin_noksurname,extra_tags='m15')
                    # messages.info(request,nin_nokfirstname,extra_tags='m16')
                    # messages.info(request,nin_nokmiddlename,extra_tags='m17')
                    # messages.info(request,nin_noktown,extra_tags='m18')
                    # messages.info(request,nin_nokstate,extra_tags='m19')
                    # messages.info(request,nin_country,extra_tags='m20')
                    # messages.info(request,nin_title,extra_tags='m21')
                    
                    #image 
                    photo = ress['photo']
                    byte_data =f"'{photo}'"
                    b= base64.b64decode(byte_data)
                    data = io.BytesIO(b)
                    data.seek(0)
                    pp = Image.open(data)
                    pp.save(data, "PNG")
                    end = base64.b64encode(data.getvalue())
                    img  = end.decode('utf-8')
                    request.session['img'] = img
                    return render(request,'v_by_phone.html',{"img_data":img,"wallet":ss})
                else:
                    math = int(nn) 
                    i = int(200)
                    done  =  math - i
                    print(done)
                    agent.objects.filter(email = user.username).update(wallet_bal = done)
                    rr = agent.objects.filter(email= user.username).values("wallet_bal")
                    ss=rr[0]['wallet_bal']
                    
                    nin_Surname =ress['surname']
                    nin_firstname =ress['firstname']
                    nin_middlename =ress['middlename']
                    nin_gender =ress['gender']
                    nin_dateofbirth =ress['birthdate']
                    nin_nin =ress['nin']
                    nin_phonenumber =ress['telephoneno']
                    #nin_email =ress[0]['heigth']
                    nin_trackingid =ress['trackingId']
                    nin_town =ress['residence_Town']
                    nin_address =ress['residence_AdressLine1']
                    nin_residencelga =ress['residence_lga']
                    nin_residencestate =ress['residence_state']
                    
                    
                    request.session['nin_Surname'] = nin_Surname
                    request.session['nin_firstname'] = nin_firstname
                    request.session['nin_middlename'] = nin_middlename
                    request.session['nin_gender'] = nin_gender
                    request.session['nin_nin'] = nin_nin
                    request.session['nin_trackingid'] = nin_trackingid
                    request.session['nin_address'] = nin_address
                    request.session['nin_town'] = nin_town
                    request.session['nin_residencelga'] = nin_residencelga
                    
                    # nin_stateoforigin =ress[0]['self_origin_state']
                    # nin_noksurname =ress[0]['nok_surname']
                    # nin_nokfirstname =ress[0]['nok_firstname']
                    # nin_nokmiddlename =ress[0]['nok_middlename']
                    # nin_noktown =ress[0]['nok_town']
                    # nin_nokstate =ress[0]['nok_state']
                    # nin_country =ress[0]['birthcountry']
                    # nin_title =ress[0]['title']
                    
                    # request.session['nin_Surname'] = nin_Surname
                    # request.session['nin_firstname'] = nin_firstname
                    # request.session['nin_middlename'] = nin_middlename
                    # request.session['nin_gender'] = nin_gender
                    # request.session['nin_nin'] = nin_nin
                    # request.session['nin_trackingid'] = nin_trackingid
                    # request.session['nin_address'] = nin_address
                    # request.session['nin_town'] = nin_town
                    # request.session['nin_residencelga'] = nin_residencelga
                    
                    messages.info(request,nin_Surname,extra_tags='m1')
                    messages.info(request,nin_firstname,extra_tags='m2')
                    messages.info(request,nin_middlename,extra_tags='m3')
                    messages.info(request,nin_gender,extra_tags='m4')
                    messages.info(request,nin_dateofbirth,extra_tags='m5')
                    messages.info(request,nin_nin,extra_tags='m6')
                    messages.info(request,nin_phonenumber,extra_tags='m7')
                    #messages.info(request,nin_email,extra_tags='m8')
                    messages.info(request,nin_trackingid,extra_tags='m8')
                    messages.info(request,nin_town,extra_tags='m9')
                    messages.info(request,nin_address,extra_tags='m10')
                    messages.info(request,nin_residencelga,extra_tags='m11')
                    messages.info(request,nin_residencestate,extra_tags='m12')
                    # messages.info(request,nin_stateoforigin,extra_tags='m14')
                    # messages.info(request,nin_noksurname,extra_tags='m15')
                    # messages.info(request,nin_nokfirstname,extra_tags='m16')
                    # messages.info(request,nin_nokmiddlename,extra_tags='m17')
                    # messages.info(request,nin_noktown,extra_tags='m18')
                    # messages.info(request,nin_nokstate,extra_tags='m19')
                    # messages.info(request,nin_country,extra_tags='m20')
                    # messages.info(request,nin_title,extra_tags='m21')
                    
                    #image 
                    photo = ress['photo']
                    byte_data =f"'{photo}'"
                    b= base64.b64decode(byte_data)
                    data = io.BytesIO(b)
                    data.seek(0)
                    pp = Image.open(data)
                    pp.save(data, "PNG")
                    end = base64.b64encode(data.getvalue())
                    img  = end.decode('utf-8')
                    request.session['img'] = img
                    #sig  
                    photo1 = ress['signature']
                    byte_data1 =f"'{photo1}'"
                    b1= base64.b64decode(byte_data1)
                    data1 = io.BytesIO(b1)
                    data1.seek(0)
                    pp1 = Image.open(data1)
                    pp1.save(data1, "PNG")
                    end1 = base64.b64encode(data1.getvalue())
                    img1  = end1.decode('utf-8')
                
                
                
                    return render(request,'v_by_phone.html',{"img_data":img,"img_data1":img1,"wallet":ss})
            
    return render(request, 'v_by_phone.html',{"wallet":nn})

def v_by_vnin(request):
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    oo = int(nn)
    if oo < 150:
        messages.info(request,"Insufficient balance", extra_tags='ans')
        
    else:
        
        if request.method == 'POST':
            me=request.POST["nin_number"]
            url = "https://api.verified.africa/sfx-verify/v3/id-service/"

            payload = {
                "searchParameter": me,
                "verificationType": "V-NIN",
                "countryCode": "NG",
            }
            headers = {
                "accept": "application/json",
                "userid": "1647784769854",
                "apiKey": "YWlmjzRG333c2pjap6Xr",
                "content-type": "application/json"
            }

            res = requests.post(url, json=payload, headers=headers).json()
            ress = res['response']
            vs = res['verificationStatus']
            print(vs)
            
            if vs == "PENDING":
                messages.info(request,"Something unexpected happened", extra_tags='ans')
            else:
                if vs == "NOT VERIFIED":
                    messages.info(request,"No Record Found", extra_tags='ans')
                    math = int(nn) 
                    i = int(100)
                    done  =  math - i
                    print(done)
                    agent.objects.filter(email = user.username).update(wallet_bal = done)
                    rr = agent.objects.filter(email= user.username).values("wallet_bal")
                    ss=rr[0]['wallet_bal']
                else:
                    if vs == "FAILED":
                        messages.info(request,"Third Party System is Unavailable", extra_tags='ans')
                    else:
                        math = int(nn) 
                        i = int(150)
                        done  =  math - i
                        print(done)
                        agent.objects.filter(email = user.username).update(wallet_bal = done)
                        rr = agent.objects.filter(email= user.username).values("wallet_bal")
                        ss=rr[0]['wallet_bal']
                        
                        nin_Surname =ress[0]['surname']
                        nin_firstname =ress[0]['firstname']
                        nin_middlename =ress[0]['middlename']
                        nin_gender =ress[0]['gender']
                        nin_dateofbirth =ress[0]['dateOfBirth']
                        nin_nin =ress[0]['vnin']
                        nin_phonenumber =ress[0]['trustedNumber']
                        nin_agentid =ress[0]['agentID']
                        nin_userid =ress[0]['userid']
                        # nin_town =ress[0]['residence_Town']
                        # nin_address =ress[0]['residence_AdressLine1']
                        # nin_residencelga =ress[0]['residence_lga']
                        # nin_residencestate =ress[0]['residence_state']
                        # nin_stateoforigin =ress[0]['self_origin_state']
                        # nin_noksurname =ress[0]['nok_surname']
                        # nin_nokfirstname =ress[0]['nok_firstname']
                        # nin_nokmiddlename =ress[0]['nok_middlename']
                        # nin_noktown =ress[0]['nok_town']
                        # nin_nokstate =ress[0]['nok_state']
                        # nin_country =ress[0]['birthcountry']
                        # nin_title =ress[0]['title']
                        
                        messages.info(request,nin_Surname,extra_tags='m1')
                        messages.info(request,nin_firstname,extra_tags='m2')
                        messages.info(request,nin_middlename,extra_tags='m3')
                        messages.info(request,nin_gender,extra_tags='m4')
                        messages.info(request,nin_dateofbirth,extra_tags='m5')
                        messages.info(request,nin_nin,extra_tags='m6')
                        messages.info(request,nin_phonenumber,extra_tags='m7')
                        messages.info(request,nin_agentid,extra_tags='m8')
                        messages.info(request,nin_userid,extra_tags='m9')
                        # messages.info(request,nin_town,extra_tags='m10')
                        # messages.info(request,nin_address,extra_tags='m11')
                        # messages.info(request,nin_residencelga,extra_tags='m12')
                        # messages.info(request,nin_residencestate,extra_tags='m13')
                        # messages.info(request,nin_stateoforigin,extra_tags='m14')
                        # messages.info(request,nin_noksurname,extra_tags='m15')
                        # messages.info(request,nin_nokfirstname,extra_tags='m16')
                        # messages.info(request,nin_nokmiddlename,extra_tags='m17')
                        # messages.info(request,nin_noktown,extra_tags='m18')
                        # messages.info(request,nin_nokstate,extra_tags='m19')
                        # messages.info(request,nin_country,extra_tags='m20')
                        # messages.info(request,nin_title,extra_tags='m21')
                        
                        # #image 
                        photo = ress[0]['photo']
                        byte_data =f"'{photo}'"
                        b= base64.b64decode(byte_data)
                        data = io.BytesIO(b)
                        data.seek(0)
                        pp = Image.open(data)
                        pp.save(data, "PNG")
                        end = base64.b64encode(data.getvalue())
                        img  = end.decode('utf-8')
                        
                        # #sig  
                        # photo1 = ress[0]['signature']
                        # byte_data1 =f"'{photo1}'"
                        # b1= base64.b64decode(byte_data1)
                        # data1 = io.BytesIO(b1)
                        # data1.seek(0)
                        # pp1 = Image.open(data1)
                        # pp1.save(data1, "PNG") 
                        # end1 = base64.b64encode(data1.getvalue())
                        # img1  = end1.decode('utf-8')
                        return render(request,'v_by_ninw.html',{"wallet":ss, "img_data":img})#,"img_data1":img1,
                    
    return render(request, 'v_by_vnin.html',{"wallet":nn})

def wallet(request: HttpRequest) -> HttpResponse:
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            pay = payment_form.save()
            return render(request,'make_payment.html',{'payment': pay, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})  
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'wallet.html', { 'user':user, 'wallet': nn,'payment_form': payment_form})


def voters(request):
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    oo = int(nn)
    
    if oo < 300:
        messages.info(request,"Insufficient balance", extra_tags='ans')
        
    else:
        
        if request.method == 'POST':
            me=request.POST["voter_number"]
            url = "https://api.verified.africa/sfx-verify/v3/id-service/"

            payload = {
                "searchParameter": me,
                "countryCode" : "NG",
                "verificationType": "VIN-FULL-DETAILS-VERIFICATION"
            }
            headers = {
                "accept": "application/json",
                "userid": "1647784769854",
                "apiKey": "QMvXdF4ckwLQ2DQkg6OV",
                "content-type": "application/json"
            }

            res = requests.post(url, json=payload, headers=headers).json()
            ress = res['response']
            vs = res['verificationStatus']
            print(ress)
            print(res)
            print(vs)
            if vs == "PENDING":
                messages.info(request,"Something unexpected happened", extra_tags='ans')
            else:
                if vs == "NOT VERIFIED":
                    messages.info(request,"No Record Found", extra_tags='ans')
                    math = int(nn) 
                    i = int(200)
                    done  =  math - i
                    print(done)
                    agent.objects.filter(email = user.username).update(wallet_bal = done)
                    rr = agent.objects.filter(email= user.username).values("wallet_bal")
                    ss=rr[0]['wallet_bal']
                else:
                    if vs == "FAILED":
                        messages.info(request,"Third Party System is Unavailable", extra_tags='ans')
                    else:
                        math = int(nn) 
                        i = int(300)
                        done  =  math - i
                        print(done)
                        agent.objects.filter(email = user.username).update(wallet_bal = done)
                        rr = agent.objects.filter(email= user.username).values("wallet_bal")
                        ss=rr[0]['wallet_bal']
                        lastname =ress[0]['last_name']
                        firstname =ress[0]['first_name']
                        full_name =ress[0]['full_name']
                        gender =ress[0]['gender']
                        yearofbirth =ress[0]['yob']
                        id_number =ress[0]['id_number']
                        phonenumber =ress[0]['phone_number']
                        occupation =ress[0]['occupation']
                        vin =ress[0]['vin']
                        phone_number2 =ress[0]['phone_number2']
                        address =ress[0]['address']
                        lga =ress[0]['lga']
                        state =ress[0]['state']
                        expiration_date =ress[0]['expiration_date']
                        
                        
                        messages.info(request,lastname,extra_tags='m1')
                        messages.info(request,firstname,extra_tags='m2')
                        messages.info(request,full_name,extra_tags='m3')
                        messages.info(request,gender,extra_tags='m4')
                        messages.info(request,yearofbirth,extra_tags='m5')
                        messages.info(request,id_number,extra_tags='m6')
                        messages.info(request,phonenumber,extra_tags='m7')
                        messages.info(request,occupation,extra_tags='m8')
                        messages.info(request,vin,extra_tags='m9')
                        messages.info(request,phone_number2,extra_tags='m10')
                        messages.info(request,address,extra_tags='m11')
                        messages.info(request,lga,extra_tags='m12')
                        messages.info(request,state,extra_tags='m13')
                        messages.info(request,expiration_date,extra_tags='m14')
                        
                        #image 
                        photo = ress[0]['photo']
                        photo13 = photo.replace('data:image/jpg;base64,', '')
                        byte_data =f"'{photo13}'"
                        b= base64.b64decode(byte_data)
                        data = io.BytesIO(b)
                        data.seek(0)
                        pp = Image.open(data)
                        pp.save(data, "PNG")
                        end = base64.b64encode(data.getvalue())
                        img  = end.decode('utf-8')
                        return render(request,'voters.html',{"img_data":img,"wallet":ss})
    
    return render(request, 'voters.html',{"wallet":nn})


def pdf(request):
    request.user
    #pdf
    #template_path = 'nin_form.html'
    
    
    
    context = {'surname':request.session['nin_Surname'],
                'firstname': request.session['nin_firstname'] ,
                'middlename': request.session['nin_middlename'],
                'gender': request.session['nin_gender'],
                'nin': request.session['nin_nin'],
                'tracking': request.session['nin_trackingid'],
                'address': request.session['nin_address'],
                'town': request.session['nin_town'],
                'add_lga': request.session['nin_residencelga'],
                'img':request.session['img']
                
    }
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'filename="report.pdf"'
    # # find the template and render it.
    # template = get_template(template_path)
    # html = template.render(context)
    
    # # create a pdf
    # pisa_status = pisa.CreatePDF(
    # html, dest=response)  
    
    # # if error then show some funny view
    # if pisa_status.err:
    #    return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response
    return render(request, 'nin_form.html',context)
    


def tin(request):
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    oo = int(nn)
    
    if oo < 150:
        messages.info(request,"Insufficient balance", extra_tags='ans')
        
    else:
        
        if request.method == 'POST':
            me=request.POST["tin_number"]
            url = "https://api.verified.africa/sfx-verify/v3/id-service/"

            payload = {
                "searchParameter": me,
                "verificationType": "TIN-FULL-DETAIL-VERIFICATION"
            }
            headers = {
                "accept": "application/json",
                "userid": "1647784769854",
                "apiKey": "qSGCtHP4XYF4uLgW39n7",
                "content-type": "application/json"
            }

            res = requests.post(url, json=payload, headers=headers).json()
            ress = res['response']
            vs = res['verificationStatus']
            print(ress)
            print(res)
            print(vs)
            if vs == "PENDING":
                messages.info(request,"Something unexpected happened", extra_tags='ans')
            else:
                if vs == "NOT VERIFIED":
                    messages.info(request,"No Record Found", extra_tags='ans')
                    math = int(nn) 
                    i = int(100)
                    done  =  math - i
                    print(done)
                    agent.objects.filter(email = user.username).update(wallet_bal = done)
                    rr = agent.objects.filter(email= user.username).values("wallet_bal")
                    ss=rr[0]['wallet_bal']
                else:
                    if vs == "FAILED":
                        messages.info(request,"Third Party System is Unavailable", extra_tags='ans')
                    else:
                        math = int(nn) 
                        i = int(150)
                        done  =  math - i
                        print(done)
                        agent.objects.filter(email = user.username).update(wallet_bal = done)
                        rr = agent.objects.filter(email= user.username).values("wallet_bal")
                        ss=rr[0]['wallet_bal']
                        
                        fullname =ress[0]['full_name']
                        typeofentity =ress[0]['typeofentity']
                        email =ress[0]['email']
                        gender =ress[0]['gender']
                        yearofbirth =ress[0]['dob']
                        id_number =ress[0]['id_number']
                        phonenumber =ress[0]['phone_number']
                        taxoffice =ress[0]['tax_office']
                        cac =ress[0]['cac_reg_no']
                        phone_number2 =ress[0]['phone_number2']
                        address =ress[0]['address']
                        taxpayername =ress[0]['tax_payer_name']
                        type_of_entity =ress[0]['type_of_entity']
                        expiration_date =ress[0]['expiration_date']
                        
                        
                        messages.info(request,fullname,extra_tags='m1')
                        messages.info(request,typeofentity,extra_tags='m2')
                        messages.info(request,email,extra_tags='m3')
                        messages.info(request,gender,extra_tags='m4')
                        messages.info(request,yearofbirth,extra_tags='m5')
                        messages.info(request,id_number,extra_tags='m6')
                        messages.info(request,phonenumber,extra_tags='m7')
                        messages.info(request,taxoffice,extra_tags='m8')
                        messages.info(request,cac,extra_tags='m9')
                        messages.info(request,phone_number2,extra_tags='m10')
                        messages.info(request,address,extra_tags='m11')
                        messages.info(request,taxpayername,extra_tags='m12')
                        messages.info(request,type_of_entity,extra_tags='m13')
                        messages.info(request,expiration_date,extra_tags='m14')
                        
                        #image 
                        photo = ress[0]['photo']
                        photo13 = photo.replace('data:image/jpg;base64,', '')
                        byte_data =f"'{photo13}'"
                        b= base64.b64decode(byte_data)
                        data = io.BytesIO(b)
                        data.seek(0)
                        pp = Image.open(data)
                        pp.save(data, "PNG")
                        end = base64.b64encode(data.getvalue())
                        img  = end.decode('utf-8')
                        return render(request,'tin.html',{"img_data":img,"wallet":ss})
    return render(request,'tin.html',{"wallet":nn})



def cac(request):
    return render(request,'cac.html')#,{"wallet":nn})


def bvn(request):
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    oo = int(nn)
    
    if oo < 150:
        messages.info(request,"Insufficient balance", extra_tags='ans')
        
    else:
        
        if request.method == 'POST':
            me=request.POST["bvn_number"]
            url = "https://api.verified.africa/sfx-verify/v3/id-service/"

            payload = {
                "searchParameter": me,
                "verificationType": "BVN-FULL-DETAILS"
            }
            headers = {
                "accept": "application/json",
                "userid": "1647784769854",
                "apiKey": "d7nMevDBwe8gpn0h2aTm",
                "content-type": "application/json"
            }

            res = requests.post(url, json=payload, headers=headers).json()
            ress = res['response']
            vs = res['verificationStatus']
            if vs == "PENDING":
                messages.info(request,"Something unexpected happened", extra_tags='ans')
            else:
                if vs == "NOT VERIFIED":
                    messages.info(request,"No Record Found", extra_tags='ans')
                    math = int(nn) 
                    i = int(100)
                    done  =  math - i
                    print(done)
                    agent.objects.filter(email = user.username).update(wallet_bal = done)
                    rr = agent.objects.filter(email= user.username).values("wallet_bal")
                    ss=rr[0]['wallet_bal']
                else:
                    if vs == "FAILED":
                        messages.info(request,"Third Party System is Unavailable", extra_tags='ans')
                    else:
                        math = int(nn) 
                        i = int(150)
                        done  =  math - i
                        print(done)
                        agent.objects.filter(email = user.username).update(wallet_bal = done)
                        rr = agent.objects.filter(email= user.username).values("wallet_bal")
                        ss=rr[0]['wallet_bal']
                        
                        #image 
                        photo_bvn = ress['imageBase64']
                        byte_data_bvn =f"'{photo_bvn}'"
                        b_bvn= base64.b64decode(byte_data_bvn)
                        data_bvn = io.BytesIO(b_bvn)
                        data_bvn.seek(0)
                        pp_bvn = Image.open(data_bvn)
                        pp_bvn.save(data_bvn, "PNG")
                        end_bvn = base64.b64encode(data_bvn.getvalue())
                        img  = end_bvn.decode('utf-8')
                        
                        #sig  
                        photo1 = ress['basicDetailBase64']
                        byte_data1 =f"'{photo1}'"
                        b1= base64.b64decode(byte_data1)
                        data1 = io.BytesIO(b1)
                        data1.seek(0)
                        pp1 = Image.open(data1)
                        pp1.save(data1, "PNG")
                        end1 = base64.b64encode(data1.getvalue())
                        img1  = end1.decode('utf-8')
                        return render(request,'bvn.html',{"img_data":img,"img_data1":img1,"wallet":ss})
                        
    
    return render(request, 'bvn.html',{"wallet":nn})



def slip_generator(request):
    if request.method == 'POST' and request.FILES['file']:
        surname=request.POST["surname"]
        firstname=request.POST["firstname"]
        middlename=request.POST["middlename"]
        gender=request.POST["gender"]
        tracking=request.POST["tracking"]
        nin=request.POST["nin"]
        address=request.POST["address"]
        town=request.POST["town"]
        add_lga=request.POST["add_lga"]
        photo =request.FILES['file']
        print(photo.name)
        
        
        
        pp = Image.open(photo)
        pp.save('static/new_img.png')
        # with open(pp, "rb") as img_file:
        #     my_string = base64.b64encode(img_file.read())
        # print(my_string)
        # pp.show()
        
        
         
        
        
        if surname== surname:
            request.session['surname'] = surname
            request.session['firstname'] = firstname
            request.session['middlename'] = middlename
            request.session['gender'] = gender
            request.session['tracking'] = tracking
            request.session['nin'] = nin
            request.session['address'] = address
            request.session['town'] = town
            request.session['add_lga'] = add_lga
            messages.info(request,"Slip generated. Click to view", extra_tags='ans')
            
    return render(request,'slip_form.html')


def gen(request):
    context = {'surname':request.session['surname'],
                'firstname': request.session['firstname'] ,
                'middlename': request.session['middlename'],
                'gender': request.session['gender'],
                'nin': request.session['nin'],
                'tracking': request.session['tracking'],
                'address': request.session['address'],
                'town': request.session['town'],
                'add_lga': request.session['add_lga'],
                
                
    }
    return render(request, 'slip_generator.html',context)

def dashboard(request):
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    
    historys = Payment.objects.filter(email = user.username).all().values()
    pay = historys
    return render(request, 'dashboard.html',{"user":user, "wallet": nn,"trans": pay})


def basics(request):
    return render(request,'basics.html')

def my_portal(request):
    historys = agent.objects.all()
    pay = historys
    return render(request, 'my_portal.html',{"trans": pay})

def Profile(request):
    user = request.user
    profile_obj = agent.objects.filter(email = user.username).first()
    context = { 'user_id' : profile_obj.email}
    if  request.method == 'POST':
            new_password =  request.POST.get('new_pass')
            con_password = request.POST.get('con_pass')
            user_id = request.POST.get('user_id')
            
            if new_password != con_password:
                messages.info(request, 'Password mismatch. ')
                return redirect('change-password')
            
            user_obj = User.objects.get(username=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            agent.objects.filter(email = user.username).update(password = new_password)
            messages.info(request, 'Password changed successfully. ')
            return redirect('login')
    return render(request, 'profile.html',context)

def int_pass(request):
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    oo = int(nn)
    if oo < 150:
        messages.info(request,"Insufficient balance", extra_tags='ans')
        
    else:
        
        if request.method == 'POST':
            
            me=request.POST["int_pass_number"]
            me1=request.POST["int_pass_surname"]
            url = "https://api.verified.africa/sfx-verify/v3/id-service/"

            payload = {
                "searchParameter": me,
                "verificationType": "PASSPORT-FULL-DETAILS",
                "lastName": me1
            }
            headers = {
                "accept": "application/json",
                "userid": "1647784769854",
                "apiKey": "8Nqd6AxWoXEtEz69VYYZ",
                "content-type": "application/json"
            }

            res = requests.post(url, json=payload, headers=headers).json()
            ress = res['response']
            vs = res['verificationStatus']
            print(res)
            print(ress)
            print(vs)
            if vs == "PENDING":
                messages.info(request,"Something unexpected happened", extra_tags='ans')
            else:
                if vs == "NOT VERIFIED":
                    messages.info(request,"No Record Found", extra_tags='ans')
                    math = int(nn) 
                    i = int(100)
                    done  =  math - i
                    print(done)
                    agent.objects.filter(email = user.username).update(wallet_bal = done)
                    rr = agent.objects.filter(email= user.username).values("wallet_bal")
                    ss=rr[0]['wallet_bal']
                else:
                    if vs == "FAILED":
                        messages.info(request,"Third Party System is Unavailable", extra_tags='ans')
                    else:
                        math = int(nn) 
                        i = int(150)
                        done  =  math - i
                        print(done)
                        agent.objects.filter(email = user.username).update(wallet_bal = done)
                        rr = agent.objects.filter(email= user.username).values("wallet_bal")
                        ss=rr[0]['wallet_bal']
                        
                        pass_Surname =ress['last_name']
                        pass_firstname =ress['first_name']
                        pass_middlename =ress['middle_name']
                        pass_gender =ress['gender']
                        pass_dateofbirth =ress['dob']
                        pass_refernce =ress['reference_id']
                        pass_phonenumber =ress['mobile']
                        pass_issue_at =ress['issued_at']
                        pass_issue_date =ress['issued_date']
                        pass_ex_date =ress['expiry_date']
                        
                        messages.info(request,pass_Surname,extra_tags='m1')
                        messages.info(request,pass_firstname,extra_tags='m2')
                        messages.info(request,pass_middlename,extra_tags='m3')
                        messages.info(request,pass_gender,extra_tags='m4')
                        messages.info(request,pass_dateofbirth,extra_tags='m5')
                        messages.info(request,pass_refernce,extra_tags='m6')
                        messages.info(request,pass_phonenumber,extra_tags='m7')
                        messages.info(request,pass_issue_at,extra_tags='m8')
                        messages.info(request,pass_issue_date,extra_tags='m9')
                        messages.info(request,pass_ex_date,extra_tags='m10')
                        
                        photo12 = ress['photo']
                        print(photo12)
                        photo13 = photo12.replace('data:image/jpg;base64,', '')
                        byte_data12 =f"'{photo13}'"
                        b12= base64.b64decode(byte_data12)
                        print(b12)
                        data12 = io.BytesIO(b12)
                        data12.seek(0)
                        pp12 = Image.open(data12)
                        pp12.save(data12, "PNG")
                        end12 = base64.b64encode(data12.getvalue())
                        img12  = end12.decode('utf-8')
                        return render(request,'int_pass.html',{"wallet":ss,"img_data":img12})
                        
    return render(request, 'int_pass.html',{"wallet":nn})

def bbm(request):
    user = request.user
    mm = agent.objects.filter(email= user.username).values("wallet_bal")
    nn=mm[0]['wallet_bal']
    oo = int(nn)
    return render(request, 'bbm.html',{"wallet":nn})


def verify_payment(request: HttpRequest,ref:str) -> HttpResponse:
    user = request.user
    payment = get_object_or_404(Payment, ref=ref) 
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "verification successfull",extra_tags='success')
        p_amount = Payment.objects.filter(ref= ref).values("amount")
        p_list = p_amount[0]['amount']
        p_cal = int(p_list)
        rr = agent.objects.filter(email= user.username).values("wallet_bal")
        ss=rr[0]['wallet_bal']
        a_cal = int(ss)
        math = p_cal + a_cal
        print(math)
        agent.objects.filter(email = user.username).update(wallet_bal = math)
        a_update = agent.objects.filter(email= user.username).values("wallet_bal")
        a_new_amount=a_update[0]['wallet_bal']
        render(request, 'wallet.html',{"wallet":a_new_amount})
    else:
        messages.error(request, "verification Failed",extra_tags='success')
    return redirect('wallet') 



