"""
Bölüm 1: Kaggle'dan İndirilen Hazır Veri Setleri
Bu script, CSV formatındaki bir veriyi okur ve temel veri temizliği
(Garbage In, Garbage Out) kontrollerini yapar.
"""

import sys
import pandas as pd


def explore_dataset(file_path: str) -> None:
    """Veri setini okur ve temel istatistiklerini ekrana basar."""
    try:
        df = pd.read_csv(file_path)
        print("✅ Veri seti başarıyla yüklendi!\n")
        print(f"Veri Seti Boyutu: {df.shape[0]} Satır, {df.shape[1]} Sütun\n")

        print("--- İlk 3 Satır ---")
        print(df.head(3).to_string())
        print("\n")

        # "Garbage In, Garbage Out" kuralı gereği eksik verileri kontrol edelim.
        print("🔍 Eksik Veri (Missing Values) Kontrolü:")
        print(df.isnull().sum())

    except FileNotFoundError:
        print(
            f"❌ Hata: '{file_path}' bulunamadı. "
            "Lütfen Kaggle CSV dosyasının bu script ile aynı klasörde olduğundan emin olun."
        )
        sys.exit(1)


if __name__ == "__main__":
    # Veri setini şuradan indirebilirsiniz:
    # https://www.kaggle.com/datasets/mahdimashayekhi/social-media-vs-productivity
    csv_file = "social_media_vs_productivity.csv"
    explore_dataset(csv_file)
