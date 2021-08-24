#https://selftaught.blog/python-tutorial-build-hangman/

def hangman(word): 
  wrong = 0
  stages = ["", "____________ ", "| ", "| | ", "| 0 ", "| /|\ ", "| / \ ", "|  "]
  rletters = list(word)
  board = ["_"] * len(word)
  win = False
  print("Welcome to HANGMAN!")
