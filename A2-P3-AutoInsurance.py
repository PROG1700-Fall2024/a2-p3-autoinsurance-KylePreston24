#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     W0443556
#Student Name:  Kyle Preston

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #  (6500 * 0.25) / 12 example calculation

    #variables
    costOfCar = float(0)

    insuranceCost = float(0)


    #input 
    gender= input("Are you 'Male' or 'Female': ")

    age = input("Enter your age: ")

    costOfCar = input("Enter the purchase price of the vehicle: ")


    #output


    if gender.capitalize() == "Male" :
        if float(age) < 15:
            print("Too young to drive")
        elif 15 < float(age) < 25:
            insuranceCost = float(costOfCar) *  0.25 / 12
        elif 25 < float(age) < 40:
            insuranceCost = float(costOfCar) * 0.17 / 12
        elif 40 < float(age) < 70:
            insuranceCost = float(costOfCar) * 0.10 / 12
        elif float(age) >= 70 :
            print("Too old to drive / No data")
    
    elif gender.capitalize() == "Female" :
        if float(age) < 15:
            print("Too young to drive")
        elif 15 < float(age) < 25:
            insuranceCost = float(costOfCar) * 0.20 / 12
        elif 25 < float(age) < 40:
            insuranceCost = float(costOfCar) * 0.15 / 12
        elif 40 < float(age) < 70:
            insuranceCost = float(costOfCar) * 0.10 / 12
        elif float(age) >= 70:
            print("Too old to drive / No data")


    #print

    print("Your monthly insurance will be ${0:.2f}".format(insuranceCost))













    # YOUR CODE ENDS HERE

main()