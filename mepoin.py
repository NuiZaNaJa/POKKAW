import random

L = random.randint(1,4)
L2 = random.randint(1,4)
K = random.randint(1,3)
K2 = random.randint(1,3)
Pi1 = random.randint(1,12)
Pi2 = random.randint(1,12)

PiBot1 = random.randint(1,12)
PiBot2 = random.randint(1,12)
LBot = random.randint(1,4)
L2Bot = random.randint(1,4)

if L == 1:
    LE= "♠"
elif L == 2:
    LE= "♥"
elif L == 3:
    LE= "♣"
elif L == 4:
    LE= "♦"
if L2 == 1:
    LE2= "♠"
elif L2 == 2:
    LE2= "♥"
elif L2 == 3:
    LE2= "♣"
elif L2 == 4:
    LE2= "♦"


if Pi1 == 10:
    Pi1E = "Jack"
    Pi1 = 0
elif Pi1 == 11:
    Pi1E = "Queen"
    Pi1 = 0
elif Pi1 == 12:
    Pi1E = "King"
    Pi1 = 0

if Pi2 == 10:
    Pi2E = "Jack"
    Pi2 = 0
elif Pi2 == 11:
    Pi2E = "Queen"
    Pi2 = 0
elif Pi2 == 12:
    Pi2E = "King"
    Pi2 = 0
if LBot == 1:
    PiBot1E= "♠"
elif LBot == 2:
    PiBot1E= "♥"
elif LBot == 3:
    PiBot1E= "♣"
elif LBot == 4:
    PiBot1E= "♦"
if L2Bot == 1:
    PiBot2E= "♠"
elif L2Bot == 2:
    PiBot2E= "♥"
elif L2Bot == 3:
    PiBot2E= "♣"
elif L2Bot == 4:
    PiBot2E= "♦"


if PiBot1 == 10:
    PiBot1LE = "Jack"
    PiBot1 = 0
elif PiBot1 == 11:
    PiBot1LE = "Queen"
    PiBot1 = 0
elif PiBot1 == 12:
    PiBot1LE = "King"
    PiBot1 = 0

if PiBot2 == 10:
    PiBot2LE = "Jack"
    PiBot2 = 0
elif PiBot2 == 11:
    PiBot2LE = "Queen"
    PiBot2 = 0
elif PiBot2 == 12:
    PiBot2LE = "King"
    PiBot2 = 0

Yourpoin = Pi1 + Pi2
Botpoin = PiBot1 + PiBot2

if PiBot1 < 10 and PiBot1 > 0 and PiBot2 < 10 and PiBot2 > 0:
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = BotpoinF - 10
elif PiBot1 < 10 and PiBot1 > 0 and PiBot2LE == "Jack":
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = BotpoinF - 10
elif PiBot1 < 10 and PiBot1 > 0 and PiBot2LE == "Queen":
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = BotpoinF - 10
elif PiBot1 < 10 and PiBot1 > 0 and PiBot2LE == "King":
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = BotpoinF - 10
elif PiBot1LE == "Jack" and PiBot2 < 10 and PiBot2 > 0:
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = Botpoin - 10
elif PiBot1LE == "Queen" and PiBot2 < 10 and PiBot2 > 0:
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = BotpoinF - 10
elif PiBot1LE == "King" and PiBot2 < 10 and PiBot2 > 0:
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = BotpoinF - 10
elif PiBot1LE == "Jack" and PiBot2LE == "Jack":
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = BotpoinF - 10
elif PiBot1LE == "Jack" and PiBot2LE == "Queen":
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = BotpoinF - 10
elif PiBot1LE == "Jack" and PiBot2LE == "King":
    BotpoinF = Botpoin
    if BotpoinF >= 10:
        BotpoinF = BotpoinF - 10

if Pi1 < 10 and Pi1 > 0 and Pi2 < 10 and Pi2 > 0:
    print ("Your card is:", Pi1, LE)
    print ("Your card is:", Pi2, LE2)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
elif Pi1 < 10 and Pi1 > 0 and Pi2E == "Jack":
    print ("Your card is:", Pi1, LE)
    print ("Your card is:", Pi2E)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
elif Pi1 < 10 and Pi1 > 0 and Pi2E == "Queen":
    print ("Your card is:", Pi1, LE)
    print ("Your card is:", Pi2E)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
elif Pi1 < 10 and Pi1 > 0 and Pi2E == "King":
    print ("Your card is:", Pi1, LE)
    print ("Your card is:", Pi2E)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
