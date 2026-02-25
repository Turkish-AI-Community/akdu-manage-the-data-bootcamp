# 🚀 TYZT Bootcamp: Veri Toplama Masterclass

Bu proje, Türkiye Yapay Zeka Topluluğu (TYZT) Bootcamp'inde "Veri Toplama" eğitimi için hazırlanmış pratik kod örneklerini içerir.

## 🛠 Modern Python Araçları: uv ve ruff

Geleneksel araçlar yerine sektörün yeni standartları olan `uv` (hızlı paket kurulumu) ve `ruff` (kod düzenleyici/linter) araçlarını kullanacağız.

### 1. Ortam Kurulumu (Paket Yöneticileri)

**Seçenek A: Modern ve Aşırı Hızlı Yol (uv kullanarak)**
`uv`, Rust ile yazılmış ve standart `pip`'e göre 10-100 kat daha hızlı çalışan yeni nesil bir paket yöneticisidir.

Önce uv'yi kurun:

- **Mac/Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Windows:** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Sanal ortam (virtual environment) oluşturun ve aktif edin:

```bash
uv venv
# Mac/Linux için: source .venv/bin/activate
# Windows için: .venv\Scripts\activate
```

Paketleri ışık hızında kurun:

```bash
uv pip install -r requirements.txt
```

**Seçenek B: Geleneksel Yol (Standart pip kullanarak)**
Eğer standart yolu tercih ederseniz:

Sanal ortam oluşturun ve aktif edin:

```bash
python -m venv venv
# Mac/Linux için: source venv/bin/activate
# Windows için: venv\Scripts\activate
```

Paketleri kurun:

```bash
pip install -r requirements.txt
```

### 2. Kod Kalitesi ve Düzenleme (ruff kullanarak)

`ruff`, yine Rust ile yazılmış, saniyeden çok daha kısa sürede binlerce satır kodu analiz edip hataları bulan ve formatlayan bir araçtır. PEP8 standartlarına uymanızı sağlar.

**Hataları Bulmak (Linting):** Projenizdeki hatalı veya kullanılmayan kodları görmek için terminalde şu komutu çalıştırın:

```bash
ruff check .
```

**Otomatik Düzeltme:** Güvenli hataları (örneğin kullanılmayan import'ları) otomatik silmek için:

```bash
ruff check . --fix
```

**Kodu Formatlamak:** Kodunuzun girintilerini ve görünümünü standartlaştırmak için:

```bash
ruff format .
```

## 🏃‍♂️ Scriptleri Çalıştırma

Projeyi 4 ana modüle böldük. Sırasıyla terminalden çalıştırarak test edebilirsiniz:

- `uv run python 01_kaggle_dataset.py` (Kaggle verisi analizi)
- `uv run python 02_tomorrow_api.py` (Hava durumu API verisi)
- `uv run python 03_traditional_scraping.py` (Selenium ve BS4)
- `uv run python 04_llm_scraping.py` (Firecrawl ile LLM-Ready data)

## Kaynaklar

- [Tomorrow.io API](https://docs.tomorrow.io/reference/welcome)
- [Kaggle](https://www.kaggle.com/)
- [Firecrawl](https://firecrawl.dev/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Python](https://www.python.org/)
- [uv](https://astral.sh/uv/)
- [ruff](https://docs.astral.sh/ruff/)

## Kaggle Veriseti

- [Veriseti](https://www.kaggle.com/datasets/mahdimashayekhi/social-media-vs-productivity)
