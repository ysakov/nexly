def number_guesser():
    import random
    randomly_selected_number = random.randint(1, 50) 
    user_entered_number = 0
    while randomly_selected_number != user_entered_number:
        user_entered_number =  int(input ("enter number : "))
        if user_entered_number==randomly_selected_number:
            print("CORRECT")
        if randomly_selected_number >user_entered_number:
            print("too low , enter another number ")
        elif randomly_selected_number <user_entered_number:
            print("too high ,enter another number ")
        
        
number_guesser()

        