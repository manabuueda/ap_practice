"""
R6秋問3 素数を列挙するアルゴリズム

NOTE: 配列の要素番号が1から始まるため、若干
"""


def prime1(N: int):
    print('=== prime1 ===')
    primes: list = []
    isPrime: bool
    L1: int = 0

    d: int = 2
    t: int

    while (d <= N):
        isPrime = True
        t = 2

        while (t < d):
            if (d % t == 0):
                isPrime = False

            t += 1 # L1の計算量はO(N^2)
            L1 += 1 # 計算量の確認用

        if (isPrime):
            # primesの末尾にdの値を追加する
            primes.append(d)

        d += 1

    print(f'L1の計算回数: {L1}') # 計算量の確認用
    print(f'isPrime: {isPrime}')
    print(f'primes: {primes}')

    return primes

def prime2(N: int):
    print('=== prime2 ===')
    primes: list = []
    isPrime: list = [False]
    L2: int = 0

    c: int = 2
    d: int = 2
    t: int

    while (c <= N):
        isPrime.append(True)
        c = c + 1

    while (d <= N):
        if isPrime[d - 1] == True: # NOTE: 配列の要素番号が1を前提とした問題となっているため、-1している
            primes.append(d)
            t = d * d
            while (t <= N):
                isPrime[t - 1] = False # NOTE: 配列の要素番号が1を前提とした問題となっているため、-1している
                t = t + d
                L2 += 1 # 計算量の確認用
        d = d + 1

    print(f'L2の計算回数: {L2}') # 計算量の確認用
    print(f'isPrime: {isPrime}')
    print(f'primes: {primes}')

    return primes

def prime3(N: int):
    print('=== prime3 ===')
    primes: list = [2]
    isPrime: list = []
    L3: int = 0

    c: int = 3
    d: int = 3
    t: int

    while (c <= N):
        isPrime.append(True)
        c = c + 2

    while (d <= N):
        print(f'd: {d}')
        if isPrime[int((d-1)/2)-1] == True: # NOTE: 配列の要素番号が1を前提とした問題となっているため、-1している
            primes.append(d)
            t = d * d
            while (t <= N):
                isPrime[int((t-1) / 2)-1] = False # NOTE: 配列の要素番号が1を前提とした問題となっているため、-1している
                t = t + 2 * d
                L3 += 1 # 計算量の確認用
        d = d + 2

    print(f'L3の計算回数: {L3}') # 計算量の確認用
    print(f'isPrime: {isPrime}')
    print(f'primes: {primes}')

    return primes

if __name__ == '__main__':
    shizensu = 20
    prime1(shizensu)
    prime2(shizensu)
    prime3(shizensu)
