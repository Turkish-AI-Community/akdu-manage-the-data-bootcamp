"""
Bölüm 2: API'ler ile Yapılandırılmış Veri Çekme
Bu script, Tomorrow.io Hava Durumu API'sine istek atarak
Antalya'nın anlık hava durumunu JSON formatında çeker.
"""

import os
import json
import requests
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()


def get_realtime_weather(api_key: str, lat: str, lon: str) -> None:
    """Tomorrow.io üzerinden canlı hava durumu verisi çeker."""
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={lat},{lon}&apikey={api_key}"
    headers = {"accept": "application/json"}

    print("📡 Tomorrow.io API'sine istek gönderiliyor...")

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        weather_data = response.json()

        # JSON sözlüğünün içinde gezinerek istediğimiz değerleri buluyoruz
        values = weather_data["data"]["values"]
        temp = values["temperature"]
        humidity = values["humidity"]
        wind_speed = values["windSpeed"]

        print("\n✅ Başarılı! İşte Antalya için canlı hava durumu:")
        print("-" * 40)
        print(f"🌡️ Sıcaklık     : {temp} °C")
        print(f"💧 Nem          : {humidity} %")
        print(f"💨 Rüzgar Hızı  : {wind_speed} m/s")
        print("-" * 40)

        # Katılımcılara ham JSON verisinin neye benzediğini göstermek için
        print("\nHam JSON Yanıtı (İlk 300 karakter):")
        print(json.dumps(weather_data, indent=2)[:300] + "...")
    else:
        print(f"❌ Veri çekilemedi. Durum Kodu: {response.status_code}")
        print("API anahtarınızı kontrol edin.")


if __name__ == "__main__":
    # .env tabanlı API Key okunması
    TOMORROW_API_KEY = os.getenv("TOMORROW_API_KEY")

    if not TOMORROW_API_KEY:
        print("❌ Hata: .env dosyasında TOMORROW_API_KEY bulunamadı!")
        print(
            "Lütfen projenin ana dizininde bir .env dosyası oluşturun ve anahtarınızı ekleyin."
        )
        import sys

        sys.exit(1)

    # Antalya Koordinatları (yaklaşık)
    LATITUDE = "36.8969"
    LONGITUDE = "30.7133"

    get_realtime_weather(TOMORROW_API_KEY, LATITUDE, LONGITUDE)
