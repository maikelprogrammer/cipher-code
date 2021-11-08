print("HEY WELCOME TO CEASER CHIPER")
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def final(text,shift,direction):
  chiper=""
  for letter in text:
    if letter in alphabets:
     position=alphabets.index(letter)
     if direction=="encode":
      new_position=position+shift
     elif direction=="decode":
      new_position=position-shift
     new_letter=alphabets[new_position]
     chiper+=new_letter
    else:
      chiper+=letter
  print(f"you {direction} is {chiper}")
final_code=True
while final_code:
  direction=input("type 'encode' for encrypt and 'decode' for decrypt\n")
  text=input("type your message\n")
  shift=int(input("enter your shift amount\n"))
  shift=shift%26
  final(text,shift,direction)
  a=input("type 'yes' for run again or type 'no' for stop \n")
  if a=="no":
    final_code=False
    print("goodbye")
  


