#function 1
total_list=input("Enter a string of numbers and words seperated by spaces:\n").split() #asks the user to Enter a string of numbers and words seperated by spaces, then saves it in the variable total_list
num_list = [] # creates an empty list called num_list
def find_numbers(n):  #defines a function where it takes a list and splits it into a list of numbers and a list of words 
  word_list = [] # creates an empty list called word_list
  global num_list
  for i in n: # loops through all the objects in string n
    if i.isdigit() == True: # if the object in string n at position i is a number then
      num_list.append(i) # add the number at position i to the list num_list
    else: #if the value is not a number
      word_list.append(i) # add the word at position i to the list word_list
  print("The words in the list are:", (', '.join(word_list)))  #outputs the list of words
  return (', '.join(num_list))  #returns the list of numbers
print("The numbers in the given list are:",find_numbers(total_list))  #states the list of numbers
print()  #separate the two functions

#function 2

def order_evens(n):  #n=num_list
  evens=[] # creates an empty list called evens
  for i in range(len(n)):
    if i%2==1:  #takes only every second number
    	evens.append(int(n[i]))
  for i in range(len(n)):
    if i%2==1:	
      n[i] = (str(max(evens)))
      temp = evens.index(max(evens))
      evens[temp] = 0
  print("This is the list with every second number put in order largest to smallest:")
  return (', '.join(n)) 
print(order_evens(num_list))
