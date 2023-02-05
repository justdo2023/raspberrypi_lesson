
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    celsius = float(input("변환하고자 하는 섭씨 온도를 입력하세요: "))
    print("화씨 온도는 ", round(convert_to_celsius(celsius)), "도 입니다")


if __name__ == '__main__':
    main()

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
