## **Password Generator using Python**



#### **## Task**

#### 

#### **Task 31 – Build a Password Generator**

###### 

###### **## Description**



This project is a simple and configurable Password Generator developed using Python.



The program allows the user to select:



\- Password length

\- Whether to include letters

\- Whether to include numbers

\- Whether to include symbols



The program uses Python's `secrets` module to generate random password characters securely.

###### 

###### **## Objective**



The main objectives of this project are:



\- To practice Python functions

\- To understand Python modules

\- To use the `secrets` module

\- To use the `string` module

\- To practice conditional statements

\- To practice loops

\- To generate configurable passwords

\- To understand basic secure programming concepts

###### 

###### **## Technologies Used**

###### 

\- Python

\- secrets module

\- string module



###### **## Python Modules Used**



**### 1. secrets**



The `secrets` module is used to generate cryptographically strong random values.



It is preferred for security-sensitive applications such as password generation.



Example:



```python

secrets.choice(characters)

```



**### 2. string**



The `string` module provides predefined character sets.



The project uses:



```python

string.ascii\_letters

```



for uppercase and lowercase letters.



```python

string.digits

```



for numbers.



```python

string.punctuation

```



for special characters.



###### **## Features**



\- User can choose password length.

\- User can include letters.

\- User can include numbers.

\- User can include symbols.

\- Password is generated randomly.

\- Uses `secrets` instead of `random`.

\- Checks for invalid password length.

\- Checks whether at least one character type is selected.

\- Displays the generated password and its length.



###### 

###### **## Program Code**



import secrets

import string





def generate\_password(length, use\_letters, use\_numbers, use\_symbols):



&#x20;   characters = ""



&#x20;   if use\_letters:

&#x20;       characters += string.ascii\_letters



&#x20;   if use\_numbers:

&#x20;       characters += string.digits



&#x20;   if use\_symbols:

&#x20;       characters += string.punctuation



&#x20;   if characters == "":

&#x20;       return None



&#x20;   password = ""



&#x20;   for i in range(length):

&#x20;       password += secrets.choice(characters)



&#x20;   return password





print("===================================")

print("       PASSWORD GENERATOR")

print("===================================")



length = int(input("Enter password length: "))



letters = input("Include letters? (yes/no): ").lower()

numbers = input("Include numbers? (yes/no): ").lower()

symbols = input("Include symbols? (yes/no): ").lower()



use\_letters = letters == "yes"

use\_numbers = numbers == "yes"

use\_symbols = symbols == "yes"



if length <= 0:

&#x20;   print("Password length must be greater than 0.")



else:

&#x20;   password = generate\_password(

&#x20;       length,

&#x20;       use\_letters,

&#x20;       use\_numbers,

&#x20;       use\_symbols

&#x20;   )



&#x20;   if password is None:

&#x20;       print("Please select at least one character type.")



&#x20;   else:

&#x20;       print()

&#x20;       print("Generated Password:", password)

&#x20;       print("Password Length:", len(password))



###### 

###### **## How to Run**



**### Step 1**



Install Python on your computer.



**### Step 2**



Open Command Prompt or Terminal.



**### Step 3**



Go to the project folder.



Example:



```bash

cd Task31\_Password\_Generator

```



**### Step 4**



Run the Python program:



```bash

python password\_generator.py

```



###### **## Sample Input**





Enter password length: 10

Include letters? (yes/no): yes

Include numbers? (yes/no): yes

Include symbols? (yes/no): yes



###### **## Sample Output**





===================================

&#x20;      PASSWORD GENERATOR

===================================



Generated Password: \[randomly generated password]

Password Length: 10





The generated password will be different each time because the program uses secure random selection.



###### **## How the Program Works**



The program first asks the user for the required password length.



Then it asks whether the password should contain:



1\. Letters

2\. Numbers

3\. Symbols



Based on the user's choices, the program creates a collection of allowed characters.



For example:



```text

Letters + Numbers + Symbols

&#x20;       ↓

Character collection

&#x20;       ↓

secrets.choice()

&#x20;       ↓

Generated password

```



###### **## Validation**



The program checks whether the password length is greater than zero.



If the user enters:



```text

0

```



or a negative number, the program displays:



```text

Password length must be greater than 0.

```



The program also checks whether the user selected at least one character type.



If no character type is selected, it displays:



```text

Please select at least one character type.

```



###### **## Security Considerations**



The project uses the `secrets` module instead of the `random` module.



This is important because passwords are security-sensitive values.



The generated password should not be unnecessarily stored or printed in application logs.



###### **## Learning Outcomes**



After completing this project, I learned:



\- How to import Python modules

\- How to create and call functions

\- How to use conditional statements

\- How to use loops

\- How to work with strings

\- How to use `secrets.choice()`

\- How to generate random passwords

\- How to validate user input

\- Basic secure programming practices



###### **## Conclusion**



The Password Generator is a simple Python project that demonstrates functions, modules, conditional statements, loops, strings, and secure random generation.



The project provides users with a configurable way to generate passwords based on their selected length and character types.

