import traceback


def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi


if __name__ == '__main__':
    try:
        # code that might raise an exception
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))

        bmi = calculate_bmi(weight, height)
        print("Your BMI is:", bmi, round(bmi, 2))

    except Exception as e:
        print(e)
        print("Traceback:")
        traceback.print_exc()





