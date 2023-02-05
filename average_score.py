
def main():
    name = input("이름을 입력하세요: ")
    math_score = int(input("수학 점수를 입력하세요: "))
    english_score = int(input("영어점수를 입력하세요: "))
    history_score = int(input("역사점수를 입력하세요: "))
    average_score = round((math_score + english_score + history_score)/3)
    print(name + "님의 평균 성적은 " + str(average_score) + "점 입니다.")


if __name__ == '__main__':
    main()
