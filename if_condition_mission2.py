
def main():
    money = int(input("가진 돈을 입력하세요: "))

    if money > 3800:
        print("택시를 타세요")
    elif money > 1250:
        print("버스 타고 가세요")
    else:
        print("건강을 위해 걷는 것도 좋아요")


if __name__ == '__main__':
    main()
