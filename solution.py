import sys 
a_file = open(sys.argv[1], "r")
list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  line_list = list(map(int, line_list))
  list_of_lists.append(line_list)
a_file.close()

length1  = list_of_lists[0][0]
length2 = list_of_lists[1][0]



def sort(list1,list2):
  new_list = []
  i = 0
  j = 0
  k = 0
  if length1 == 0:
    return([length2] + list2)
  if length2 == 0:
    return([length1] + list1)



  while i < length1 and j < length2:
    if list1[i] < list2[j]:
      new_list.append(list1[i])
      i = i + 1
    elif list1[i] > list2[j]:
      new_list.append(list2[j])
      j = j + 1

    if j == length2:
      new_list = new_list + list1[i:]
    if i == length2:
      new_list = new_list + list2[j:]
  
  return ([length1 + length2]+ new_list)


result = sort(list_of_lists[0][1:],list_of_lists[1][1:])
outF = open(sys.argv[2], "w")
outF.write(str(result))
outF.close()
  
