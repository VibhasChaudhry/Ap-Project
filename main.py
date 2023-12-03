import mysql.connector #Importing the python-mysql connector.

#Establishing connection between mysql(AWS RDS) and pyhon using the connector.
con = mysql.connector.connect (
    host="project.ccbr0xymap3c.ap-south-1.rds.amazonaws.com", #Host-Name(AWS RDS)
    user="admin",
    password="admin123",
    database="student_db", #Database-name
    auth_plugin='mysql_native_password' #Required for Authentication
)

#Making Lists which will help the computer identify spelling errors in the input
attendance = ["tend", "att", "tnd", "ted", "nce"]
maths = ["mat", "ath"]
english = ["eng", "lish"]
gpa = ["gpa", "gap", "gps"]
total = ["tot", "tal"]

cursor = con.cursor() 

#Function to get the information from the database
def get_score(score, adm):
    sql = f"SELECT {score} FROM student_performance WHERE Admission_number = {adm}"
    cursor.execute(sql)
    return cursor.fetchall()

#Function to get the name of the user based on admission number
def get_name(adm):
    sql = "SELECT f_name FROM student_data WHERE Admission_number = {}".format(adm)
    cursor.execute(sql)
    return cursor.fetchall()

#Function to check if user has asked for a specefic score or not
def get_result(list_name):
    for i in list_name:
        if question.find(i) != -1:
            return True

    return False


#Asking user for admission number. Adding each word in input as an item in a list 'adm' using .split() 
# For Example, if input is "My admission number is 3" Then adm = ["My","admission","number","is","3"]

adm = input("What is your admission number?\n").split()

#Searching for admission no. in adm by checking which value in adm can be converted into an integer
for i in adm:
    try:
        num = str(int(i))
    except:
        continue

try:
    #Taking password (based on admission no provided) from mysql and putting the value in variable 'passwd'
    sql = "SELECT passwd FROM student_data WHERE Admission_number = {}".format(num)
    cursor.execute(sql)
    passwd = (cursor.fetchall()[0])[0]

    #Asking user for password
    pas = input("\nWhat is your password?\n")
    name = get_name(num)[0][0]
    counter = 0 

    #While Loop - Runs if inputted password = Password in database
    while pas == passwd:

        found = False #Used again later

        if counter == 0:
            print("\nHi", name, "What would you like to know?") #Printed if iteration is being run for first time
        else:
            print("\nWhat else would you like to know?") #Printed if iteration is not being run for first time
            
        question = input().lower() #Converts input to lower case


        #Conditional statements to check what the user is asking for (attendance, maths score, eng score etc) with the help of the function 'get_result'
        if get_result(attendance) == True:
            result = get_score("attendance", num)
            print("Your attendance is",result[0][0],"%")
            found = True
        
        if get_result(maths) == True:
            result = get_score("maths_score", num)
            print("Your Mathematics score is",result[0][0])
            found = True

        if get_result(english) == True:
            result = get_score("english_score", num)
            print("Your English score is",result[0][0])
            found = True
        
        if get_result(gpa) == True:
            result = get_score("gpa", num)
            print("Your GPA is",result[0][0])
            found = True

        if get_result(total) == True:
            result1 = get_score("maths_score", num)
            result2 = get_score("english_score", num)
            print("Your total score is ",result1[0][0] + result2[0][0])
            found = True
        
        #Checking if inputted value contains 'no' in it and breaking out of the loop if it does
        if question.find("no") != -1:
            print("Ok. Have a wonderful day!")
            break
        
        #Found remains false if all the conditional statements above were ignored (none of them were run).
        if found==False:
            print("Sorry, I am unable to help you with that.")


        counter += 1 #Incrementing counter
    else:
        print("\nIncorrect Password") #Printed if inputted password does not match password in database

except:
    #If error is thrown, it means admission number is incorrect
    print("\nIncorrect admission number")
