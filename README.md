# Crypto Trading Calculator
#### Video Demo:  <https://youtu.be/CvJ6-1-enUc?si=a5U0LEQRUXH0Mnxz>
#### Description:
This project is a calculator for trading cryptocurrencies. It was written by me (Hodais Torkamand) using Python 3.10 and sys module. It allows the user to enter the purchase and sales commission percentages of their exchange, and then enter multiple buys and sell transactions of cryptocurrencies. It calculates the net cost, revenue, profit, or loss of trading crypto based on the difference between the total cost and revenue. It also keeps track of the total amount of crypto that the user has.
The main features or components of this project are:
**commission_questions function:** This function asks the user to enter the commission percentage of their exchange for buying or selling crypto. If the percentage that the user entered is not between 0% and 2%, its raises ValueError. This function validates the input and returns the percentage as a float.
**commission function:** This function calculates the commission fee for buying or selling crypto based on the price, amount, and commission percentage that gets from the commission_questions function.
**questions function:** This function asks the user to enter the price and amount of crypto that they want to buy or sell. It validates the input and returns a list of two floats. Each question will be repeated 3 times if the user enters invalid input. After 3 invalid input, the program will be exited.
**how_much function:** This function calculates the net cost or revenue of buying or selling crypto based on the price, amount, and commission fee.
**calculate function:** This function calculates the net profit or loss of trading crypto based on multiple transactions. It uses a loop to ask the user to enter the next step (buy, sell, or stop). It updates the amount of crypto that the user has and appends the net cost or revenue to a list. It stops when the user enters “stop” or when the amount of crypto is zero. It returns the sum of the list as a float.
**convert_number function:** This function converts a number to an integer or a float with two decimal places depending on whether it has decimals or not.
**main function:** This is the main entry point of the program. It calls the global variables for buy and sell commission percentages, and then calls the calculate function with the first buy transaction as an argument. It prints out the final profit or loss in dollars.
I designed and implemented this project using Python 3.10 as my programming language and sys module as my only dependency. I used sys module to exit from the program when there is an invalid input or a wrong amount. I used basic data types such as floats, strings, lists, and booleans to store and manipulate data. I used functions to modularize and reuse code. I used loops, conditional statements, and exception handling to control the flow of execution. I used input and print functions to interact with the user.
The program will start running and ask you for inputs. You need to follow the instructions and enter valid numbers for all inputs. The program will display the results on the screen.
Some of the challenges or difficulties that I faced or overcame while working on this project are:
•	Handling different types of errors and exceptions that may occur due to invalid inputs or wrong amounts.
•	Making sure that the program stops when the user enters “stop” or when the amount of crypto is zero.
•	Formatting the output to show the correct number of decimals and symbols.
Some of the limitations or improvements that I would like to make on this project in the future are:
•	Adding more features such as showing the current price and value of different cryptocurrencies, allowing the user to choose different currencies, and saving the history of transactions to a file.
•	Improving the user interface and experience by using a graphical user interface (GUI) or a web application instead of a terminal window.
•	Optimizing the code and performance by using better algorithms, data structures, and modules.