def return0dd(list1):
    holder = []
    for i in range(len(list1)):
        if i % 2 == 1:
            holder.append(list1[i])
    return holder
