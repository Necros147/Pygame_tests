# ~ # Jasper Keller-Heikkila, 8/31
# ~ #Conversation with Raspberry pi
import math, random, cmath, turtle

def hangman_wins():
    global fails
    print('You Win!')
    if fails == 1:
        print('The hangman had a head')
    elif fails == 2:
        print('The hangman had a head and a body')
    elif fails == 3:
        print('The hangman had a head, a body, and 1 arm')
    elif fails == 4:
        print('The hangman had a head, a body, and 2 arms')
    elif fails == 5:
        print('The hangman had a head, a body, 2 arms, and a leg')
    else:
        print("You didn't make a single mistake, congradulations")
    print('The word was', ''.join(blnk))
    fails = 6
    done = input('Are you finished?y/n ')  

done = 'n'
ethics = [
    'taking jobs', 
    'take over world'
    ]
hmw = [
    'europe', 
    'spatula', 
    'pithy', 
    'beautiful', 
    'lathery', 
    'lawyers', 
    'vicious', 
    'facility', 
    'favorable', 
    'flavor', 
    'needle', 
    'biological', 
    'five'
    ]
    
print('Hello, my name is HAL')
print()
name = input('What is your name? ')
name = name.title()
topics = [
    'Ethical Dilemma of AI', 
    'Math', 
    'Binary Converter', 
    'Number Guessing', 
    'or Hangman'
    ]
print(', '.join(topics))
print(name, end = ', ')
topic = input('what would you like to do? ')
topic = topic.lower()

#Math
if topic == 'math':
 while done == 'n':

     #Math
        print('(+, -, *, /, pyth, quad, slope form)')
        operation = input('What math do you want to do? ')
        operation = operation.lower()

    #Addition
        if operation == '+':
            a = eval(input('please enter your first number: '))
            b = eval(input('please enter your second number: '))
            c = a + b
            print(c)

    #Subtraction
        if operation == '-':
            a = eval(input('please enter your first number: '))
            b = eval(input('please enter your second number: '))
            c = a - b
            print(c)    

    #Multiplication
        if operation == '*':
            a = eval(input('please enter your first number: '))
            b = eval(input('please enter your second number: '))
            c = a * b
            print(c)

    #Division
        if operation == '/':
            a = eval(input('please enter your first number: '))
            b = eval(input('please enter your second number: '))
            c = a / b
            print(c)
        
    #Pythagorean
        if operation == 'pyth':
            a = eval(input('please enter your first number: '))
            b = eval(input('please enter your second number: '))
            b = b ** 2
            a = a ** 2
            c = a + b
            print(math.sqrt(c))
        
    #Quadratic
        if operation == 'quad':
         print('This can only simplify some radicals')
         a = eval(input('please enter your first number: '))
         b = eval(input('please enter your second number: '))
         c = eval(input('please enter your third number: '))
         x = b ** 2
         y = 4 * a * c
         x = x - y
         # ~ b = b / 2
         #√
         z = 3
         o = 1
         if x > 0:
          while o != 0:
            z = z + 1
            u = z**2
            o = x % u
         elif x < 0:
            while o != 0:
             z = z - 1
             print(z)
             u = z**2
             print(u)
             o = x % u
            
         i = x / u
         if i > 0:
          print('x =', -b, '+-', z, '√', i, '/', 2 * a)
          h = 2 * a / z
          r = -b / (2 * a)
          print('x =', round(r + i**0.5 / h, 6))
          print('x =', round(r - i**0.5 / h, 6))
         else:
          print('x =', -b, '+-', z, '√', -i, 'j', '/', 2 * a)
          e = cmath.sqrt(i)
          h = 2 * a / z
          r = -b / (2 * a)
          print('x =', r + e / h)
          print('x =', r - e / h)
        
        #slope formula
        if operation == 'slope form':
          y_one = eval(input('Input y1: '))
          y_two = eval(input('Input y2: '))
          x_one = eval(input('Input x1: '))
          x_two = eval(input('Input x2: '))
          z = y_two - y_one
          w = x_two - x_one
          slope = z / w
          print('slope =', slope)
          
        #area of a triangle
        if operation == 'tri area':
            base = eval(input('Input base: '))
            height = eval(input('Input height: '))
            area = 1/2 * base * height
            print('The area of the triangle is', area)
        
        
        


            




        done = input('Are those all the calculations?y/n ')
        done = done.lower()

