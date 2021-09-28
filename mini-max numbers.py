def computegrade(score):
    
    if score<0 or score>1.0:
        return 'outta range'

    elif score>=0.9:
        return 'A' 

    elif score>=0.8:
        return 'B'

    elif score>=0.7:
        return 'C'

    elif score>=0.6:
        return 'D'

    else:
        return 'F'

score = computegrade(float(input("enter score: ")))

print("Grade is :", score)