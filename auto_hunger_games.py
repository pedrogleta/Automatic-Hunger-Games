# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:40:28 2020

@author: pedro
"""

#Verifying Terms
#termsVerified = ['I am 13 years or older. I have read and understand these terms.',\
#                 'I am under the age of 13 and have parental guidance. I have read and understand these terms.']
#
#verifyTerms = input("By using this script, you agree that you are 13 years or older, that you have read the Privacy Policy\
#and the Disclaimer & Terms of Use linked in the README file. To proceed, enter 'I am 13 years or older.\
# I have read and understand these terms.' or 'I am under the age of 13 and have parental guidance.\
# I have read and understand these terms.': ")
#
#try:
#    if verifyTerms in termsVerified:
#        pass
#    else:
#        0/0
#except ZeroDivisionError:
#    print('Terms not agreed to.')
#    sys.exit()


import sys
import requests, bs4
from selenium import webdriver


def downloadImg(image_url, img_name):
    img_data = requests.get(image_url).content
    with open(img_name + '.jpg', 'wb') as handler:
        handler.write(img_data)

def getUrl(image):    
    url = """https://www.google.com/search?hl=en&tbm=isch&source=hp&biw=1920&bih=937&ei=fEg0Xr3sJ8ud5OUPvZaj0Ao&q=""" + image + """&oq=.&gs_l=img.3..0l10.4515.5946..6115...0.0..0.84.160.2......0....1..gws-wiz-img.....0.F8d4NDS-pEo&ved=0ahUKEwi9msC4lK7nAhXLDrkGHT3LCKoQ4dUDCAY&uact=5"""
    return url


#Picking Size
while True: 
    size = int(input('Escolha o número de tributos (24/36/48): '))
    if size not in [24,36,48]:
        print('O número precisa ser 24, 36 ou 48')
    else:
        break

participants = []
#Picking Participants
for i in range(size):
    participant = input('Selecione o participante ' + str(i) + ': ')
    participants.append(participant)
    downloadImg(getUrl(participant),i)
    
#Login Imgur
chrome = webdriver.Chrome()
payload = {'username': 'pedrogleta@gmail.com','password': 'RjM&Smf$2#FU*SE'}
chrome.get('https://imgur.com/signin?redirect=%2F')

inputs = chrome.find_elements_by_css_selector('input')
username = inputs[0]
password = inputs[1]
submit = chrome.find_element_by_css_selector('button')

username.send_keys(payload['username'])
password.send_keys(payload['password'])
submit.click()


chrome.get('https://brantsteele.net/hungergames/agree.php')
chrome.get('https://brantsteele.net/hungergames/ChangeTributes-' + str(size) + '.php)
