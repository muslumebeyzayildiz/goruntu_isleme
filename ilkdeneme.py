import cv2
import numpy as np
from matplotlib import pyplot as plt

def bosFonk(x):#fonksiyon
    #print (x) her hareket ettitined hangi değer olduğunu dönecek trackbar 
    pass

img =np.zeros((512,512,3),np.uint8)#siyah arkaplanı pozitifint sayılardan oluşsun

cv2.namedWindow("gorsel")#boş çerçeve oluşturdum

cv2.createTrackbar("R","gorsel",0,255,bosFonk)#Trackbar name,hangi görsel içinde olacak değerinin başlangıcı nereye kadar ve fonksiyon
cv2.createTrackbar("G","gorsel",0,255,bosFonk)
cv2.createTrackbar("B","gorsel",0,255,bosFonk)

cv2.createTrackbar("ON/OFF","gorsel",0,1,bosFonk)


while(1):
    cv2.imshow('gorsel',img)#görüntüyü döngüye alalım ki sürekli göstersin
   
    if cv2.waitKey(1) & 0xFF == ord("q") :
    #çıkmak içinwaitkey(1) 0xFF azen hata veriyor hata vermesin diye 
    #q ya basınca kapatacak
    # == 27 olsaydı 27 ascii kodda esc escye basınca çıkac
    

        break
   
    r=   cv2.getTrackbarPos("R","gorsel")#HANGİ İFADENİN POZİSYONunu alacağım hangi pencere
    g=   cv2.getTrackbarPos("G","gorsel")
    b=   cv2.getTrackbarPos("B","gorsel")

    switch = cv2.getTrackbarPos("ON/OFF","gorsel")#gorsel çerçevesinde switch okuyor

    if switch:#1birse
        img[:] =[b,g,r]#img tüm piksellerini b g r e eşitliyorum
    else:
        img[:]=0#siyah bir görüntü olsun

cv2.destroyAllWindows()#kapansın diye


