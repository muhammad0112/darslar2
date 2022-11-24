# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:19:11 2022

@author: UserPC
"""

mahsulotlar = ["uzum","olma", "anor", "nok","shoftoli", "behi", "non","sabzi", "kartoshka", "sholgom", "piyoz", "shkolad"]
soralganlar = []
bor = []
yoq = []
for son in range(5):
    soralganlar.append(input(f"savatga {son+1}- mahsulotni kiriting: "))
for soralgan in soralganlar:
    if soralgan in mahsulotlar:
        bor.append(soralgan)
    
    else:
        soralgan not in soralganlar
        yoq.append(soralgan)
if yoq:
    print("dokonimizda quyidagi mahsulotlar yo'q: ")
    for y in yoq: 
        print(y)
else:
    print("dokonimizda siz soragan barcha mahsulot mavjud")    

    
    
