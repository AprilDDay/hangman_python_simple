#https://selftaught.blog/python-tutorial-build-hangman/

def hangman(word): 
  wrong = 0
  stages = ["", "__________ ", "| ", "| | ", "| 0 ", "| /|\ ", "| / \ ", "|  "]
  rletters = list(word)
  board = ["_"] * len(word)
  win = False
  print("Welcome to HANGMAN!")

 while wrong < len(stages)-1:
  print("\n")
  msg = "Guess a letter in the word..." 
  char = input(msg)
  if char in rletters: 
    cind = rletters \ .index(char)
    board[cind] = char 
    #rletters[cind] = 
  
  #need to put if win
  
  if not win: 
    print("\n" .join(stages[0: \ wrong]))
    print("Oh no! You lost! It was {}.".format(word))
    
 
