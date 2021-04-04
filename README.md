# Loan Calculator https://hyperskill.org/projects/90

## Stage 1
Let's start by imitating this behavior. There are some prepared variables in the source code: these are text messages that our loan calculator can output. In this stage, all you need to do is output them in the right order.

## Stage 2
The behavior of your program should look like this:

* Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.
* To perform further calculations, you'll also have to ask for the required missing value.
* Finally, output the results for the user.

## Stage 3
In this stage, you should add new behavior to the calculator:

1. First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.
2. Then, you need to ask them to input the remaining values.
3. Finally, compute and output the value that they wanted.

## Stage 4
In this stage, you are going to implement the following features:

* Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
* Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
* Handling of invalid parameters. It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).

The final version of your program is supposed to work from the command line