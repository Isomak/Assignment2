# Michael Maniatis
# 100876436

digit = int(input("Please Enter A Number Between 0 and 1000: "))
if digit == 1000:
    print("The Digit Sum of the number 1000 is 1")   #This Is Just Used Because I didnt set up my code correctly, so you couldnt type 1000 without a logic error happening
elif digit >= 0 and digit <= 1000:
    extractdigit = (digit % 10)
    extractseconddigit = ((digit % 100) // 10)   # This is kind of a mess but basically it just grabs the first, second and third number from the number you input. 
    extractthirddigit = ((digit // 10) // 10)
    print("The Digit Sum of the number", digit, "is", extractdigit + extractseconddigit + extractthirddigit)
else:
    print("that is not a valid number")