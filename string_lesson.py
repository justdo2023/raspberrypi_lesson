# 샘플 Python 스크립트입니다.

# ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.


def main():
    a = "Life is short , you need python"
    print(a.count('o'))
    print(a.find('p'))
    print(a.upper())
    print(a.lower())
    print(a.replace('python', 'money'))
    print(a.split())
    comma = ','
    string = "abcde"
    print(comma.join(string))
    print(string)
    name = "John"
    age = 30
    print("My name is %s, and I am %d years old." % (name, age))
    print(f"My name is {name}, and I am {age} years old.")
    temperature = 25
    print("The current  temperature is %d" % temperature)
    pet_name = 'Bori'
    print("My dog's name is %s" % pet_name)
    a = 10
    print("I ate %d apples" % a)
    print("%10s" % "space")
    print("%-10s" % "space")
    print("%0.3f" % 3.141592)
    print("%10.3f" % 3.141592)
    sum = 0
    for num in range(1, 101):
        sum = sum + num
    print(sum)

    sum = 0
    for num in range(2, 101, 2):
        sum = sum + num

    print(sum)


if __name__ == '__main__':
    main()

