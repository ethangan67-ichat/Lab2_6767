def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height**2)
    print("BMI is ", f"{bmi: .2f}")
    if bmi <18.5:
        print("UnderWeight")
        return -1
    elif bmi >25.0:
        print("Overweight")
        return 1
    else:
        print("Normal Weight")
        return 0



print(calculate_bmi(weight=57, height=1.73))
print(calculate_bmi(weight=87, height=1.73))
print(calculate_bmi(weight=17, height=1.73))