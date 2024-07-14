def position(t):
    """Menghitung posisi objek pada waktu t."""
    return 4 * t**2 + 2 * t + 4

def velocity(t):
    """Menghitung kecepatan objek pada waktu t (turunan pertama dari posisi)."""
    return 8 * t + 2

def acceleration():
    """Menghitung percepatan objek (turunan pertama dari kecepatan)."""
    return 8

def main():
    t1 = 1
    t5 = 5
    t0 = 0

    # Kecepatan pada t = 1 detik
    v1 = velocity(t1)
    print(f"Kecepatan pada t = {t1} detik adalah {v1} m/s")

    # Kecepatan rata-rata pada 5 detik pertama
    x5 = position(t5)
    x0 = position(t0)
    v_avg_5 = (x5 - x0) / (t5 - t0)
    print(f"Kecepatan rata-rata pada 5 detik pertama adalah {v_avg_5} m/s")

    # Percepatan sesaat
    a = acceleration()
    print(f"Percepatan sesaat adalah {a} m/s^2")

if __name__ == "__main__":
    main()
