def calculate_bmi(weight,height):
    bmi=weight/(height**2)
    return bmi
def interpret_bmi (bmi):
    if bmi<18.5:
        return "your underweight"
    elif 18.5<=bmi<25:
        return "your normal weight"
    elif 25.0<=bmi<30:
        return "your overweight"
    else:
        return "obese"
def main():
    weight=float(input("enter your weight"))
    height=float(input("enter your height"))
    bmi=calculate_bmi(weight,height)
    interpretation=interpret_bmi(bmi)
    print(f"your BMI is:{bmi:.2f}")

    print(f"your are classified as:{interpretation}")
if __name__ == "__main__":
    main()
    
    
