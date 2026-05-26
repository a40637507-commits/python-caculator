# 더하기 함수
def add(num1, num2):
    return num1 + num2

# 빼기 함수
def subtract(num1, num2):
    return num1 - num2

# 프로그램 실행 부분
if __name__ == "__main__":
    print("=== 🧮 파이썬 계산기 프로그램 ===")
    
    # 1. 사용자에게 숫자와 연산자 입력받기
    # input()으로 받은 값은 문자열이기 때문에, int()를 감싸서 숫자로 바꿔줍니다.
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    operator = input("연산자를 입력하세요 (+ 또는 -): ")
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    
    print("-" * 30) # 구분선
    
    # 2. 사용자가 입력한 연산자 기호에 따라 계산하기
    if operator == "+":
        result = add(num1, num2)
        print(f"결과: {num1} + {num2} = {result}")
        
    elif operator == "-":
        result = subtract(num1, num2)
        print(f"결과: {num1} - {num2} = {result}")
        
    else:
        print("❌ 에러: + 또는 - 기호만 입력할 수 있습니다.")