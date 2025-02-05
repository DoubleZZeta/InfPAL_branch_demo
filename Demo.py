def count_up(n):
    for i in range(n):
        print(i)

def count_down(n):
    for i in range(n-1,-1):
        print(i)

def mean(lst):
    return sum(lst)/len(lst)





def main():
    count_up(10)
    count_down(10)
    print(mean([1,2,3,4,5]))
