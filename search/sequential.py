def sequential_search(item_list, item):
  for index, value in enumerate(item_list):
    if value == item:
      return True
  return False

def alt_seq_search(item_list,item):
  n = len(item_list)
  pos = 0
  while  pos < n:
    if item_list[pos] == item:
      return True
    pos += 1
  return False

data = [1,2,3,4,'t']

def ordered_seq_search(item_list, item, order=0):
  # order 0 means ASC whereas 1 means DESC
  n = len(item_list)
  pos = 0
  while  pos < n:
    cur_item  = item_list[pos]
    print(cur_item)
    if  cur_item == item:
      return True

    if order == 0 and cur_item > item:
      return False

    if order == 1 and cur_item < item:
      return False

    pos += 1
  return False

data = [1,2,5,7,9]
atad = [9,7,5,2,1]


# print(sequential_search(data, 2))
# print(alt_seq_search(data, 't'))
# print(alt_seq_search(data, 'f'))
# print(alt_seq_search(data, 9))
print(ordered_seq_search(data, 4))
print(ordered_seq_search(atad, 4,order=1))

print("-------")
print(ordered_seq_search(data, 5))
print(ordered_seq_search(atad, 5, order=1))