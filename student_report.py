'''Write a python program to dispaly the name marks and grade of students 
using list,function and a for loop'''

student = ["Jay","Rahul","Ram","Ritesh","Kajal"]
marks = [95,83,92,86,79]

def get_status(name,mark):
    if mark >=90:
        grade ="A"
    elif mark >=75:
        grade ="B" 
    else:
        grade ="C" 
    print("Name :",name)
    print("Marks :",mark)
    print("Grade :",grade)
    print("===============")

for i in range(len(student)):
    get_status(student[i],marks[i])