print("                     ___    ")
print(" o__        o__     |   |\ ")
print("/|          /\      |   |X\ ")
print("/ > o        <\     |   |XX\ ")
print("Welcome to Soccer Match.")
print("Your mission is to shot a goal and make Madrid win the match.") 
print("Madrid: 2 / Barcelona: 2")
choice1 = input("You have the ball which side do you want to move? Type 'left' or 'right'.\n").lower()
if(choice1 == 'left'):
  print('Good you are moving towards the opposition.')
  
  choice2 = input('Now you will pass the ball or keep it to yourself ? Type "pass" to pass and "keep" to keep it.\n').lower()

  if(choice2 == 'pass'):
    print("Good now you have the ball again.\nNow you are in a good position to do a goal.")

    choice3 = input('At which area of the GoalPost do you want to Shoot? Type "left" for left, "right" for right and "center" for center\n').lower()
    if(choice3 == 'center'):
      print("Yes U did it. it's a GOAL You Won")
      print("Madrid: 3 / Barcelona: 2")
    else:
      print("Nooo..... GoalKeeper Saved it.\nNow oppositon did the Goal you lost the Game.")
      print("Madrid: 2 / Barcelona: 3")
  else:
    print("You are attacked by Opposition and you lost the ball")
    print("Madrid: 2 / Barcelona: 3")

else:
  print("No... Ball got lost by you and Opposition did a Goal.")
  print("Madrid: 2 / Barcelona: 3")
