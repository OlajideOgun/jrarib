import sys
list_of_lists = []

for line in sys.stdin:
  stripped_line = line.rstrip()
  line_list = stripped_line.split()
  line_list = list(map(int, line_list))
  list_of_lists.append(line_list)

# a_file = open(sys.argv[1], "r")
# for line in a_file:
#   stripped_line = line.strip()
#   line_list = stripped_line.split()
#   line_list = list(map(int, line_list))
#   list_of_lists.append(line_list)
# a_file.close()

def merge(list1, list2):
    if len(list1) == 0 :
        return list2
    if len(list2) == 0:
        return list1
    sortedlist = []
    x = 0
    y = 0
    while len(sortedlist) < len(list1) + len(list2):
        if list1[x] < list2[y]:
            sortedlist.append(list1[x])
            x = x + 1
        else:
            sortedlist.append(list2[y])
            y = y + 1

        if x == len(list1) or y == len(list2):
            sortedlist.extend(list1[x:] or list2[y:])

    return sortedlist



def merge_sort(numList):

    if len(numList) == 1 :
        return numList
    elif len(numList) == 0:
        return numList

    midpoint = len(numList) // 2
    list1 = merge_sort(numList[:midpoint])
    list2 = merge_sort(numList[midpoint:])

    return merge(list1,list2)

result = list(map(str,merge_sort(list_of_lists[1])))
result = ", ".join(result).replace(",","")
print(result)

