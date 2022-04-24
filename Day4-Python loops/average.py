
student_height=(input("Input a list of student heights: ").split())
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
    
#print(student_height)     
t_height=0
for height in student_height:
    t_height+=height  

total_1=0     
for total in student_height:
    total_1+=1
av_height=round(t_height/total_1)

print("The average height is, ",av_height)

