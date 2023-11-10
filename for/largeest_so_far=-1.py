# largeest_so_far=-1
# print ('before',largeest_so_far)
# for the_num in [9,41,12,3,74,15]:
#     if the_num>largeest_so_far:
#         largeest_so_far=the_num
#     print(largeest_so_far,the_num)    
# print('after',largeest_so_far)    
#___________________________________
# sum=0
# count=0

# print('before',sum)
# for the_num in [9,41,12,3,74,15]:
#    sum+=the_num
#    count+=1
# print('avrage = ' ,sum/count)  
#___________________________________
# for the_num in [9,41,12,3,74,15,19,20,28,64,70,90]:
#     if the_num>18:
#         print(the_num)
#     if the_num==90:
#         print('there is a person with 90 age')  
#___________________________________  
smallest=None
print("before")
for the_num in [9,41,12,3,74,15,19,20,28,64,70,90]: 
    if smallest is None:
        smallest=the_num
    elif the_num<smallest:
        the_num=smallest 
        print("smallest",the_num)
print("after ",the_num)        
              