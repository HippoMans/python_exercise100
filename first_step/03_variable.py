# 변수명 규칙
# 1. 변수명의 시작은 _ 또는 영문자로 시작
# 2. 변수명의 두번째 문자부터는 알파벳, 숫자 그리고 밑줄 문자를 사용
# 3. 대소문자를 구분함으로 Count 변수와 count 변수는 다르다.
# 4. 파이썬 예약어 사용 X (if, elif, while, for, def, class, and, or 등)
_myname = "Hippo"       # _ 사용
my_name = "Man"         # 영문자 시작
H2mmm = "mmm"           # 두번째 문자를 숫자 2를 사용해도 된다.

# 대소문자 구분
Count = 1
print(Count)
count = 2
print(count)

# 파이썬 예약어 확인
import keyword
print(keyword.kwlist)

# 내장되어 있는 함수명을 변수명으로 사용하는 경우 함수 사용 불가
abs = 1
#abs(-3)    <- 함수 사용 X... 함수 형태로 사용하면 오류 발생

