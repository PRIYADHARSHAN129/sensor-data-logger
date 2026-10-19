import random


def read_distance():
    """Simulate an ultrasonic distance sensor reading in cm."""
    return round(random.uniform(5.0, 200.0), 2)