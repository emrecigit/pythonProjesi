print("hello world") # hello world
print('hello'+' '+'world') # hello world
sampleString1= 'hello'
sampleString2=' '
sampleString3='world'
print(sampleString1+sampleString2+sampleString3) # hello world
print(sampleString1,sampleString2,sampleString3) #hello   world (, ile yazdırıldıgında her metin sonrası
                                                 # 1 bosluk ekler)
print(sampleString1,sampleString3) # hello world
print(sampleString1,sampleString2,sampleString3,sep='')  # hello world (sep ayraç tanımıdır ,
                                                         # otomatik olarak koyacağı boşluk yerine hiçlik koyar)
print(sampleString1,sampleString3,sep=' *** ') #hello *** world (ayrac olarak string bir ifade de kullanılabiliriz)
sampleString1 ='hello'
sampleString3 ='"world"'
print(sampleString1,sampleString3) # hello "world"
sampleString1 ='hello'
sampleString3 ="'world'"
print(sampleString1,sampleString3) # hello 'world'
sampleString2 ="'python' ders serisi"
print(sampleString2) # 'python' ders serisi
sampleString4 ="""Python's name does not come from 'snake'"""
print(sampleString4) #Python's name does not come from 'snake'
sampleString5 ="""Python's name does not come from 
'snake'"""
print(sampleString5) #Python's name does not come from (Başta ve sonda 3 adet " veya ' konursa
                     #'snake'                            istendiği yerde alt satıra geçer)

sampleString6 ='''
Hi Emre
How are you?
fyi
'''
print(sampleString6) # basta ve sonda """ veya ''' yazıldığında ,yazıldığı formatta çıktı alır