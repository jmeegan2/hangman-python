# Set the correct word and initialize the variables
word = "hangman"
guessed_letters = ""
hangman_parts = 0

# Keep asking for input until the user has guessed the correct word
while True:
  # Print the current state of the game
  for letter in word:
    if letter in guessed_letters:
      print(letter, end="")
    else:
      print("_", end="")
  print()

  # Ask the user for input
  guess = input("Enter a letter: ")

  # Check if the guess is correct and update the game state
  if guess in word:
    guessed_letters += guess
    if guessed_letters == word:
      print("Congratulations, you guessed the word!")
      break
  else:
    print("Sorry, that is not correct.")
    hangman_parts += 1

    # Display the hangman figure with an extra part added
    if hangman_parts == 1:
        print("   ____")

    if hangman_parts >= 2:
        print("   ____")
        print("  |    |")

    if hangman_parts >= 3:
        print("   ____")
        print("  |    |")
        print("  |    o")

    if hangman_parts >= 4:
        print("   ____")
        print("  |    |")
        print("  |    o")
        print("  |   /|\ ")

    if hangman_parts >= 5:
        print("   ____")
        print("  |    |")
        print("  |    o")
        print("  |   /|\ ")
        print("  |    |")

    if hangman_parts >= 6:
        print("   ____")
        print("  |    |")
        print("  |    o")
        print("  |   /|\ ")
        print("  |    |")
        print("  |   / \ ")
        
    if hangman_parts >= 7:
        print("   ____")
        print("  |    |")
        print("  |    o")
        print("  |   /|\ ")
        print("  |    |")
        print("  |   / \ ")
        print(" _|_")
        print("Sorry, you suck.")
        break

        