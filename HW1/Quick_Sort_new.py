def quicksort(x):
    if len(x) > 1:
        last = len(x)-1
        pivot = x[last]
        change_index = -1 # 用來標記需要互換位置的index
        j = 0 # 用來判斷的index
        while j <= last:
            if x[j] < pivot:
                change_index += 1
            elif x[j] == pivot:
                change_index += 1
                # 互換
                c = x[change_index]
                s = x[j]
                x[change_index] = s
                x[j] = c
                now_pi = change_index # 現在基準點所在的位置
            # 因為要讓x[j]去判斷與pivot，j+=1才能接著去檢查下一個list中的index的值
            j+=1
        # 對較小與較大的兩邊各自進行quick sort
        L = quicksort(x[:now_pi])
        R = quicksort(x[now_pi+1:])
        return L+[pivot]+R
    return x
    
example = [34,21,5,9,0,12,-3,-15]
quicksort(example)
