import random
import string
def game():
    symbols=[]
    symbols=list(string.ascii_letters)
    card1=[0]*5
    card2=[0]*5
    pos1=random.randint(0,5)
    pos2=random.randint(0,5)
    print(pos1)
    print(pos2)
    #pos1 and pos2 are same symbol position in card1 and card2
    samesymbol=random.choice(symbols)
    symbols.remove(samesymbol)
    if (pos1==pos2):
        card2[pos1]=samesymbol
        card1[pos1]=samesymbol
    else:
        card1[pos1]=samesymbol
        card2[pos2]=samesymbol
        card1[pos2]=random.choice(symbols)
        symbols.remove(card1[pos2])
        card2[pos1]=random.choice(symbols)
        symbols.remove(card2[pos1])
    i=0
    while(i<5):
        if(i!=pos1 and i!=pos2):
            alpha=random.choice(symbols)
            symbols.remove(alpha)
            alpha2=random.choice(symbols)
            symbols.remove(alpha2)
            card1[i]=alpha
            card2[i]=alpha2
        i=i+1
    print(card1)
    print(card2)
    ch=input("spot the similiar symbol:")
    if(ch==samesymbol):
        print("right")
    else:
        print("wrong answer!")
game()
