import random

wordlist = ["cat", "dog", "rabbit", "mouse", "wolf", "horse", "dragon", "unicorn", "snake", "bird", "swan", "crow", "lion", "elephant", "flog", "cow", "pig", "jiraffe", "flamingo","human"]
word = random.choice(wordlist)  # The answer is decided randomly here.

def hangman(word):
    """
    Let's Play "Hangman Game". (If you don't play, I will kill you... Just kidding! Forget it!)
    :param word: string, the answer of this game.
    :print: You win or lose.
    Please enjoy!
    """
    wrong = 0
    stages = [ "",
               "_______     ",
               "|           ",
               "|      |    ",
               "|      0    ",
              r"|     /|\   ",
              r"|     / \   ",
               "|           "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman Game!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Predict a letter----→ "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win... Maybe, are you genius than I think?????")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! Answer is {} ! Hahahahaha!!!!!".format(word))


hangman(word)