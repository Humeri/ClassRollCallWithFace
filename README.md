# :busts_in_silhouette: ClassRollCallWithFace
###  Gerçek Zamanlı Yüz Tanıma ile Otomatik Yoklama Alma Sistemi
Bu projede, Python programlama dili kullanılarak OpenCV, Numpy, Pyttsx3, Face Recognition, os, glob gibi çeşitli modüller ve kütüphaneler entegre edilmiştir. Bu entegrasyon, Anaconda ve Spyder ortamında gerçekleşmiştir. Proje, sınıf içindeki öğrencilerin yüzlerini tanıyarak otomatik bir yoklama alır ve bu bilgileri bir Excel dosyasına düzenli bir şekilde kaydeder. Ayrıca, "Pyttsx3" kütüphanesi kullanılarak ilgili bilgiler sesli bir şekilde ifade edilir, böylece kullanıcıya sesli geri bildirim sunulur. Bu sayede Otomatik yoklama alma işlemini büyük ölçüde kolaylaştırır ve hızlandırır. Ayrıca, yüz tanıma teknolojisinin gücünü ve kullanışlılığını gösterir. Bu tür projeler, eğitim kurumları, toplantılar veya etkinlikler için kullanılabilir ve zaman tasarrufu sağlayabilir. <br/> <br/>


## :rocket:Proje Aşamaları:
-  ##### Yüz Algılama ve Tanıma
   - Kamera tarafından yakalanan görüntüler OpenCV ve Face Recognition kullanılarak yüzlerin algılanması sağlanır.
   - Algılanan yüzler, Face Recognition aracılığıyla tanımlanır ve kaydedilir.
   - Sınıf yoklamasına kayıtlı olmayan öğrencileri ise misafir öğrenci olarak kayda alır. <br/> <br/> 
   - ![Face Recognition](https://github.com/Humeri/ClassRollCallWithFace/blob/main/images-git/facerecognition.PNG) <br/> <br/>
   - ![Face Recognition](https://github.com/Humeri/ClassRollCallWithFace/blob/main/images-git/misafirogrenci.PNG)   
   
-  ##### Yoklama Alma ve İsimleri Sesli Okutma
   - Yoklama bilgileri için csv formatında bir dosya oluşturur.
   - Tanınan kişilerin isimlerini sesli olarak okur.
   - Tanınan her kişi için ad, soyad, öğrenci numarası ve saat bilgisi kaydedilir.
   - Oluşturulan dosya içerisinde veriler depolanır. <br/> <br/>
   - ![Face Recognition](https://github.com/Humeri/ClassRollCallWithFace/blob/main/images-git/csv.PNG)

-  ##### Sonuçlar
   - Ders sonunda, excel dosyası katılımcıların yoklama bilgileriyle doldurulmuş olur.
   - Bu dosya, alınan yoklamanın tarihine göre düzenlenir ve saklanır. <br/><br/>


 :pushpin: **İmage klasöründeki resimler projede kullanılmak üzere örnek olarak konulmuştur. Normalde dersin yoklama listesine kayıtlı olan öğrenciler bulunmaktaydı.( Ayrıca isimlerde türkçe karakterler kullanılmamalıdır.)**








