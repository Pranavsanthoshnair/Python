def gen_fibonnaci(n):
    sequence = []
    first_num,second_num = 0,1
    for i in range(n):
        sequence.append(first_num)
        first_num,second_num = second_num,first_num + second_num
    return sequence
