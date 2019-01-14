
def main():
    
    x = 3
    y = 6

    a =[[0] * y for i in range(x)]

    for i in range(x):
        for j in range(y):
            print(a[i][j])
        print('-')

    
main()