import numpy as np

students=np.array(["shaurya","pranav","soham"])
subjects=np.array(["science","maths"])

marks=np.array([ 
    [99,95],
    [85,67],
    [89,50] 
])

for i in range(len(students)):
    print(students[i],":",marks[i])
    
print("\nShape(R,C):",marks.shape)

students_total=np.sum(marks,axis=1)
print(students_total)
subject_total = np.sum(marks,axis=0)
print("Subject Total :",subject_total)

subject_avg=np.mean(marks,axis=0)
print("subject_avg:",subject_avg)

student_avg=np.mean(marks,axis=1)
print("student_avg:",student_avg)

print("\n----Topper----")

top_index=np.argmax(students_total)
print("topper: ",students[top_index],"marks: ",marks[top_index])

print("\n----Subject analysis----")
weak_sub_index=np.argmin(subject_avg)
strong_sub_index=np.argmax(subject_avg)

print("weakest subject :",subjects[weak_sub_index])
print("strongest subject :",subjects[strong_sub_index])

print("\n----Result----")
result=np.where(marks>=40,"Pass","Fail")
for i in range(len(students)):
    print(students[i],":",result[i])

print("\n----Grade----")
for i in range(len(student_avg)):
    m=student_avg[i]
    if m>=90 and m<=100:
        Grade="A+"
    elif m>=80 and m<=89:
        Grade="A"  
    elif m>=70 and m<=79:
        Grade="B1"
    elif m>=60 and m<=69:
        Grade="B2"
    elif m>=50 and m<=59:
        Grade="C+"
    elif m>=40 and m<=49:
        Grade="C"
    else:
        Grade="F"   
    print(students[i],":",Grade)  

print("\n----Filtered Data----")
print("students scoring less than 70:")  
print(students[student_avg<70])

print("\n students scoring >80 in any subject:")
print(students[np.any(marks>80,axis=1)])

print("\n----Broadcasting for improved marks")
improvedMarks=marks+5
print(improvedMarks)

print("\n----Final Summary----")
print("overall avg:",np.mean(marks))
print("Highest marks:",np.max(marks))
print("Lowest marks:",np.min(marks))




