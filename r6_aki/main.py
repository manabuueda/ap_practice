"""
R6秋問3 素数を列挙するアルゴリズム

NOTE: 配列の要素番号が1から始まるため、若干
"""


def prime1(N: int):
    print("=== prime1 ===")
    primes: list = []
    isPrime: bool
    L1: int = 0

    d: int = 2
    t: int

    while d <= N:
        isPrime = True
        t = 2

        while t < d:
            if d % t == 0:
                isPrime = False

            t += 1  # L1の計算量はO(N^2)
            L1 += 1  # 計算量の確認用

        if isPrime:
            # primesの末尾にdの値を追加する
            primes.append(d)

        d += 1

    print(f"L1の計算回数: {L1}")  # 計算量の確認用
    print(f"isPrime: {isPrime}")
    print(f"primes: {primes}")

    return primes


def prime2(N: int):
    print("=== prime2 ===")
    primes: list = []
    isPrime: list = [False]
    L2: int = 0

    c: int = 2
    d: int = 2
    t: int

    while c <= N:
        isPrime.append(True)
        c = c + 1

    while d <= N:
        # NOTE: 配列の要素番号が1を前提とした問題となっているため、-1している
        if isPrime[d - 1] == True:  # 「イ」
            primes.append(d)
            t = d * d
            while t <= N:
                # NOTE: 配列の要素番号が1を前提とした問題となっているため、-1している
                isPrime[t - 1] = False  # 「ウ」
                """
                d以上の自然数xについて、dをx倍した数を、"素数ではない"とマークする
                """
                t = t + d
                L2 += 1  # 計算量の確認用
        d = d + 1

    print(f"L2の計算回数: {L2}")  # 計算量の確認用
    print(f"isPrime: {isPrime}")
    print(f"primes: {primes}")

    return primes


def prime3(N: int):
    print("=== prime3 ===")
    primes: list = [2]
    isPrime: list = []
    L3: int = 0

    c: int = 3
    d: int = 3
    t: int

    while c <= N:
        isPrime.append(True)
        c = c + 2

    while d <= N:
        print(f"d: {d}")
        # NOTE: 配列の要素番号が1を前提とした問題となっているため、-1している
        if isPrime[int((d - 1) / 2) - 1] == True:  # 「エ」
            """
            t = 2k+1
            2k = t-1
            k = (t-1)/2
            """
            primes.append(d)
            t = d * d
            while t <= N:
                # NOTE: 配列の要素番号が1を前提とした問題となっているため、-1している
                isPrime[int((t - 1) / 2) - 1] = False  # 「オ」
                """
                図2のプログラムでは、現在のtの値にdを加算することで＋1倍を実現していましたが、
                ここでは＋2倍としたいためdを2倍した値を加算すれば求める処理となります。したがって、空欄カには「t＋2×d」が当てはまります。
                """
                t = t + 2 * d  # 「カ」
                L3 += 1  # 計算量の確認用
        d = d + 2

    print(f"L3の計算回数: {L3}")  # 計算量の確認用
    print(f"isPrime: {isPrime}")
    print(f"primes: {primes}")

    return primes


if __name__ == "__main__":
    shizensu = 20
    prime1(shizensu)
    prime2(shizensu)
    prime3(shizensu)
