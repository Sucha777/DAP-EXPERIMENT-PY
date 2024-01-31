Principle = int(input("Enter the principle amount :"))
Rate = int(input("Enter the rate of interest:"))
time = int(input("Enter time in years:"))

Amount = Principle * (pow((1 + Rate / 100), time))
compound_interest =(Amount - Principle)
print("The compound interest is:", compound_interest)