from sensor import read_distance
from logger import save_readings

NUM_READINGS = 20


def main():
    readings = [read_distance() for _ in range(NUM_READINGS)]
    save_readings(readings)
    print(f"Saved {len(readings)} readings to readings.csv")
    print(f"Min:     {min(readings)} cm")
    print(f"Max:     {max(readings)} cm")
    print(f"Average: {sum(readings) / len(readings):.2f} cm")


if __name__ == "__main__":
    main()