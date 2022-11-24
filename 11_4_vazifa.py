# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:00:40 2022

@author: muhammad
"""
mahsulotlar = ["uzum","olma", "anor", "nok","shoftoli", "behi", "non","sabzi", "kartoshka", "sholgom", "piyoz", "shkolad"]
savat = []
for son in range(5):
    savat.append(input(f"{son+1}- mahsulotni kiriting: "))   
for mah in savat:
    if mah.lower() in mahsulotlar:
        print(f"dokonimizda {mah} bor")
    else:
        print(f"dokonimizda {mah} yo'q")


