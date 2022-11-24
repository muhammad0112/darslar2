# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:53:43 2022

@author: Muhammad
"""
foydalanuvchilar = ["anvar","muhammad","islom","akrom","nusratillo","umidjon","g'iyosbek"]
login = input("loginni kiriting: ")
if login.lower() in foydalanuvchilar:
    print("login band! yangi login kiriting")
else:
    print(f"hush kelibsiz {login.title()}")    
