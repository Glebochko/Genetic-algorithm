from random import randint

def main():
    DNA = []
    for i in range(64):
        DNA.append(randint(0, 5))
        #print(DNA[i])
    print(DNA)
main()