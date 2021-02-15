#get the variables and set the word that hat to be guessed
lifes=5
word=input('Please insert your word here: ')
tried=[]
guess=[]
#the programm is lower the case just to be sure that we enter the same type of characters later in 
#the programm we will do the same thing for the characters
try: 
    word=word.lower()
except:
    print('something went wrong')
for i in range(len(word)):
    if i==0:
        guess.append(word[0])
        tried.append(word[0])
    elif word[i]==word[0]:
        guess.append(word[0])
    else:
        guess.append('_')
#start an infinity loop that will stop when the list will be complete moment that will reaviel the word
#or when the player will be out of lifes
while True:
    if not '_' in guess:
        print('Congratulation you guessed the word')
        break
    else :
        print('You have ',lifes,'lifes left')
        print(guess)
        character=input('Enter a character: ').lower
        #we will see if the player tried this before and if so we will let him guess again
        if character in tried:
            print('you allready tried this')
        else:
            tried.append(character)
            if len(character)!=1:
                print('Just one character')
            else:
                #we will check if the character is in the word and if it is the pragramm will take every position and check if 
                #there shoud be that character. It will then continue just to be sure that this character isn't unique.
                #there are word like 'book' where 'o' is fond twice on position 1 and 2
                if character in word:
                    for i in range(1,len(word)):
                        if word[i]==character:
                            guess[i]=character
                else:
                    print('Wrong')
                    lifes-=1
    #at this moment if the player will be out of lifes it will be game over for him
    if lifes==0:
        print('GAME OVER')
        break