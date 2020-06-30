#öncelikle tabloyu dictionary(sözlük) türünde tanımlıyoruz,
#karakterlerin kümesi isteğe
#veya ihtiyaca bağlı olarak artırılıp azaltılabilir

#burada tablo belli değerlere atandığı an otomatik olarak oluşturuluyor

tablo = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15,'r':16, 
's':17, 't':18, 'u':19, 'v':20, 'y':21, 'z':22, 'q':23, 'w':24, 'x':25}


#metni ve öteleme sayısını dışarıdan alıp metni şifreler

def metniSifrele(metin,oteleme):

#sifrelenmis karakterleri tutacak bir string ve 
#karakterlerin değerlerinin hesaplanması için
#bir değişken

	sifrelenmisMetin=""
	deger=0

#boşluksa ya da tabloda bulunmuyorsa olduğu gibi bırakır,
#öyle değilse yeni değeri büyük-küçük harf durumuna göre
#hesaplayıp sifrelenmisMetin değişkenine ekler

	for c in metin:
		if c == ' ':
			sifrelenmisMetin = sifrelenmisMetin + ' '
			continue
		elif c.lower() not in tablo:
			sifrelenmisMetin = sifrelenmisMetin + c
			continue

		if (deger+oteleme)>0:
		        deger=(tablo.get(c.lower())+oteleme)%len(tablo)
		else:
			deger = deger + oteleme
			while deger<0:
				deger=deger+(len(tablo))

		for karakter, yeniDeger in tablo.items():
			if yeniDeger == deger:
				if c.isupper():
					sifrelenmisMetin = sifrelenmisMetin + karakter.upper()
				else:
					sifrelenmisMetin = sifrelenmisMetin + karakter	

	print("Sifrelenmeden once metin:",metin)
	print("Sifrelendikten sonra metin:",sifrelenmisMetin)		
	

#boşluksa ya da tabloda bulunmuyorsa olduğu gibi bırakır,
#öyle değilse yeni değeri büyük-küçük harf durumuna göre
#hesaplayıp cozulmusMetin değişkenine ekler,maxOteleme
#degiskenindeki degere kadar her asamada o kadar öteleyip
#şifreyi çözer 

def metniCoz(metin,maxOteleme):
	cozulmusMetin=""
	deger=0
	for i in range(maxOteleme+1):
		
		for c in metin:
			if c == ' ':
				cozulmusMetin = cozulmusMetin + ' '
				continue
			elif c.lower() not in tablo:
				cozulmusMetin = cozulmusMetin + c
				continue

			deger=tablo.get(c.lower())

			if (deger-i)>0:
			        deger=(tablo.get(c.lower())-i)%len(tablo)
#çok büyük negatif değerler için			
			else:
				deger = deger - i
				while deger<0:
					deger=deger+(len(tablo))

			for karakter, yeniDeger in tablo.items():
				if yeniDeger == deger:
					if c.isupper():
						cozulmusMetin = cozulmusMetin + karakter.upper()
					else:
						cozulmusMetin = cozulmusMetin + karakter	


		if i == 0:
			cozulmusMetin=cozulecekMetin
		print("Cozulmus metin(Oteleme sayisi:"+str(i)+"):"+cozulmusMetin)
		cozulmusMetin=""


#menüyü oluşturup gerekli yönlendirmeleri yapar
if __name__=="__main__":
	while(True):
		print("-Metin sifrelemek için 1 girin")
		print("-Metin cozmek icin 2 girin")
		print("-Cikmak icin 3 girin")

		secim=input();

		if secim == "1":
			while(True):
				sifrelenecekMetin=input("Sifrelenecek metni girin(Menuye donmek icin 0 girin):")
				if sifrelenecekMetin == "0":
					break
				otelemeSayisi=input("Oteleme sayisini girin(Menuye donmek icin 0 girin):")
				try:
					otelemeSayisi=int(otelemeSayisi)
				except:
					print("-----Hatali veya cok buyuk bir sayi girdiniz!-----")
				if otelemeSayisi == 0:
					break


				metniSifrele(sifrelenecekMetin,otelemeSayisi)
		
		elif secim=="2":
			while(True):
				cozulecekMetin=input("Cozulecek metni girin(Menuye donmek icin 0 girin):")
				if cozulecekMetin == "0":
					break
				otelemeSayisi=input("Maksimum oteleme sayisini girin(Menuye donmek icin 0 girin):")
				try:
					otelemeSayisi=int(otelemeSayisi)
				except: 
					if otelemeSayisi == 0:
						break


				metniCoz(cozulecekMetin,otelemeSayisi)
		elif secim=="3":
			break
		else:
			print("-----Hatali bir secim yaptiniz,lutfen tekrar deneyin!-----")
