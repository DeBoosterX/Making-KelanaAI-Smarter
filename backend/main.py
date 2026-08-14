"""
backend/main.py
Layer: Presentation Layer

Modul ini bertanggung jawab untuk interaksi dengan pengguna (CLI),
validasi input dasar, memanggil business logic dari trip_service,
serta memformat tampilan output KelanaAI.
"""

from services.trip_service import (
    get_trip_category,
    get_travel_season,
    calculate_daily_budget,
    get_recommendations
)


def main():
    print("==================================")
    print("Selamat Datang di KelanaAI Planner")
    print("==================================")
    
    # 1. Input Data dan Validasi
    destination = input("Masukkan Destinasi (contoh: Japan, Bali, Paris): ").strip()
    if not destination:
        print("Error: Destinasi tidak boleh kosong!")
        return

    try:
        days_input = input("Masukkan Jumlah Hari (Days): ").strip()
        days = int(days_input)
        if days <= 0:
            print("Error: Jumlah hari harus lebih besar dari 0.")
            return
    except ValueError:
        print("Error: Input hari harus berupa bilangan bulat positif.")
        return

    try:
        budget_input = input("Masukkan Total Budget (USD): ").strip()
        budget = float(budget_input)
        if budget <= 0:
            print("Error: Budget harus lebih besar dari 0.")
            return
    except ValueError:
        print("Error: Input budget harus berupa angka.")
        return

    month = input("Masukkan Bulan Perjalanan (contoh: December, June): ").strip()
    if not month:
        print("Error: Bulan perjalanan tidak boleh kosong!")
        return

    # 2. Proses Data Menggunakan Business Logic (Services Layer)
    category = get_trip_category(budget)
    season = get_travel_season(month)
    daily_budget = calculate_daily_budget(budget, days)
    recommendations = get_recommendations(destination)

    # Format angka budget untuk tampilan
    budget_display = int(budget) if budget.is_integer() else f"{budget:.2f}"

    # 3. Tampilkan Output Terformat
    print("\n==================================")
    print("KelanaAI")
    print("==================================")
    print(f"{'Destination':<16}: {destination.title()}")
    print(f"{'Days':<16}: {days}")
    print(f"{'Budget':<16}: {budget_display} USD")
    print(f"{'Category':<16}: {category}")
    print(f"{'Daily Budget':<16}: {daily_budget:.2f} USD/Day")
    print(f"{'Travel Month':<16}: {month.title()}")
    print(f"{'Season':<16}: {season}")
    print("\nRecommended Places:")
    
    # Iterasi daftar rekomendasi menggunakan for-loop
    for place in recommendations[:3]:
        print(f"- {place}")


if __name__ == "__main__":
    main()
