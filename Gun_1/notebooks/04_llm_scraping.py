"""
Bölüm 4: LLM-Ready Web Scraping (Firecrawl API)
Bu script, geleneksel HTML karmaşası yerine, bir web sitesini doğrudan
Yapay Zeka modellerinin (LLM) sevdiği temiz Markdown formatına çevirir.
"""

import os
import requests
from dotenv import load_dotenv

# Optional: from firecrawl import FirecrawlApp
# Firecrawl kütüphanesi kullanmak isterseniz `pip install firecrawl-py`

# .env dosyasındaki değişkenleri yükle
load_dotenv()


def scrape_for_llm(api_key: str, url: str) -> None:
    """Firecrawl kullanarak siteyi Markdown formatında çeker."""
    firecrawl_url = "https://api.firecrawl.dev/v1/scrape"

    # API'ye göndereceğimiz komutlar
    payload = {
        "url": url,
        "formats": ["markdown"],
        "onlyMainContent": True,  # Menüleri ve reklamları atlar, sadece ana içeriği alır!
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    print(
        "🔥 Web sitesi LLM-Ready Markdown'a dönüştürülmek üzere Firecrawl API'sine gönderiliyor (Requests Yaklaşımı)..."
    )

    response = requests.post(firecrawl_url, json=payload, headers=headers)

    if response.status_code == 200:
        firecrawl_data = response.json()

        # API Response formatı versiyona göre değişebilir (data -> markdown veya direkt markdown)
        if "data" in firecrawl_data and "markdown" in firecrawl_data["data"]:
            markdown_content = firecrawl_data["data"]["markdown"]
        else:
            markdown_content = firecrawl_data.get("markdown", str(firecrawl_data))

        print("\n✅ Başarılı! HTML tagları yerine bu temiz formata bakın:\n")
        print("=" * 60)
        # Sadece ilk 3000 karakteri yazdırıyoruz
        print(markdown_content[:3000])
        print("\n... [MARKDOWN DOKÜMANININ GERİ KALANI]")
        print("=" * 60)
        print(
            "\n🤖 Bu metin artık ChatGPT, Claude veya kendi RAG sisteminize beslenmeye tamamen hazır!"
        )

        # Markdown içeriğini bir dosyaya kaydetmek için
        with open("scraped_content.md", "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print("\n✅ İçerik 'scraped_content.md' dosyasına kaydedildi.")

    else:
        print(f"❌ Çekim başarısız. Durum Kodu: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    # .env'den API anahtarını alıyoruz
    FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

    if not FIRECRAWL_API_KEY:
        print("❌ Hata: .env dosyasında FIRECRAWL_API_KEY bulunamadı!")
        print(
            "Lütfen projenin ana dizininde bir .env dosyası oluşturun ve anahtarınızı ekleyin."
        )
        import sys

        sys.exit(1)

    target_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

    # Requests mantığı ile çalıştır
    scrape_for_llm(FIRECRAWL_API_KEY, target_url)
