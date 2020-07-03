primelist = []


def prime_list():
    sieve = [True] * 9999

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(9999 ** 0.5)
    for i in range(1000, m + 1):
        if sieve[i]:  # i가 소수인 경우
            for j in range(i + i, 9999, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, 9999) if sieve[i] == True]

def change_prime(start,end,count):
    if start==end:
        return count
    digit = {start / 1000, (start / 100) % 10, (start / 10) % 10, start % 10}
    for i in range(len(digit)):
        if i == 0:
            for j in range(1,10):
                


def solution():
    T = input()
    for i in range(0, int(T)):
        N, M = map(int, input().split())
        primelist.append([N, M])

    prime = prime_list()


solution()