elif Pi1E == "Jack" and Pi2 < 10 and Pi2 > 0:
    print ("Your card is:", Pi1E, LE)
    print ("Your card is:", Pi2)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
elif Pi1E == "Queen" and Pi2 < 10 and Pi2 > 0:
    print ("Your card is:", Pi1E, LE)
    print ("Your card is:", Pi2)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
elif Pi1E == "King" and Pi2 < 10 and Pi2 > 0:
    print ("Your card is:", Pi1E, LE)
    print ("Your card is:", Pi2)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
elif Pi1E == "Jack" and Pi2E == "Jack":
    print ("Your card is:", Pi1E)
    print ("Your card is:", Pi2E)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
elif Pi1E == "Jack" and Pi2E == "Queen":
    print ("Your card is:", Pi1E)
    print ("Your card is:", Pi2E)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
elif Pi1E == "Jack" and Pi2E == "King":
    print ("Your card is:", Pi1E)
    print ("Your card is:", Pi2E)
    Yourpoin = Yourpoin
    if Yourpoin >= 10:
        Yourpoin = Yourpoin - 10
        print ("Your poin is:", Yourpoin)
    else:
        print ("Your point is:", Yourpoin)
Question = input("Do you want to continue? (Y/N)")
if Question == "y":
    J = random.randint(1,12)
    J2 = random.randint(1,4)
    if J2 == 1:
        JE= "♠"
    elif J2 == 2:
        JE= "♥"
    elif J2 == 3:
        JE= "♣"
    elif J2 == 4:
        JE= "♦"
    if J == 10:
        J1E = "Jack"
        J = 0
    elif J == 11:
        J1E = "Queen"
        J = 0
    elif J == 12:
        J1E = "King"
        J = 0
    if J < 10 and J > 0:
        print ("Your card is:", J, JE)
        Yourpoin = Yourpoin + J
        if Yourpoin >= 10:
            Yourpoin = Yourpoin - 10
            if Yourpoin > BotpoinF:
                print ("Your poin is:", Yourpoin)
                if Yourpoin > BotpoinF:
                    print("You win!")
                elif Yourpoin < BotpoinF:
                    print("You lose")
                else:
                    print("Draw!")
        else:
            print ("Your point is:", Yourpoin)
            if Yourpoin > BotpoinF:
                print("You win!")
            elif Yourpoin < BotpoinF:
                print("You lose")
            else:
                print("Draw!")
    elif J1E == "Jack":
        print ("Your card is:", J1E)
        Yourpoin = Yourpoin + J
        if Yourpoin >= 10:
            Yourpoin = Yourpoin - 10
            print ("Your poin is:", Yourpoin)
            if Yourpoin > BotpoinF:
                print("You win!")
            elif Yourpoin < BotpoinF:
                print("You lose")
            else:
                print("Draw!")
        else:
            print ("Your point is:", Yourpoin)
            if Yourpoin > BotpoinF:
                print("You win!")
            elif Yourpoin < BotpoinF:
                print("You lose")
            else:
                print("Draw!")
    elif J1E == "Queen":
        print ("Your card is:", J1E)
        Yourpoin = Yourpoin + J
        if Yourpoin >= 10:
            Yourpoin = Yourpoin - 10
            print ("Your poin is:", Yourpoin)
            if Yourpoin > BotpoinF:
                print("You win!")
            elif Yourpoin < BotpoinF:
                print("You lose")
            else:
                print("Draw!")
        else:
            print ("Your point is:", Yourpoin)
            if Yourpoin > BotpoinF:
                print("You win!")
            elif Yourpoin < BotpoinF:
                print("You lose")
            else:
                print("Draw!")
    elif J1E == "King":
        print ("Your card is:", J1E)
        Yourpoin = Yourpoin + J
        if Yourpoin >= 10:
            Yourpoin = Yourpoin - 10
            print ("Your poin is:", Yourpoin)
            if Yourpoin > BotpoinF:
                print("You win!")
            elif Yourpoin < BotpoinF:
                print("You lose")
            else:
                print("Draw!")
        else:
            print ("Your point is:", Yourpoin)
            if Yourpoin > BotpoinF:
                print("You win!")
            elif Yourpoin < BotpoinF:
                print("You lose")
            else:
                print("Draw!")
elif Question == "n":
    if Yourpoin > BotpoinF:
        print("You win!")
    elif Yourpoin < BotpoinF:
        print("You lose")
    else:
        print("Draw!")
print("Bot point is:", BotpoinF)