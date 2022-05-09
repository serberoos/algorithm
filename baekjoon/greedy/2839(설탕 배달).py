N = int(input())
count = 0;

while N >= 0:
	if N % 5 == 0: # 5로 나눈 나머지가 0 이라면
		count += N // 5 # 5로 나눈 나머지
		print(count)
		break;
	N -= 3 # 5의 배수가 될 때까지 3을 빼며 봉지 추가
	count += 1
else:
	print(-1) #while문이 거짓이라면 -1 출력