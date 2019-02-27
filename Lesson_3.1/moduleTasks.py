# csvTo2DList(filename) #this function will read in a csv and return the csv as a 2D list with no newline characters.
# Test it with the studentInfo.txt file
# specialInput() #this function will ask for the first name to be checked for and will return is as a string
# listQuery(data, fName) #this function will return a list of student data that matches the fName input
# (Optional) printClean(newData) #this function prints a clean table of your newData list


def csvTo2DList(filename):
    file_opening = open(str(filename), "r")
    data = [j.split(",") for j in file_opening.read().split()]
    return data


def specialInput():
    fName = input("First Name: ")
    return fName


def listQuery(data, fName):
    for r in range(len(data)):
        if fName.title() in data[r]:
            newData = data[r]
            return newData


def printClean(newData):
    final_list = []
    try:
        for x in range(len(newData)):
            final_list.append(newData[x])
    except:
        return "Can't"
    return final_list


def printClean_P2(final_list):
    if final_list == "Can't":
        print("Cannot be done.")
    else:
        for x in final_list:
            print(x)
