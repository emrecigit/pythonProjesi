print("hello world") # tırnak veya kesme isareti farketmez
print('hello wolrd')
print('hello'+' '+'world') # toplama islemi yapılabilir (ifadeleri yanyn getirir) hello world
print('*'*10) # string bir ifade ile çarpma yapılabilir **********
print('hello'*10) # hellohellohellohellohellohellohellohellohellohello
print('hello world'[6])
sampleString="hello world"
print(sampleString[0])  # h index 0 ile başlar ve h harfini verir -1
                        # yazarsak metnin sonuna gider ve ordan saymaya başlar
print(sampleString[-1]) # d
print(sampleString[-2]) # l
print(sampleString[0:3]) # hel (2 index arası için : kullanılır ilk endex dahil son endex hariç alır)
print(sampleString[:3]) # hel (başlangıç indexi yazılmazsa default degeri alır yani 0 alınır)
print(sampleString[0:]) # hello world (gideceği index boş kalırsa default degeri tamamını ifade eder)
print(sampleString[:]) # hello world (iki index de boşşsa yani yine = dan başlar sonuna kadar yazdirir)
print(sampleString[1:-2]) # ello wor