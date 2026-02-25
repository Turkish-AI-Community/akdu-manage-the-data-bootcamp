"""
Bölüm 3: Geleneksel Web Scraping (BeautifulSoup & Selenium)
Bu script, Wikipedia üzerinden statik ve dinamik scraping tekniklerini gösterir.
"""

import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scrape_with_beautifulsoup(url: str) -> None:
    """BeautifulSoup ile statik HTML ayrıştırma."""
    print("--- 1. BEAUTIFULSOUP (Statik HTML Parsing) ---")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Sayfanın ana başlığını (H1) bulalım
    main_title = soup.find("h1", id="firstHeading")
    title_text = main_title.text if main_title else "Başlık Bulunamadı"

    print(f"✅ BeautifulSoup ile Çekilen Başlık: {title_text}\n")


def scrape_with_selenium(url: str) -> None:
    """Selenium ile tarayıcı otomasyonu."""
    print("--- 2. SELENIUM (Dinamik Tarayıcı Otomasyonu) ---")
    print("🤖 Otomatik tarayıcı (Chrome) arka planda başlatılıyor...")

    # Headless mod: Chrome'u görsel arayüzü olmadan çalıştırır, daha hızlıdır.
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # webdriver_manager sürücü uyumsuzluklarını otomatik çözer
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        # JavaScript'in veya sayfanın tam yüklenmesi için kısa bir bekleme
        time.sleep(2)

        # Selenium element seçicileri ile aynı başlığı bulalım
        main_title = driver.find_element("id", "firstHeading")
        print(f"✅ Selenium Botu ile Çekilen Başlık: {main_title.text}\n")

    finally:
        # Tarayıcıyı kapatmayı ASLA unutmayın, aksi takdirde RAM'de asılı kalır!
        driver.quit()
        print("Tarayıcı güvenle kapatıldı.")


if __name__ == "__main__":
    target_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

    scrape_with_beautifulsoup(target_url)
    scrape_with_selenium(target_url)
