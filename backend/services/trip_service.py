"""
Business Logic Layer for KelanaAI Recommendation Engine.
Berisi fungsi-fungsi bisnis murni untuk klasifikasi, kalkulasi, dan rekomendasi.
"""

from typing import List


def get_trip_category(budget: float) -> str:
    """
    Menentukan kategori perjalanan berdasarkan total budget (dalam USD).
    - budget < 1000          -> "Backpacker"
    - 1000 <= budget <= 3000 -> "Standard"
    - budget > 3000          -> "Luxury"
    """
    if budget < 1000:
        return "Backpacker"
    elif 1000 <= budget <= 3000:
        return "Standard"
    else:
        return "Luxury"


def get_travel_season(month: str) -> str:
    """
    Menentukan musim perjalanan berdasarkan nama bulan (case-insensitive & trim whitespace).
    - December -> "Peak Season"
    - June     -> "Holiday Season"
    - Lainnya  -> "Regular Season"
    """
    normalized = month.strip().lower()
    if normalized == "december":
        return "Peak Season"
    elif normalized == "june":
        return "Holiday Season"
    else:
        return "Regular Season"


def calculate_daily_budget(budget: float, days: int) -> float:
    """
    Menghitung alokasi budget harian (budget / days).
    Dilengkapi validasi defensif terhadap division by zero / angka non-positif.
    """
    if days <= 0:
        raise ValueError("Jumlah hari (days) harus lebih besar dari 0.")
    if budget < 0:
        raise ValueError("Budget tidak boleh bernilai negatif.")
    
    return round(budget / days, 2)


def get_recommendations(destination: str) -> List[str]:
    """
    Mengambil daftar rekomendasi tempat (List) berdasarkan nama destinasi.
    """
    dest_key = destination.strip().lower()

    # Database rekomendasi berbasis List
    database = {
        "japan": [
            "Tokyo Tower",
            "Shibuya",
            "Mount Fuji"
        ],
        "bali": [
            "Ubud Monkey Forest",
            "Tanah Lot",
            "Kuta Beach",
            "Uluwatu Temple"
        ],
        "paris": [
            "Eiffel Tower",
            "Louvre Museum",
            "Arc de Triomphe"
        ],
        "switzerland": [
            "Jungfraujoch",
            "Matterhorn Zermatt",
            "Lake Geneva"
        ]
    }

    # Fallback jika destinasi belum terdaftar
    return database.get(
        dest_key,
        [
            f"Pusat Kota {destination.title()}",
            f"Objek Wisata Populer {destination.title()}",
            f"Pusat Kuliner {destination.title()}"
        ]
    )
