"""6. Write a python script which takes a three digit number from the user and displays
only its middle digit."""
x=int(input("Enter any three number ..:"))
# when you find out mid value of three digit then divided by 10
# when you find out mid value of fifth digit then divided by 100
#when you find out mid value of seventh digit then divided by 1000

y=int(x/10)
print("Its mid value of ",x ,"is :",y%10)
