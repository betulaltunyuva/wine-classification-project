#  Wine Veri Seti ile Makine Öğrenmesi Sınıflandırma Projesi

Bu projede, **scikit-learn** kütüphanesinde yer alan **Wine veri seti** kullanılarak bir sınıflandırma problemi ele alınmıştır. Çalışmanın amacı, şarap örneklerini kimyasal özelliklerine göre doğru sınıflara ayırmak ve farklı makine öğrenmesi algoritmalarının performanslarını karşılaştırmaktır.

---

## 📌 Proje Hakkında

Wine veri seti, farklı şarap örneklerine ait çeşitli kimyasal ölçümleri içermektedir. Bu projede veri seti önce incelenmiş, ardından bağımsız değişkenler ile hedef değişken ayrılmış ve eğitim-test süreci oluşturulmuştur.

Sonrasında iki farklı sınıflandırma modeli uygulanmıştır:

- **Decision Tree (Karar Ağacı)**
- **K-Nearest Neighbors (KNN)**

Elde edilen sonuçlar doğruluk oranı ve sınıflandırma metrikleri üzerinden karşılaştırılmıştır.

---

## 🎯 Projenin Amacı

Bu çalışmanın temel amacı:

- Wine veri setindeki örneklerin hangi sınıfa ait olduğunu tahmin etmek
- İki farklı sınıflandırma algoritmasının performansını karşılaştırmak
- Hangi modelin bu veri setinde daha başarılı sonuç verdiğini gözlemlemek

---

## 📊 Veri Seti Bilgisi

Projede `load_wine()` fonksiyonu ile gelen hazır **Wine Dataset** kullanılmıştır.

### Veri setinin genel özellikleri:
- **178 gözlem**
- **13 özellik**
- **3 sınıf**

### Kullanılan öznitelikler:
- alcohol
- malic_acid
- ash
- alcalinity_of_ash
- magnesium
- total_phenols
- flavanoids
- nonflavanoid_phenols
- proanthocyanins
- color_intensity
- hue
- od280/od315_of_diluted_wines
- proline

### Hedef değişken:
- **class**

---

## ⚙️ Uygulama Süreci

Projede sırasıyla aşağıdaki adımlar uygulanmıştır:

1. Wine veri seti yüklendi  
2. Veri çerçevesi oluşturuldu  
3. Bağımsız değişkenler (`X`) ve hedef değişken (`y`) ayrıldı  
4. Eğitim ve test verileri oluşturuldu  
5. Decision Tree modeli eğitildi  
6. KNN modeli eğitildi  
7. Accuracy, confusion matrix ve classification report ile değerlendirme yapıldı  
8. İki modelin sonuçları karşılaştırıldı  

---

## 🤖 Kullanılan Modeller

### 1) Decision Tree Classifier
Bu modelde aşağıdaki parametreler kullanılmıştır:

- `criterion = "entropy"`
- `max_depth = 3`
- `random_state = 0`

### 2) K-Nearest Neighbors (KNN)
Bu modelde aşağıdaki parametre kullanılmıştır:

- `n_neighbors = 5`

---

## 📈 Model Sonuçları

Uygulama sonunda elde edilen doğruluk oranları aşağıdaki gibidir:

| Model         | Accuracy |
|------         |----------|
| Decision Tree | **0.88** |
| KNN           | **0.67** |

Bu sonuçlara göre **Decision Tree modeli**, Wine veri seti üzerinde **KNN modeline göre daha başarılı performans göstermiştir**.

---

## 🧾 Değerlendirme Metrikleri

Projede modellerin başarısını ölçmek için şu yöntemler kullanılmıştır:

- **Accuracy Score**
- **Confusion Matrix**
- **Classification Report**

Bu metrikler sayesinde yalnızca genel doğruluk oranı değil, sınıf bazlı performans da incelenmiştir.

---

## 📁 Proje Dosyaları

```bash
wine-classification-project/
│
├── README.md
└── wine_classification.ipynb
```

## ✅ Son Değerlendirme
Bu çalışma, aynı veri seti üzerinde farklı sınıflandırma algoritmalarının farklı performanslar gösterebileceğini ortaya koymaktadır. Elde edilen sonuçlara göre bu problem için en başarılı model Decision Tree olmuştur.
