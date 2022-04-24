student_scores=input("Ïnput a list of student marks: ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)
large_max=0
for large in student_scores:
    print(large)
    if large>large_max:
        large_max=large
print("The highest number is ",large_max)
        
        
    
   
    
