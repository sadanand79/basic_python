#1.Simple Message: Store a message in a variable, and then print that message.
Name='S Dombale'
print("Name:",Name)
#2.Store a message in a variable and print that message. Then change the value of your variable to a new message andprint the new message.
Name='S Dombale'
print("Name:",Name)
Name='sadanand'
print("Name:",Name)

#3.Store a person’s name in a variable andprint a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
Name= "SD"
print ("Hello %s, would you like to learn some Python today?"%(Name))

#4.Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.
quote = 'John Locke once said,“I have always thought the actions of men the best interpreters of their thoughts.”'
print (quote)

#5.Repeat Exercise 4, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message.Print your message.
famous_person='John Locke'
quote = ' once said,“I have always thought the actions of men the best interpreters of their thoughts.”'
print (famous_person,quote)

#6.Write addition, subtraction, multiplication, and division operations that each result in the number 8.Be sure to enclose your operations in print statements to see the results.You should create four lines that look like this:print (5 + 3)Your output should simply be four lines with the number 8 appearing once on each line.
print('{0}\n{1}\n{2}\n{3}\n'.format(5+3,9-1,2*4,int(16/2)))

#7.Store your favouritenumber in a variable.Then, using that variable, create a message that reveals your favouritenumber.Print that message.
my_fav=25
print("My favourite number is:",my_fav)

#8.Choose two of the programs you’ve written andadd at least one comment to each.If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file.Then write one sentence describing what the program does
#10-july-2020 SADANAND
print('{0}\n{1}\n{2}\n{3}\n'.format(5+3,9-1,2*4,int(16/2))) #simple airthmatic operations

quote = 'John Locke once said,“I have always thought the actions of men the best interpreters of their thoughts.”'
print (quote) #Print a simple quote 

#9.Store the names of a few of your friends in a list called names.Print each person’s name by accessing each element in the list, one at a time
Names=["praveen","Bassu","Manjunath","Swami"]
for friends in Names:
    #print("hello guys {0}" .format(friends))
    print(friends) 

#10.Start with the list you used in Exercise 9, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’sname.
Names=["praveen","Bassu","Manjunath","Swami"]
for friends in Names:
    print("How are you {0}" .format(friends))

#11.Think of your favouritemode of transportation, such as a motorcycle or a car, and make a list that stores several examples.Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”Python Basics-Assignment    
fav_mode  = 'Car'
stores = ["Abarth","Acura","Alfa Romeo","Aston Martin","Audi","Bentley","BMW"]
for Cars in stores:
  print (" I would like to drive a {0} {1}".format(Cars,fav_mode))"""
