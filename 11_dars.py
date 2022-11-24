#son = 50
#if son<0:
#    print("manfiy son")
#else:
#    print("musbat son")    
#yosh = int(input("yoshingiz nechida? "))
#if yosh<4:
#    narh = 0    
#elif yosh<12:
#    narh = 5000
#elif yosh<25:
#    narh = 8000
#else:
#    narh = 10000
#print(f"sizga kirish {narh} so'm")
#hafta = ["dushanba","seshanba","chorshanba","payshanba","juma","shanba","yakshanba"]
#kun = input("bugun qanday kun: ")
#if kun.lower() == hafta[-1] or kun.lower() == hafta[-2]:
#    print("bugun dam olish kuni")
#else:
#    print("bugun ish kuni")
#kun = input("bugun qanday kun? ")  
#harorat = float(input("havo harorati qanday? "))  
#if kun.lower()=="yakshanba" and harorat>=30:
#    print("cho'milgani kettik!")
#else:
#    print("uyda dam olamiz") 
#kun = input("bugun qanday kun? ")
#harorat = float(input("havo harorati qanday? "))
#if (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat>=30:
#    print("cho'milgani kettik!")
#elif (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat<30:
#    print("uyda dam olamiz")
#narh = 15000
#choy = True
#salat = False
#if choy and salat:
#    narh = narh+10000
#elif choy or salat:
#    narh = narh+5000
#print(f"jami: {narh}")    
#narh = 15000
#choy = 1
#salat = 0
#kompot = 0
#non = 1
#assorti = 1
#if choy:
#    narh = narh+5000
#if salat:
#    narh = narh+3000
#if kompot:
#    narh = narh+10000
#if non:
#    narh = narh+2000
#if assorti:
#    narh = narh+15000
#print(f"jami: {narh}")    
#menu = ["osh","qozonkabob","shashlik","norin","somsa"]
#ovqat = input("nima ovqat yeysiz? ")
#if ovqat.lower() in menu:
#    print("Buyurtmangiz qabul qilindi")
#else:
#   print("ro'yhatda bunday taom mavjud emas")
#menu = ["osh","qozonkabob","shashlik","norin","somsa"]
#taom = input("buyurtmangizni kiriting: ")
#if taom.lower() not in menu:
#    print("bizda bunday taom mavjud emas")
#else:
#    print("Buyurtmangiz qabul qilindi")    
menu = ["osh","qozonkabob","shashlik","norin","somsa"]
buyurtmalar = ["osh","somsa","manti","shashlik"]
#buyurtmalar = []
if buyurtmalar:
  for yemek in buyurtmalar:
      if yemek in menu:
          print(f"menuda {yemek} bor")
      else:
          print(f"menuda {yemek} yoq")  
else:
    print("ro'yhat bo'sh")    