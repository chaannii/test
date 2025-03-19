#2.1
print(200,'+',300,'+',400,'=',200+300+400)

#2.2
width=30
height=60
print(width)
print(height)

#2.3
rectangle_area=width*height
print('사각형의 면적 :', rectangle_area)

#2.4
width=40
height=20
triangle_area=width*height*1/2
print('삼각형의 면적 :', triangle_area)

#2.5
side_length=int(input('정사각형의 밑변을 입력하시오 :'))
area = side_length ** 2
print('정사각형의 면적:', area)

#2.6
print('1에서 10까지의 합:', 1+2+3+4+5+6+7+8+9+10)

#2.7
print('10! :', 1*2*3*4*5*6*7*8*9*10)

#2.10
celsius=int(input('섭씨 온도를 입력하세요 :'))
fahrenheit= (9/5)*celsius+32
print('섭씨',celsius, '도는 화씨', fahrenheit, '도 입니다.')

#2.11
fahrenheit=int(input('화씨 온도를 입력하세요 :'))
print('화씨', fahrenheit, '도는 섭씨', celsius, '도 입니다.')

#2.12
radius=11
print('원의 반지름 =', radius,', 원의 둘레 =', 2.0*3.141592*radius,', 원의 면적 =', 3.141592*radius*radius)

#2.13
radius=int(input('원의 반지름을 입력하세요 :'))
print('원의 둘레 =',2.0*3.141592*radius,'원의 면적=',3.141592*radius*radius)

#2.15
a=int(input('밑변을 입력하세요 :'))
b=int(input('높이를 입력하세요 :'))
c=(a**2+b**2)**0.5
print('빗변 :', c)

#2.17
for i in range(10):
    print(2<<i, end=' ')

#2.18
n=int(input('정수를 입력하세요:'))
if n%2==0:
    print('이 수가 짝수인가요? true')
else:
    print('이 수가 짝수인가요? false')

#2.19
n=int(input('정수를 입력하세요:'))
if 0 <= n <= 100 and n % 2 == 0:
    print('입력한 정수는 0에서 100의 범위 안에 있는 짝수인가요? true')
else:
    print('입력한 수는 0에서 100의 범위 안에 있는 짝수인가요? false')

#2.21
n = int(input('정수를 입력하시오:'))
print(n,'의 2진수 값:', bin(n))
print(n,'의 2진수 값에 대한 비트단위 부정값:', bin(~n))

#2.22
a=int(input('정수 a를 입력하시오 :'))
b=int(input('정수 b를 입력하시오 :'))
print('a / b의 몫 :', a//b)
print('a / b의 나머지 :', a%b)

#2.23
n=int(input('세 자리 정수를 입력하시오 :'))
print('백의 자리 :', n//100)
print('십의 자리 :', (n//10)%10)
print('일의 자리 :', n%10)

#2.24
n=int(input('세 자리 정수를 입력하시오 :'))
print(n%10)
print((n//10)%10)
print(n//100)

#2.8 2.9 2.14 2.16 2.20 모르겠어요
