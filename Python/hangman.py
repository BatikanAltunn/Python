import random
import time

name = input("What is your name? : ")
print ("Hello, " + name, "Time to play hangman!")
print ("_")
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)

def selectWord():
    
    words =["lion","computer","essex","colchester"]
    myword = random.choice(words)
    
    return myword


def hangMan():
  guesses = 0
  word = selectWord()
  word_list = list(word)
  blanks = "_"*len(word)
  length_word = len(word)
  blanks_list = list(blanks)
  new_blanks_list = list(blanks)
  guess_list = []
  
  print ("Let's play hangman!\n")
  print("Ok, so the word You need to guess has", length_word, "characters")
  print("Be aware that You can enter only 1 letter from a-z\n\n")
  print ("\n")
  print ("" + ' '.join(blanks_list))
  print ("\n")
  print ("Guess a letter.\n")
  turns = 10

  while guesses < 6:
  
        guess = str(input("> "))
        guess = guess.lower()
        
        if len(guess) > 1:
                print ("Stop cheating! Enter one letter at time.")
        elif guess == "":
                print ("Don't you want to play? Enter one letter at a time.")
        elif guess in guess_list:
                print ("You already guessed that letter! Here is what you've guessed:")
                print (' '.join(guess_list))
        else:
                guess_list.append(guess)
                i = 0
                while i < len(word):
                        if guess == word[i]:
                                new_blanks_list[i] = word_list[i]
                        i = i+1
  
                if new_blanks_list == blanks_list:
                        print ("Your letter isn't here.")
                        
                        turns -= 1
                        print ("You have", + turns, 'more guesses')
                        if turns == 0:
                          print ("You Lose")
                          break
                        
                        
                        if guesses < 6:
                                print ("Guess again.")
                                print (' '.join(blanks_list))
                        
                elif word_list != blanks_list:
                        
                        blanks_list = new_blanks_list[:]
                        print (' '.join(blanks_list))
                        
                        if word_list == blanks_list:
                          print ("\nYOU HAVE WON!")
                          print ("\n")
                          print ("Would you like to play again?")
                          print ("Type 1 for yes or 2 for no.")
                          again = str(input("> "))
                          if again == "1":
                            hangMan()
                          
                          else:
                            print("Thank You")
                        
                        else:
                                print ("Great guess! Guess another!")
hangMan()
