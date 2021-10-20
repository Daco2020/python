kor = ["가","나","다"]
eng = ["A","B","C"]

print(list(zip(kor, eng))) # 집은 리스트를 묶어줌

mixed = [('가', 'A'), ('나', 'B'), ('다', 'C')]
print(list(zip(*mixed))) # 변수 옆에 * 을 넣으면 언집, 즉 리스트를 풀어줌

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)