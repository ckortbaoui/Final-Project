# Chris Kortbaoui
# chris.kortbaoui@owl.ucc.edu
# May 16, 2017

'''
The name of this program is ZyBooks Chapter 5-8 Trivia Game.
The program consists of a main menu that will lead a user to either start the game or quit. 
If they choose to start the game, it leads them through a series of 20 multiple choice and true/false questions.
They will enter an answer and the program will store it into a list before moving on to another question.
Once they complete all 20 questions, it will retrieve their score and let them know what it is.  
'''
            
def study_question1():
    print('Question 1:')
    print('Complete the following loop expression - iterate until c is equals \'z\'.')
    print('HINT: do not confuse this expression with iterate while.')
    print('while ______:')
    print('    # Loop body statements go here')
    print('A. c == \'z\'')
    print('B. c <= \'z\'')
    print('C. c != \'z\'')
    print('D. None of the above.')
    answer1 = input('Please enter your answer:')
    user_answers.append(answer1.upper())
    

def study_question2():
    print('Question 2:')
    print('Use a for loop when the number of iterations is NOT computable before entering the loop.')
    print('Type T for True and F for False')
    answer2 = input('Please enter your answer:')
    user_answers.append(answer2.upper())
    

def study_question3():
    print('Question 3:')
    print('What is the simplest range() function that generates every integer from 0 to 500?')
    print('A. range(499)')
    print('B. range(501)')
    print('C. range(500)')
    print('D. None of the above.')
    answer3 = input('Please enter your answer:')
    user_answers.append(answer3.upper())
    

def study_question4():
    print('Question 4:')
    print('Use a while loop when the number of iterations is computable before entering the loop.')
    print('Type T for True and F for False')
    answer4 = input('Please enter your answer:')
    user_answers.append(answer4.upper())
    
        
def study_question5():
    print('Question 5:')
    print('Given the following Python code, how many times will the print statement execute?')
    print('for i in range(5):')
    print('    for j in range(10, 12):')
    print('        print(\'%%d%%d\' %% (i1, i2))')
    print('A. 5')
    print('B. 8')
    print('C. 2')
    print('D. 10')
    answer5 = input('Please enter your answer:')
    user_answers.append(answer5.upper())
    
    
def study_question6():
    print('Question 6:')
    print('What function creates a new rearranged container without modifying the original one?')
    print('A. sorted()')
    print('B. rearrange()')
    print('C. sort()')
    print('D. None of the above.')
    answer6 = input('Please enter your answer:')
    user_answers.append(answer6.upper())
    

def study_question7():
    print('Question 7:')
    print('A view object provides read-only access to dictionary keys and values.')
    print('Type T for True and F for False')
    answer7 = input('Please enter your answer:')
    user_answers.append(answer7.upper())
    
    
def study_question8():
    print('Question 8:')
    print('What is the term for when a dictionary contains another dictionary as a value?')
    print('A. dictionary')
    print('B. nested dictionary')
    print('C. tuple')
    print('D. array')
    answer8 = input('Please enter your answer:')
    user_answers.append(answer8.upper())
    
    
def study_question9():
    print('Question 9:')
    print('A ___________ is a method of organizing data in a logical and coherent fashion.')
    print('A. list')
    print('B. dictionary')
    print('C. data structure')
    print('D. loop')
    answer9 = input('Please enter your answer:')
    user_answers.append(answer9.upper())
    
    
def study_question10():
    print('Question 10:')
    print('You can only have up to three levels of nested dictionaries.')
    print('Type T for True and F for False')
    answer10 = input('Please enter your answer:')
    user_answers.append(answer10.upper())
    
    
def study_question11():
    print('Question 11:')
    print('Which if these is a reason for defining and utilizing new functions in a program.')
    print('A. improve program readability')
    print('B. encourage modular program development')
    print('C. reduce redundant code')
    print('D. All of the above')
    answer11 = input('Please enter your answer:')
    user_answers.append(answer11.upper())
        
    
def study_question12():
    print('Question 12:')
    print('According to a concept called _________. The behavior of a function depends on the argument types.')
    print('A. polymorphism')
    print('B. duck typing')
    print('C. hierarchical function calls')
    print('D. static typing')
    answer12 = input('Please enter your answer:')
    user_answers.append(answer12.upper())
       
    
