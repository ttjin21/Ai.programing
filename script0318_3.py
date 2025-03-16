Python 3.11.0b1 (main, May  7 2022, 22:43:46) [MSC v.1931 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2<<0
2
2<<1
4
2<<2
8
2<<3
16
2<<4
32
2<<5
64
2<<6
128
2<<7
256
2<<8
512
2<<9
1024
n=int(input('정수를 입력하세요:'))
정수를 입력하세요:20
print('이 수가 짝수인가요?', n%2==0)
이 수가 짝수인가요? True
n=int(input('정수를 입력하세요:'))
정수를 입력하세요:21
print('이 수가 짝수인가요?', n%2==0)
이 수가 짝수인가요? False
a=int(input('정수 a를 입력하시오:'))
정수 a를 입력하시오:202
b=int(input('정수 b를 입력하시오:'))
정수 b를 입력하시오:50
print('a/b의 몫:', a//b)
a/b의 몫: 4
print('a/b의 나머지:', a%b)
a/b의 나머지: 2
n=int(input('세 자리 정수를 입력하시오:'))
세 자리 정수를 입력하시오:349
print('백의 자리:', 349//100)
백의 자리: 3
print('십의 자리:', (n//10)%10)
십의 자리: 4
print('일의 자리:', n%10)
일의 자리: 9
n=int(input('세 자리 정수를 입력하시오:'))
세 자리 정수를 입력하시오:349
n%10
9
(n//10)%10
4
n//100
3
