numberOfSlots = input('Enter the number of slots: ')
print(numberOfSlots)

lot = [{} for i in range(0, numberOfSlots)]

lot[3]["kl01"] = "red"
lot[7]["kl02"] = "red"
temp = []

# print(lot[i])


def getCarWithColor(x, lot, temp):
    for i, j in enumerate(lot):
        for k, v in j.items():
            if(v == x):
                var = str(i) + " " + k + " " + x
                temp.append(var)
    print(temp)


inputColor = input('Enter the color: ')
getCarWithColor(str(inputColor), lot, temp)
