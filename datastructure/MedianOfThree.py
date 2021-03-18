def median_of_three(array):
    median_index = (len(array)//2)
    print(0, median_index, len(array))
    first_value = array[0]
    median_value = array[median_index]
    last_value = array[-1]
    print(array)
    a = [first_value, median_value, last_value]
    a.sort();
    print(a)
    array[0] = a[0]
    array[median_index] = last_value
    print(array)
    r=dict()
    return r


if __name__ == '__main__':
    data = [4, 2, 5, 7, 9, 10, 1, 3, 8, 6, 0]
    refine_data = median_of_three(data)
    print(refine_data)
