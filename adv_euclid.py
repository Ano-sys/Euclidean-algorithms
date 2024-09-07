import sys
import math

def adv_euklid(m: int, n: int) -> (int, int):
    if n % m == 0:
        return (1, 0)
    else:
        x_, y_ = adv_euklid(n % m, m)
        x = y_ - x_ * math.floor(n / m)
        y = x_
        return (x, y)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python adv_euklid.py x y")
        exit(-1)

    m = int(sys.argv[1])
    n = int(sys.argv[2])
    x, y = adv_euklid(m, n)
    ggt = m * x + n * y
    
    print(f"ggT: {ggt}\nx: {x}\ny: {y}")
