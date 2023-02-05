###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################
x = 8
type(x)
y = 3.2
type(y)
z = 8j + 18
type(z)
a = "Hello World"
type(a)
b = True
type(b)
c = 23 < 22
type(c)

l = [1, 2, 3, 4,"String",3.2, False]
type(l)


d={"Name": "Jake",
     "Age": "[27,56]",
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)


s = {"Python", "Machine Learning", "Data Science","Python"}
type(s)



###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################
text = "The goal is to turn data into information, and information into insight."
tx1=text.replace(",","").replace(".","")
print(tx1.upper().split(" "))
###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
lst1=lst[0:4]

# Adım 4: Sekizinci index'teki elemanı silin.
lst.remove(lst[8])

# Adım 5: Yeni bir eleman ekleyin.
lst.append("W")


# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
lst.insert(8,"N")


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.
dict.keys()


# Adım 2: Value'lara erişiniz.
dict.values()


# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"]=['England', 13]

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({"Ahmet":["Turkey",24]})


# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")



###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]
even_list=[]
odd_list=[]
def func(k):
    for k in l:
        if k % 2 == 0:
            even_list.append(k)
            else:
            odd_list.append(k)
    print("cift sayilar : ", even_list,
          "tek sayilar : ", odd_list)

func(l)
############################################### -------
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
def ogr_siralama(x):
    for index, i in enumerate(ogrenciler,1):
        if index <= 3:
            print("Mühendislik Fakültesi ",index,". öğrenci: ",i)
        else:
            print("Tıp Fakültesi ",index-3,". öğrenci: ",i)

ogr_siralama(ogrenciler)

###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

ders_bilgileri=list(zip(ders_kodu,kredi,kontenjan))
#ders_bilgileri[0][1] diyerek degerlere ulaastık.
print("Kredisi ",ders_bilgileri[0][1], " olan ",ders_bilgileri[0][0]," kodlu dersin kontenjanı ",ders_bilgileri[0][2]," kişidir.",
"\nKredisi ",ders_bilgileri[1][1], " olan ",ders_bilgileri[1][0]," kodlu dersin kontenjanı ",ders_bilgileri[1][2]," kişidir.",
"\nKredisi ",ders_bilgileri[2][1], " olan ",ders_bilgileri[2][0]," kodlu dersin kontenjanı ",ders_bilgileri[2][2]," kişidir.",
"\nKredisi ",ders_bilgileri[3][1], " olan ",ders_bilgileri[3][0]," kodlu dersin kontenjanı ",ders_bilgileri[3][2]," kişidir.")

##bunu func ile ya da lambda ile yazabilir miydik??
###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])
def setfunc ():
if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))

setfunc()









