


row1=["😀","😀","😀"]
row2=["😀","😀","😀"]
row3=["😀","😀","😀"]
map=[row1,row2,row3]
print(map)
print(len(map))
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to the treasure? ")

str_position=(position)

column=int(position[1])
row=int(position[0])

map[column-1][row-1]="Z"

print(f"{row1}\n{row2}\n,{row3}")
