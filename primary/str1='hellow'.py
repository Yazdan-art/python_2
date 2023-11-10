# str1='hello'
# str2="world"
# bob =str1+str2
# print(bob)
# str3="123"
# x=int(str3)+1
# print(x)

#___________________
# age=int(input("enter your age"))
# if(age>18):
#     print("age >18")
# elif(age==18):   
#     print("age==18") 
# else:
#     print("age<18")
#______________________
# fruit="banana"
# letter=fruit[0]
# print(letter)

# print("\n")

# x=3
# print(fruit[x-1])
# print(len(fruit))
#_________________________
# fruit="banana"
# index=0
# while index<len(fruit):
#     letter=fruit[index]
#     print(index,letter)
#     index=index+1
#_________________________
# fruit="banana"
# for latter in fruit:
#     print(latter)
    
#_________________________    
# fruit="banana"
# count =0
# for letter in fruit:
#     if (letter=='a'):
#         count=count+1
# print(count) 

#__________________________________
# s="Monty python"
# print(s[:])
# print(s[0:2])
# print(s[0:5])
# print(s[:2])
# print(s[5:])
#________________
# fruit="banana"
# if "nan" in fruit:
#     print("found it")
# print("nan"in fruit)# this is a summarisation of the command
#________________
# word=input("enter your desire word")
# userName="yazdan"
# if word==userName:
#     print("wellcome")
# elif word>userName:
#     print("your word,"+word+"comes before userName")
# elif word<userName:
#     print("your word,"+word+"comes after userName")    
# else :
#     print("wellcome"+userName)
#___________________________________
#greet="yazdan ghe"
# lower_greet=greet.lower()
# print(lower_greet)
# print(greet.upper())
# print(type(greet))
# print(dir(greet))
#split1=greet.split()
#print(split1)
#print(greet.split())
#___________________________________
# fruit="banana"
# fin=fruit.find("an")
# print(fin)
#___________________________________
# fruit="banana"
# print(fruit.capitalize())
# fruit=fruit.upper()
# print(fruit)
# print(fruit.capitalize())
# rep=fruit.replace('ana','ANA',2)
# print(rep)
#___________________________________
# fruit="    banana,orange    "
# print(fruit.lstrip().rstrip().capitalize())
#___________________________________
long_str=" The rsplit() method is same as split method that splits a string from the specified separator and returns a list object with string elements. The default separator is any whitespace character such as space, \t, \n, etc." 
"The only difference between the split() and rsplit() is when the maxsplit parameter is specified. If the maxsplit parameter is specified, then the rsplit() method starts splitting a string from the right side (from the last character), whereas the split() method starts splitting from the left side (from the first character)."
print("\n")
print(long_str.split())
print("\n")
print(long_str.rsplit(' ',3))
