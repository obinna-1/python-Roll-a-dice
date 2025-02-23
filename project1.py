#print ('hello world')
#dice rolling game

import random

while True:
  choice = input ('Roll the dice ? (y/n): ').lower()
  if choice == 'y':
      diel1 = random.randint(1, 6)
      diel2 = random.randint(1, 6)
      print(f'({diel1}, {diel2})')
  elif choice == 'n':
      print('Thanks for playing!')    
      break
  else:
       print('Invalid choice!') 