def study_question13():
    print('Question 13:')
    print('What is an argument as it pertains to functions?')
    print('A. The result of of a function after it has been executed.')
    print('B. The value passed to a function\'s parameter.')
    print('C. A named series of statements.')
    print('D. A value stored in a dictionary.')
    answer13 = input('Please enter your answer:')
    user_answers.append(answer13.upper())
       

def study_question14():
    print('Question 14:')
    print('A local variable is one defined inside a function.')
    print('Type T for True and F for False')
    answer14 = input('Please enter your answer:')
    user_answers.append(answer14.upper())
       
    
def study_question15():
    print('Question 15:')
    print('What causes execution to jump back to where the original function call occurred?')
    print('A. Dynamic typing')
    print('B. A function\'s return')
    print('C. A parameter of a function')
    print('D. A function call')
    answer15 = input('Please enter your answer:')
    user_answers.append(answer15.upper())
    
    
def study_question16():
    print('Question 16:')
    print('What is the correct way to write the definition of an __init__ method that requires the parameters x and y.')
    print('A. def __init__(x, y) ')
    print('B. def __init__(self) ')
    print('C. def __init__(self, x, y)')
    print('D. class __init__(self, x, y) ')
    answer16 = input('Please enter your answer:')
    user_answers.append(answer16.upper())
      
    
    
def study_question17():
    print('Question 17:')
    print('A class interface should be the only necessary way to interact with a class instance.')
    print('Type T for True and F for False')
    answer17 = input('Please enter your answer:')
    user_answers.append(answer17.upper())
    
    
def study_question18():
    print('Question 18:')
    print('A _________ is responsible for setting up the initial state of the new instance of a class.')
    print('A. method')
    print('B. dot operator')
    print('C. attribute')
    print('D. constructor')
    answer18 = input('Please enter your answer:')
    user_answers.append(answer18.upper())
           
    
def study_question19():
    print('Question 19:')
    print('Internal methods used by a class should start with an underscore in their name.')
    print('Type T for True and F for False')
    answer19 = input('Please enter your answer:')
    user_answers.append(answer19.upper())
    
    
def study_question20():
    print('Question 20:')
    print('Pick the statement that creates an instance of the class Animal named "cat".')
    print('A. cat = Animal()')
    print('B. Animal(cat)')
    print('C. cat.Animal()')
    print('D. Animal = cat')
    answer20 = input('Please enter your answer:')
    user_answers.append(answer20.upper())
     

def calculate_score():
    user_score = 0
    for i in range(len(user_answers)):
        if user_answers[i] == answer_key[i]:
            user_score += 1
        else:
            continue
    return user_score

def main_menu(usrstart):
    menuOp = ' '
    print('Welcome to the CST161 Semester Exam 2 Trivia Game!')
    print('It is intended to help you study for our exam regarding Chapters 5,6,7, and 8 in Zybooks.')
    print('It has a total of 20 questions - 5 from each chapter.')
    print('MENU:')
    print('b - Begin Game')
    print('q - Quit Game')
    
    while menuOp != 'b' and menuOp != 'q':
        menuOp = input('Please select an option:\n')
        
        if menuOp == 'b':            
            study_question1()
            study_question2()
            study_question3()
            study_question4()
            study_question5()
            study_question6()
            study_question7()
            study_question8()
            study_question9()
            study_question10()
            study_question11()
            study_question12()
            study_question13()
            study_question14()
            study_question15()
            study_question16()
            study_question17()
            study_question18()
            study_question19()
            study_question20()
            calculate_score()            
            
        
        return menuOp


if __name__ == '__main__':
    user_answers = []
    answer_key = ['C','F','B','F','D','A','T','B','C','F','D','A','B','T','B','C','T','D','T','A']
    usrstart = ' '
    main_menu(usrstart)
    print('Thank you for playing!')
    print('Your score is: %d out of 20.' % calculate_score())
    print("\nFinal Programming Project by Chris Kortbaoui on May 16, 2017\n")
    pause=input('\nPress the Enter key to continue')