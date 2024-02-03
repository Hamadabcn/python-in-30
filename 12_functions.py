def showMessage(message):
    print("The message")
    print(message)
    print("Done")

def calculateSalary(bonus = 50, deduction = 0):
    return 5000 + bonus - deduction

employee1 = calculateSalary()
employee2 = calculateSalary()
employee3 = calculateSalary()

print(employee1, employee2, employee3)
showMessage("Here are your salaries")
