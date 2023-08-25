def is_power_of_four(n):
    b = bin(n)
    while len(b) > 3:
        if b[-2:] != "00":
            return False
        b = b[:-2]

    return b == "0b1"


N = 256

if __name__ == "__main__":
    print(is_power_of_four(N))
