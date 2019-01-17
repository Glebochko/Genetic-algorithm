
class cell:
    def __init__(self):
        self.type = 0
        

def main():
    n = 5
    m = 4
    botsmap = []
    for i in range(n + 1):
        botsmap.append([])
        for j in range(m + 1):
            botsmap[i].append(cell())


    for i in range(n + 1):
        botsmap[i][m].type = 2
    for j in range(m + 1):
        botsmap[n][j].type = 2 



    for i in range(n + 1):
        for j in range(m + 1):
            print(botsmap[i][j].type)
        print('-----')
main()