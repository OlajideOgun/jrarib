a_file = open('problem1/input-1.txt', "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  line_list = list(map(int, line_list))
  list_of_lists.append(line_list)

a_file.close()

length1  = list_of_lists[0][0]
length2 = list_of_lists[1][0]
print(length1,length2)



def sort(list1,list2):
  i = 0
  j = 0
  if length1 == 0:
    print(list2)
  if length2 == 0:
    print(list1)
  while i < length1 and j < length2:
    print(i,j)

sort(list_of_lists[0][1:],list_of_lists[1][1:])
  
