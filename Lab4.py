""" Lamens
This program gives the user three tries to answer the quesiton 
question = "what is the capital of California". With the answer being Sacramento
We have to set a value for the three tries they get: max_tries = 3.
Then we create a loop to iterate three times. For each iteration, we ask the user for the answer. 
Then based on the answer the user gives, we check to see if the user input matches the correct answer. 
If so we print "correct!" then terminate the loop.

If the user fails to guess the correct answer within three tries, then print
"You have used up all your guesses"

"""
"""Psudocode
main
  question= "what is the capital of California"
  ask(question, answer)

ask
  tries=0
  loop three times
        tries+=1
        ask user input()
        check to see if input=answer
            if so, print "correct"
            end
    if not correct
        print to the user "You have used up all your guesses"
        print the correct answer "The correct answer is Sacramento"

main
"""
def main():
    question= "What is the captial of California? "
    answer = "Sacramento"
    ask(question, answer)
def ask (question, answer, maxTries=3):
    tries = 0
    ans =""
    while tries < maxTries:
        tries =tries+1
        ans = input(question)
        if ans==answer:
            print("correct")
            break
    if ans != answer:
        print("You have used up your allotment of guesses.")
    
main()








