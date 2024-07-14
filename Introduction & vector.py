import numpy as np

def calculate_momentum(mass, velocity):
    """
    Menghitung momentum vektor dari massa dan kecepatan.
    
    :param mass: Massa objek (kg)
    :param velocity: Vektor kecepatan (m/s) dalam bentuk numpy array [vx, vy, vz]
    :return: Vektor momentum (kg·m/s) dalam bentuk numpy array [px, py, pz]
    """
    momentum = mass * velocity
    return momentum

def main():
    # Diketahui
    mass = 100  # kg
    velocity = np.array([15, 60, -2])  # m/s (vx, vy, vz)

    # Hitung momentum
    momentum = calculate_momentum(mass, velocity)
    print(f"Momentum yang dimiliki oleh Truk tersebut adalah {momentum} kg·m/s")

if __name__ == "__main__":
    main()
