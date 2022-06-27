def max_sequence(arr):
    not_negative=[x for x in arr if x>0]
    if len(not_negative)==0:
        result = 0
    else:
        result = sum(arr)
        count = 2
        while count < len(arr):
            for i in range(0, len(arr)):
                a = ([arr[k] for k in range(i, i+count) if i+count<len(arr)+1])
                if len(a) != 0:
                    if result < sum(a):
                        result=sum(a)
            count +=1
    return result
