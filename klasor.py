import os  
print(""" 
1 - Bulunduğunuz dosyanın konumu 

2 - Dosyaları görüntüle 

3 - Dosya oluştur 

4 - Dosya adını değiştir 

5 - Dosya sil   
""")
sec = input(" => ")
if sec == "1":
   print(os.getcwd())
if sec == "2":
   print(os.listdir())
if sec == "3":
   oluscakdosya = input(" Lütfen oluşcak dosya & dizinin adını giriniz => ")
   os.mkdir(oluscakdosya)
   print(os.listdir())
if sec == "4":
    addeiscekdosya = input(" Adı değişcek dosyanın adı => ")
    print("")
    yeniad = input(" Dosyanın yeni adı => ")
    os.rename(addeiscekdosya,yeniad)
    print(os.listdir())
if sec == "5":
    print(""" 
    
    1 - Dizin kaldır (klasör)

    2 - Dosya kaldır (txt ,html ,vs ,sh vesayre)
    
    """)
    secim = input(" Seçenek seç =>")
    if secim == "1":
       secim2 = input(" Dosya adı =>")
       print(os.listdir())
       os.rmdir(secim2)
    if secim == "2":
        secim3 = input("dizin adı =>")
        print(os.listdir())
        os.remove(secim3)
