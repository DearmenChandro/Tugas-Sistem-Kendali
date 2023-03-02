# Tugas-Sistem-Kendali

# Dearmen Chandro Rumasingap

# 21/473866/PA/20437

Program di atas adalah implementasi Python dari stabilitas Routh yang dapat menghitung nilai polinomial, menampilkan tabel Routh, dan menerima masukan dari variabel K oleh pengguna untuk menghitung tabel Routh yang diperbarui. Berdasarkan program di atas dapat diperhatikan fungsi evaluate_polynomial adalah mengambil argumen koefisien polinomial dan titik s, kemudian menghitung nilai polinomial pada titik tersebut. Lalu ada juga fungsi dari routh_stability mengambil argumen koefisien polinomial dan nilai K. Fungsi ini menghitung dan menampilkan tabel Routh untuk polinomial yang diberikan dan nilai K. Algoritma kriteria stabilitas Routh digunakan untuk menghitung nilai-nilai tabel Routh. Program utama menggunakan fungsi evaluate_polynomial dan routh_stability untuk menghitung nilai polinomial dan menampilkan tabel Routh dengan nilai K awal yang dimasukkan pengguna melalui input. Setelah tabel Routh pertama kali ditampilkan, pengguna diminta untuk memasukkan nilai K baru untuk menghitung tabel Routh yang diperbarui. Kedua tabel Routh dicetak di layar. Untuk menerapkan stabilitas Routh, kita dapat memeriksa apakah semua elemen di baris pertama tabel Routh adalah bilangan positif. Jika ada elemen yang nol atau negatif, maka sistem yang diwakili oleh polinomial tersebut bernilai tidak stabil.
