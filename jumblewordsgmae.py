import random
def choose():
    words=['rainbow','computere','science','programming','mathmetics','player','condition','reverse','board','water']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,'your score is:',p1)
    print(p2n,'your score is:',p2)
    print('thankx for playing nobis game')

def play():
    p1name=input('player 1, please enter your name:')
    p2name=input('player 2 , please enter your name:')
    p1=0 # assign the point initial 0
    p2=0  # assign 2nd player point initial 0
    turn=0
    while(1):
        #computers part
        picked_word=choose()
        #create question
        qn=jumble(picked_word)
        print(qn)
        #for player 1
        if turn%2==0:
            print(p1name,'your turn')
            ans=input('what is my  mind?')
            if ans==picked_word:
                p1=p1+1
                print('your score is',p1)
            else:
                print('better luck next time:',picked_word)
                d=input('press 1 to continue else 0 to exit:')
                c=int(d)
                if c==0:
                    thank(p1name,p2name,p1,p2)
                    break
                 #for player 2
        else:
            print(p2name,'your turn')
            ans=input('what is my  mind?')
            if ans==picked_word:
                p2=p2+1
                print('your score is',p2)
            else:
                print('better luck next time:',picked_word)
                d=input('press 1 to continue else 0 to exit:')
                c=int(d)
                if c==0:
                    thank(p1name,p2name,p1,p2)
                    break
        turn=turn+1
        
play()
