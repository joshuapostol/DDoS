import random

def generate_ip_addresses(num):
    return ['.'.join(str(random.randint(0, 255)) for _ in range(4)) for _ in range(num)]
