"""
Presentation Layer for KelanaAI Recommendation Engine.
Bertanggung jawab menangani input/output dari user dan menampilkan hasil.
"""

import sys
from pathlib import Path

# Proteksi agar import services selalu bekerja baik dijalankan dari root maupun dari backend/
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from services.trip_service import (
    get_trip_category,
    get_travel_season,
    calculate_daily_budget,
    get_recommendations,
)


def main():
    # 1. Menerima Input dari User
    destination = input("Destination : ").strip()
    days_raw = input("Days        : ").strip()
    budget_raw = input("Budget      : ").strip()
    month = input("Travel Month: ").strip()

    # 2. Validasi Tipe Data & Nilai Positif
    try:
        days = int(days_raw)
        budget = float(budget_raw)
    except ValueError:
        print("\n[Error]: Days harus berupa angka bulat dan Budget harus berupa angka!")
        return

    if days <= 0 or budget <= 0:
        print("\n[Error]: Days dan Budget harus lebih besar dari 0!")
        return

    # 3. Proses Data Melalui Business Logic
    category = get_trip_category(budget)
    season = get_travel_season(month)
    daily_budget = calculate_daily_budget(budget, days)
    places = get_recommendations(destination)

    # Format angka (tampilkan integer jika bulat, contoh 1500 USD & 300 USD/Day)
    formatted_budget = f"{int(budget)}" if budget.is_integer() else f"{budget:.2f}"
    formatted_daily = f"{int(daily_budget)}" if daily_budget.is_integer() else f"{daily_budget:.2f}"

    # 4. Tampilkan Output Persis Sesuai Format Spesifikasi
    print("\n==================================")
    print("KelanaAI")
    print("==================================")
    print(f"Destination     : {destination.title()}")
    print(f"Days            : {days}")
    print(f"Budget          : {formatted_budget} USD")
    print(f"Category        : {category}")
    print(f"Daily Budget    : {formatted_daily} USD/Day")
    print(f"Travel Month    : {month.title()}")
    print(f"Season          : {season}")
    print("\nRecommended Places:")

    # Iterasi List rekomendasi tempat menggunakan for-loop
    for place in places:
        print(f"- {place}")


if __name__ == "__main__":
    main()
