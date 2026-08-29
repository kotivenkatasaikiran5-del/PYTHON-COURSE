questions=(("what is the sum of 3+5 ?"),
           ("what is the mul of 8*9 ?"),
           ("who is director of bahubali ?"),
           ("who is CM of chennai ?"))
options=(("A:9","B:10","C:8","D:90"),
         ("A:23","B:72","C:8","D:328"),
         ("A:Rajmouli","B:Trivi","C:prashan","D:kvsk"),
         ("A:hero","B:nani","C:vijay","D:koti"))
answers=(("C"),("B"),("A"),("C"))
guesses=[]
score=0
question_num=0
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter u r guess")
    guesses.append(guess)
    if guesses==answers[question_num]:
        score+=1
        print("correct")
    else:    
        print("wrong")
        print(f"{answers[question_num]} is correct answer")
        question_num+=1


#hello
