def AgeConvert(dob):
    dob = dob.split("-")
    age = 2019 - int(dob[2])
    if int(dob[1])>6:
        age = age - 1
    print("Age :",age)
AgeConvert(str(input("Enter the dob :")))
#Age format : DD-MM-YYYY
