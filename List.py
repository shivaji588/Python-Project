#List - one variable with multipal vslues
students = ["Dipak","Kartik","Tanamay","Ram","Shivam"]
print(students)
print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4])

#Loops = to print all th elements of list
for student in students:
    print("Hello",student,"! Welcom to the class")



marks_list = [50,64,54,89,45,15]

for marks in marks_list:
    if marks >=90:
        print("Excelent you scored ",marks)
    elif marks >=80:
        print("Good Job you scored ",marks)
    else:
        print("Keep trying you scored ",marks)


name = "Yogita"
print(f"Hello {name}")


#range
for i in range(len(marks_list)):
    print(f"line number : {i}")


for i in range(5):
    print(f" number = {i}")


for i in range(1,6):
    print(f"Student number {i}")



#Define Function
def greet(name):
    print(f"Hello , {name} ! Welcome to the progrsmming world.")

greet("samarth")
greet("yogita")
greet("dipak")

#call the function
#print(greet("Sakshi"))

#list,for loop,function
studentss=["kajal","ram","kartik","jayram","kamal"]
def disp(studentss):
    print(f"Hello ,{studentss}")

for stud in studentss:
    disp(stud)