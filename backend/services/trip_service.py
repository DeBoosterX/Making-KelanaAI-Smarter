"""
backend/services/trip_service.py
Layer: Business Logic Layer

Modul ini bertanggung jawab atas seluruh aturan bisnis dan perhitungan
rekomendasi perjalanan pada platform KelanaAI.
"""

def get_trip_category(budget: float) -> str:
    """
    Menentukan kategori perjalanan berdasarkan total budget (USD).
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
    Menentukan musim perjalanan berdasarkan nama bulan (Case-Insensitive).
    - December -> "Peak Season"
    - June     -> "Holiday Season"
    - Lainnya  -> "Regular Season"
    """
    normalized_month = month.strip().lower()
    
    if normalized_month == "december":
        return "Peak Season"
    elif normalized_month == "june":
        return "Holiday Season"
    else:
        return "Regular Season"


def calculate_daily_budget(budget: float, days: int) -> float:
    """
    Menghitung alokasi budget harian (budget dibagi days)
    dengan pembulatan 2 angka di belakang koma.
    """
    if days <= 0:
        raise ValueError("Jumlah hari (days) harus lebih besar dari 0.")
    return round(budget / days, 2)


def get_recommendations(destination: str) -> list:
    """
    Mengembalikan list rekomendasi tempat wisata berdasarkan destinasi populer.
    Menyediakan fallback rekomendasi jika destinasi belum terdaftar di database.
    """
    # Database lokal destinasi populer menggunakan dictionary & list
    destinations_db = {
        "japan": [
            "Tokyo Tower",
            "Shibuya",
            "Mount Fuji",
            "Fushimi Inari Taisha",
            "Dotonbori"
        ],
        "bali": [
            "Pantai Kuta",
            "Pura Tanah Lot",
            "Ubud Monkey Forest",
            "Uluwatu Temple",
            "Nusa Penida"
        ],
        "paris": [
            "Eiffel Tower",
            "Louvre Museum",
            "Arc de Triomphe",
            "Notre-Dame Cathedral",
            "Champs-Élysées"
        ],
        "switzerland": [
            "Jungfraujoch",
            "Lake Geneva",
            "Matterhorn",
            "Lucerne Chapel Bridge",
            "Interlaken"
        ]
    }
    
    normalized_dest = destination.strip().lower()
    
    # Ambil list rekomendasi tempat sesuai input
    if normalized_dest in destinations_db:
        return destinations_db[normalized_dest]
    else:
        # Fallback rekomendasi generik
        return [
            f"Pusat Kota {destination.strip().title()}",
            f"Museum Sejarah {destination.strip().title()}",
            f"Landmark Ikonik {destination.strip().title()}"
        ]
