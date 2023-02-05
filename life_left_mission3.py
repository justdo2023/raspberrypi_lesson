expected_life_man = 80.6
expected_life_woman = 86.6


def main():
    age = int(input("나이를 입력하세요: "))
    sex = int(input("성별을 입력하세요: 여성 1 남성 0 "))

    if sex:
        years_left = expected_life_woman - age
    else:
        years_left = expected_life_man - age

    weeks_left = 52 * years_left
    days_left = 365 * years_left

    print("당신은 앞으로 ", years_left, "년,", weeks_left, "주,", days_left,"일 남았습니다.")


if __name__ == '__main__':
    main()