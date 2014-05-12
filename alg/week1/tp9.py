def merge_sort(array_nums):
    if(len(array_nums) > 2):
        array_left = merge_sort(array_nums[:int(len(array_nums) / 2)])
        array_right = merge_sort(array_nums[int(len(array_nums) / 2):])
    else:
        if(len(array_nums) == 2):
            if(array_nums[0] > array_nums[1]):
                array_nums[0], array_nums[1] = array_nums[1], array_nums[0]
        return array_nums
 
    out_array = []
    while(0 < (len(array_left) + len(array_right))):
        if(len(array_left) == 0):
            out_array.append(array_right.pop(0))
        elif(len(array_right) == 0):
            out_array.append(array_left.pop(0))
        else:
            if(array_left[0] > array_right[0]):
                out_array.append(array_right.pop(0))
            else:
                out_array.append(array_left.pop(0))
    return out_array
