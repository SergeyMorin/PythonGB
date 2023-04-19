# def rint_operation_table(operation, num_rows=6, num_columns=6):

def print_table (op,a,b):
    for i in range(1,a+1):
        for j in range(1,b+1):
            if i == 1 or j == 1:
                print(i*j, end = " ")
            if i > 1 and j > 1:
                print(op(i,j), end = " ")
        print()


a = lambda x, y: x + y

print_table(a,4,4)