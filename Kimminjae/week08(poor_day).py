total = 0
adult, teen, kid = 0, 0, 0
ages = []
try:
    humans = int(input("몇 분이세요? "))
    for i in range(humans):
        ages.append(int(input("나이는? ")))

    print(ages)

    for age in ages:
        # 어른(20~) 20000, 청소년(8~19) 10000, 어린이(~7) 5000
        if age > 19:
            total += 20000
            adult += 1
        elif 8 <= age <= 19:
            total += 10000
            teen += 1
        else:
            total += 5000
            kid += 1
except IndexError:
    print("인덱스에서 범위를 체크하세요 (0에서 부터 전체 크기-1)")
except ValueError as err:
    print(f"입력값을 확인해주세요 \n{err}")
except Exception as err:
    print("무언가 에러가 발생")
    print(err)
else:
    print(f'어른 {adult}명, 청소년 {teen}, 어린이 {kid}명의 총 요금은 {total}원 입니다')
