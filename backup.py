import mysql.connector

con = mysql.connector.connect (
    host="project.ccbr0xymap3c.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="admin123",
    database="student_db",
    auth_plugin='mysql_native_password'
)

attendance = ["tend", "att", "tnd", "ted", "nce"]
maths = ["mat", "ath"]
english = ["eng", "lish"]
gpa = ["gpa", "gap", "gps"]
total = ["tot", "tal"]

cursor = con.cursor() 

def get_score(score, adm):
    sql = f"SELECT {score} FROM student_performance WHERE Admission_number = {adm}"
    cursor.execute(sql)
    return cursor.fetchall()

def get_name(adm):
    sql = "SELECT f_name FROM student_data WHERE Admission_number = {}".format(adm)
    cursor.execute(sql)
    return cursor.fetchall()

def get_result(list_name):
    for i in list_name:
        if question.find(i) != -1:
            return True

    return False



adm = input("What is your admission number?\n").split()

for i in adm:
    try:
        num = str(int(i))
    except:
        continue

try:
    sql = "SELECT passwd FROM student_data WHERE Admission_number = {}".format(num)
    cursor.execute(sql)
    passwd = (cursor.fetchall()[0])[0]

    pas = input("\nWhat is your password?\n")
    name = get_name(num)[0][0]
    counter = 0 

    while pas == passwd:
        found = False
        if counter == 0:
            print("\nHi", name, "What would you like to know?")
        else:
            print("\nWhat else would you like to know?")
            
        question = input().lower()

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
        
        if question.find("no") != -1:
            print("Ok. Have a wonderful day!")
            break
        
        if found==False:
            print("Sorry, I am unable to help you with that.")


        counter += 1
    else:
        print("\nIncorrect Password")

except:
    print("\nIncorrect admission number")
