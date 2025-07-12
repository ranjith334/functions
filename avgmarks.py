subject_marks=[]
def add_subject_marks():
    global total
    mark=int(input("enter marks of a subject:   "))
    subject_marks.append(mark)
    
    return mark
print("subject1 marks: ",add_subject_marks())
print("subject2 marks: ",add_subject_marks())
print("subject3 marks: ",add_subject_marks())
print("All subject marks")
print("total marks stored in global",add_subject_marks())
total=sum(subject_marks)
l=len(subject_marks)
avg=total/1
print("total marks",total)
print("Total marks",total)
print("average",avg)


