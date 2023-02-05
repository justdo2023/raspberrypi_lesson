import random


def main():
    random_number = random.randint(1, 100)

    game_count = 1

    while True:
        number = int(input("1~100 사이 숫자를 맞추어 보세요: "))

        if number > random_number:
            print("다운")
        elif number < random_number:
            print("업")
        elif number == random_number:
            print("축하합니다. ! 당신은 ", game_count, "회만에 맞추셨습니다.")
            break;

        game_count = game_count + 1


if __name__ == '__main__':
    main()

