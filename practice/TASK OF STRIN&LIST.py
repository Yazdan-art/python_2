#___________________________THE FIRST TASK OF STRING __________________________________________________________


# print("\n"+"TASK ONE"+"\n\n\n")
#  # i.e : yazdan *ghezelbash*alborz*karaj     +98935555555
# st="login page"
# print(st.upper())
# print("\n")
# user_string=input("Enter your Name * familly * City "+"\n").capitalize().strip().rsplit('*',2)

# print("\n")
# print(user_string)

# num=input("Enter cell phone number"+"\n")

# if num.startswith("+98",0,20):
#    num= num.replace("+98","0",1)
   
# if num.isnumeric and len(num)==11 :
#     print("your cellphnone is correct ",num)
# else:
#     print("please try again and enter your valid number like: 09121234567 /+989121234567 ")   
 
#___________________________ THE SECOND TASK OF STRING  __________________________________________________________


# string.find(value, start, end)

print("\n"+"TASK TWO,Parsing and Extracting"+"\n\n\n")

email=input("Enter Your Email And date"+"\n")#Yazdan-art@gmail.com 10 November 2023

print("your domain of the email :",email[email.find('@')+1 : email.find(  ' '   ,  email.find('@'))])
print("your host of the email:",email[ :email.find('@')])        #   :     از ابتدای تا ابتدای 
print("date of registration:",email[email.find(  ' '   ,  email.find('@')):])


#____________________________ TASK OF LIST________________________
print("\n"+"TASK 3 ,lists"+"\n\n\n")
myList=email.split('@')
host=myList[0]
domain=myList[1][  :  myList[1].find(' ')]

date=myList[1][ myList[1].find(' ')  : ]

print("your host is: "+host+"\n"+"your date is: "+date+"\n"+"your domain is: "+domain)