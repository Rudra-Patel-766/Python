import random

Question = ["Who was the first woman to win a Nobel Prize?","Who wrote the famous book 'The God of Small Things'?","In which year did India win its first Cricket World Cup?"]

que = random.choice(Question)
print(que)
if que=="Who was the first woman to win a Nobel Prize?":
    a = "a.Indira Gandhi"
    b = "b.Marie Curie"
    c = "c.Toni Morrison"
    d = "d.Alice Munro"
    print(a,b,c,d)
    e = input("Choose from a,b,c,d: ")
    if e=="b":
        print("You Won 5,000 Rupees")
    else:
        print("You have lost a money")
elif que=="Who wrote the famous book 'The God of Small Things'?":
    a = "a.J.K. Rowling"
    b = "b.Arundhati Roy"
    c = "c.George Orwell"
    d = "d.Chimamanda Ngozi Adichie"
    print(a,b,c,d)
    e = input("Choose from a,b,c,d: ")
    if e=="b":
        print("You Won 50,000 Rupees")
    else:
        print("You have lost a money")
elif que=="In which year did India win its first Cricket World Cup?":
    a = "a.1983"
    b = "b.1996"
    c = "c.2011"
    d = "d.2023"
    print(a,b,c,d)
    e = input("Choose from a,b,c,d: ")
    if e=="a":
        print("You Won 1,00,000 Rupees")
    else:
        print("You have lost a money")
    
            
        
        


 
