# finding duplicates
#for a word
my_string = "banana"
print("The list is : "+ my_string)
print("The duplicate elements in the strimy_string are : ")

for i in range(0, len(my_string)):
   for j in range(i+1, len(my_string)):
      if(my_string[i] == my_string[j]):
        print(my_string[j])
 
#numerals
my_list = [1, 2, 5, 6, 8, 9, 3, 4, 8, 9, 1, 8]
print("The list is :")
print(my_list)
print("The duplicate elements in the list are : ")

for i in range(0, len(my_list)):
   for j in range(i+1, len(my_list)):
      if(my_list[i] == my_list[j]):
         print(my_list[j])
         
#list of fruits
my_list2 = ["banana","apple","grape","apple","carrot","mango","banana"]
print("The list is : ")
print(my_list2)
print("The duplicate elements in the strimy_list2 are : ")

for i in range(0, len(my_list2)):
   for j in range(i+1, len(my_list2)):
      if(my_list2[i] == my_list2[j]):
        print(my_list2[j])
    