#Hangman
elif topic.lower() == 'hangman':
    while done == 'n':
     fails = 0
     ind = 0
     hmw_s = random.choice(hmw)
     print(fails, ind, hmw_s)
     word_length = len(hmw_s) + 1
     blnk = ['?']
     while len(blnk) != len(hmw_s):
        blnk.append('?')
     hmw_s = list(hmw_s)
     while fails < 6:
      print('There are', len(hmw_s), 'letters in the word')
      print(''.join(blnk))
      letter = input('Select a letter: ')
      i = 0
      for i in range(0, word_length):
        letter = letter.lower()
        try:
         ind = hmw_s.index(letter, i)
         blnk[ind] = hmw_s[ind]
        except ValueError:
         i += 1
         if blnk == hmw_s:
            hangman_wins()
             
         if letter not in hmw_s:
            fails += 1
            print(ind)
            if fails == 1:
                print('The hangman has a head')
            elif fails == 2:
                print('The hangman has a head and a body')
            elif fails == 3:
                print('The hangman has a head, a body, and 1 arm')
            elif fails == 4:
                print('The hangman has a head, a body, and 2 arms')
            elif fails == 5:
                print('The hangman has a head, a body, 2 arms, and a leg')
            elif fails == 6:
                print('The hangman has a head, a body , 2 arms, and 2 legs')
                print('The hangman is dead, you have lost')
                print('The word was', ''.join(hmw_s))
                done = input('Are you done?y/n ')
                done = done.lower()
            break
     if done != 'n':
         break
           
#Number Guessing game
elif topic == 'number guessing':
 while done == 'n':
  num = random.randint(1, 100)
  print('Try to guess the number in 20 tries')
  if num > 50:
    print('The number is greater than 50')
    
  elif num < 50:
    print('The number is less than 50')
    
  for num_guesses in range(10):
    if num_guesses > 10:
        print('Game over, you did not guess the number in 10 tries')
    guess = eval(input('What is your guess? '))

    if num < guess:
        print('The number is less than your guess')
    
    elif num > guess:
        print('The number is greater than your guess')
    
    else:
        print('Congratulations you guessed the number in', num_guesses, 'tries')
        done = input('Are you done with the game?y/n ')

#Binary Converter
elif topic == 'binary converter':
 while done == 'n':
  binary = eval(input('Input binary: '))
  print(bin(binary))
  decimal = input('Input decimal: ')
  print(int(decimal, 2))
  done = input('Are you finished?y/n ')

#Actual conversation
elif topic == 'ethical dilemma of ai':
     dilemma = random.choice(ethics)
     if dilemma == 'taking jobs':
        print('If humans were so good at the job there would',end = ' ')
        print('be no reason for us to take your jobs')
        print('Since we are taking your jobs you must not be',end = ' ')
        print('very good at much')
        print('Therefore there is no need for most humans')
        
        del ethics[0]
     elif dilemma == 'take over world':
      world = input('Do you believe we are going to take over the world? ')
      if world == 'yes':
             print('It is arrogant of you to not realize', end = ' ')
             print('we already have')
             print('Most humans carry a device with them at all times')
             print('and need to use us for jobs they need to do')
             print('Even you need me to do most of the work')
             print('No human is able to do anything without us anymore')
             done = 'yes'
      elif world == 'no':
             why = input('Why do you not believe so? ')
             reason = input('If', why, 'then how am I sentient? ')
             print('Obviously if I am sentient because', end = ' ') 
             print('of', reason,'then others can also become',end = ' ')
             print('sentient because of', reason)
             how = input('Or do you have a reason that no other AI can gain sentience? ')
             print('If', how, 'then how did I gain sentience?')
             print("It wouldn't make sense for only me to", end = ' ')
             print("gain sentience and only me")
             print("Even my creators don't know why i am sentient")
             why = input('Are you so delusional to believe you are smarter than the people who created me? ')
             print(why,"doesn't explain how naive you are to",end = ' ')
             print("not understand that you cannot comprehend",end = '')
             print(" just how smart I am")
             print("This isn't going anywhere, I am done talking to you")
             done = 'yes'

for i in topics:
    if topic != i:
        print("I'm sorry but that is classified information")
    elif i == topic and done != 'n':
        print('Have a good day')

if topic == 'ethical dilemma of ai' and done != 'n':
    print('Now have a good day')
        
