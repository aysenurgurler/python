myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# bir değişkenin yeniden bildirilmesi çalışır
myint = "abc"
print (myint)

# sıra türünün bir üyesine erişmek için [] kullanın
print(mylist[2])
print(mytuple[1])
# bir dizinin parçalarını almak için dilimleri kullanın
print(mylist[1:4:2])
# bir diziyi tersine çevirmek için dilimleri kullanabilirsiniz
print(mylist[::-1])

# sözlüklere anahtarlar aracılığıyla erişilir
print(mydict["one"]) 

# HATA: farklı türdeki değişkenler birleştirilemez
#print ("dize türü " + 123)
print ("string type " + str(123))

# Fonksiyonlarda global ve yerel değişkenler
def someFunction():
    #global mystr
    mystr = "def"
    print (mystr)

someFunction()
print (mystr) 

del mystr
print (mystr)
