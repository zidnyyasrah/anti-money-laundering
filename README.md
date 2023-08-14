**Halo!**, Perkenalkan nama saya Zidny Yasrah Sallum, Student Full Time Data Science hacktiv8 batch 20 Remote.

Link Dataset : https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml

Link Model Deployment : https://huggingface.co/spaces/zidnyyasrah/anti-money-laundering/tree/main

# Anti Money Laundering

Pada Final Project ini, saya membuat classification model untuk mengklasiifikasikan apakah seseorang melakukan tindakan money laundering pada sebuah transaksi.

# Hasil Analisis 

Dari keempat alalah yang terbaik. Setelah dilakukan hyperparameter tuning, model menjadi goritma baseline machine learning yang digunakan mulai dari `Local Outlier Factor`, `Isolation Forest`, `Logistic Regression`, dan `Random Forest`. Terlihat bahwa peforma dari `Random Forest` adlebih pandai dalam mengklasifikasikan kasus money laundering, namun tetap ada trade-off antara precisionnya yang meningkat, menandakan kasus false positive juga ikut naik.

## **Kelebihan dan Kekurangan Model**

#### Kelebihan

* Recall yang tinggi pada class 1, menandakan model ini bisa dengan baik memprediksi kasus-kasus money laundering. Kalau menurut saya dalam kasus money laundering, kita harus berupaya untuk meminimalkan nilai False Negative.   

#### Kekurangan

* Precision yang rendah pada class 1, nilai precision pada class 1 itu hanya 0.02, menandakan dari seluruh kasus yang diprediksi sebagai money laundering oleh model, hanya 2% nya saja yang benar-benar termasuk kasus money laundering. nilai precision yang rendah ini menandakan banyaknya kasus false positive. Akan lumayan memakan resource dan juga waktu untuk mengidentifikasi kasus-kasus lainnya

## **Further Improvement**

Bisa dilihat bahwa adanya limitasi pada model yang telah dibuat. Pada kasus money laundering ini sepertinya model machine learning tradisional seperti random forest dan lain-lain masih kesulitan dalam membaca pattern yang ada pada skema-skema money laundering ini. Kedepannya akan lebih baik menggunakan model yang lebih advance seperti Artificial Neural Network, dimana dia mempunyai ability untuk menangkap pattern dan interaksi pada data yang sangat kompleks.