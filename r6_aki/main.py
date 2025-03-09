
def prime1(N: int):
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
    print(f'primes: {primes}')

    return primes



if __name__ == '__main__':
    prime1(20)
