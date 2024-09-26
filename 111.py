def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    try:
        weight = float(input("請輸入您的體重(公斤): "))
        height = float(input("請輸入您的身高(公尺): "))
        
        bmi = calculate_bmi(weight, height)
        
        print(f"您的 BMI 值為: {bmi:.2f}")
        
        if bmi < 18.5:
            print("體重過輕")
        elif 18.5 <= bmi < 24.9:
            print("體重正常")
        elif 25 <= bmi < 29.9:
            print("體重過重")
        else:
            print("肥胖")
    except ValueError:
        print("請輸入有效的數字")

if __name__ == "__main__":
    main()