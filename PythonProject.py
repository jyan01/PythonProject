Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import keyword
print(keyword.kwlist)
#하나만 출력
print("# 하나만 출력.")
print("Hello Python Programing...!")
print()

#여러 개를 출력
print("# 여러개를 출력.")
print("안녕하세요", "저의", "이름은", "안준영입니다.")
print()

#아무것도 입력하지 않을 경우 단순 줄바꿈
print("# 아무것도 출력하지 않음.")
print("___ 확인 전용선 ___")
print()
print()
print("--- 확인 전용선---")
print("\"안녕하세요\" 라고 말했습니다.")
print('\'배가 고픕니다\'라고 생각했습니다')
print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t3\t강서구")
print("구름\t3\t강서구")
print("""\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한사람 대한으로 길이 보전하세""")

# 출력합니다.
print(3 * "안녕하세요")

#출력합니다.
print("# 문자 선택 연산자")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

#출력합니다.
print("# 문자 선택 연산자 : 뒤에서부터 선택")
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])

#출력합니다.
print("# 문자 범위 선택 연산자")
print('"안녕하세요"[0:2]:', "안녕하세요"[0:2])
print('"안녕하세요"[1:3]:', "안녕하세요"[1:3])
print('"안녕하세요"[2:4]:', "안녕하세요"[2:4])
print()
print("# 문자 범위 선택 연산자 : 한쪽 숫자 생략")
print('"안녕하세요"[3:]:', "안녕하세요"[3:])
print('"안녕하세요"[:3]:', "안녕하세요"[:3])

#출력합니다.
print("# IndexError 예외")
print("안녕하세요"[10])
