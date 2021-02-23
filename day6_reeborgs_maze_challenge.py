#This challenge was aimed at learning the use of while loops

#Reeborg's world was used to practice while loos

#The maze project link can be found here --> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

#My solution to the maze challenge👇

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
while not at_goal():
      if right_is_clear():
            turn_right()
            move()
      elif front_is_clear():
        move()
      else:
        turn_left()
            
