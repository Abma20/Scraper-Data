import requests
from bs4 import BeautifulSoup
import csv

# 1. Tentukan URL target
url = "https://example-news-site.com"

# 2. Kirim permintaan ke website
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# 3. Cek apakah koneksi berhasil (status 200)
if response.status_code == 200:
    # 4. Parsing HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 5. Cari elemen yang diinginkan (misal: tag <h2> untuk judul berita)
    headlines = soup.find_all('h2')
    
    # 6. Simpan hasil ke file CSV
    with open('hasil_berita.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["No", "Judul Berita"]) # Header
        
        for index, item in enumerate(headlines, 1):
            judul = item.text.strip()
            print(f"{index}. {judul}")
            writer.writerow([index, judul])

    print("\nData berhasil disimpan ke hasil_berita.csv")
else:
    print(f"Gagal mengakses website. Status code: {response.status_code}")