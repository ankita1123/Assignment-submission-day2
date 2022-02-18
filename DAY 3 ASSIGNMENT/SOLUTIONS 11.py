#SOLUTION NO.11

numbers = {'one':1, 'two':2, 'three':3}
 pullout_key = 2
 for key, value in numbers.items():            
	if value == pullout_key:
		del numbers[key]
		break
	print(numbers)
	
	
	#Explaination:
	#call dict.items to get a list of the key values pairs of dict 
	#create a for loop to iterate through the list of key value pairs
	#at each , iteration checking if the value is desired value to remove.
	#use the del keyword along with the dict indexing to delete the key value pair and then call the break keyword....
	
	
	
#SOLUTION NO.12
#CREATING A TUPLE USING NUMBERS 8, 9 , 10....

t = (8, 9, 10)
print(t)

#ANOTHER EXAMAPLE:
t = (8, 9, 10)
print(t[2])

#OUTPUT:10


#13. Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
#d = {one:1, two:2, three:3} d[one]
#ERROR IN CODE:NameError: name 'one' is not defined
#SOLUTION NO.13 #EEROR FREE CODE
d={'one':1,'two':2, 'three':3}
 print(d)
{'one': 1, 'two': 2, 'three': 3}
 d['one']

#OUTPUT:1


#14.14 Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
#f = false not f
#ERROR IN CODE : syntax error : invalid syntax f is a undefined variable....
#SOLUTION NO.14 #ERROR FREE CODE
f = "false"
 if f==f:
	print("f is equal to false not f")

	#OUTPUT: f is equal to false not f
	
	
	
	
	
#15. Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
#lst = [1,3,5] lst[3]
#ERROR IN CODE: lst is a undefined variable which will give a invalid syntax error 
#SOLUTION NO.14 #ERROR FREE CODE
lst = [1, 3, 5, [3]]
 print(lst)

 #OUTPUT:[1, 3, 5, [3]]

