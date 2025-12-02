# 가장 대표적인 소수 판별 알고리즘

'''
1. 소수 판별 알고리즘
 - 시간 복잡도: O(N)
'''
def isprime(num):
    for i in range(2, num):
        if num % i == 0:  # 1과 자기자신을 제외하고 하나라도 나누어지면 소수 X
            return False
    
    return True
print(isprime(97))

'''
2. 개선된 소수 판별 알고리즘
 - 시간 복잡도: O(N**0.5)
 - ex) 8의 소수 -> 1, 2, 4, 8
   2*4 = 4*2 대칭을 이룸
=> 제곱근까지만 약수의 여부 검증
'''
def isprime2(num):
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            return False
    return True
print(isprime2(97))

'''
3. 에라토스테네스의 체
 - 대량의 소수를 한꺼번에 판별하고자 할 때 사용
 1) 판별할 범위만큼 배열을 할당하고, 그 인덱스에 해당하는 값 넣기
 2) 2부터 시작해서 특정 숫자의 배수에 해당하는 숫자 제거
 3) 이미 지워진 숫자의 경우는 건너뛰기
'''
def isprime3(num):
    lst = [0] * (num+1)
    for i in range(2, num+1):   # 1번
        lst[i] = i
    
    for i in range(2, num+1):
        if lst[i] == 0:
            continue
        
        # 2번
        for j in range(i*i, num+1, i):
            lst[j] = 0
    
    return [i for i in lst[2:] if lst[i]]
print(isprime3(97))