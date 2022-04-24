from art import logo
print(logo)
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
      'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
      'v', 'w', 'x', 'y', 'z']

direction=input("Type 'encode' to encrypt ,type 'decode' to decrypt: ")

text=input("Type your message: ").lower()
shift=int(input("Type the shift number: \n"))

def ceasar(text_1,shift_1,direction_1):


            cipher=""
            for i in text_1:
                letter=alphabet.index(i)
                if direction_1=="encode":
                    new_position=letter + shift_1
                elif direction_1=="decode":
                    new_position=letter -shift_1 

                cipher+=alphabet[new_position]
                    
            print(f"Your {direction_1} message is {cipher}") 
            

ceasar(text_1=text,shift_1=shift,direction_1=direction)
        
            
   