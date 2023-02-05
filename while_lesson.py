
def main():
    time = 0
    population = 1000
    growth_rate = 0.21
    while population < 2000:
        population = population + growth_rate * population
        print(round(population))
        time = time + 1
    print("박테리아가 두배가 되는데 걸린 시간은 ", time, "분 입니다.")
    print("최종 박테리아수는 ", round(population), " 입니다.")


if __name__ == '__main__':
    main()

