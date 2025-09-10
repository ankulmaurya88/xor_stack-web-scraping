from learn import add,multiply

def dived(a,b):
    if b>0:
        return a/b
    else:
        return "not divable "
    
def sub(a,b):
    return (a-b)

if __name__=="__main__":
    print (add(2,3))
    print(dived(2,3))
    print(sub(2,3))
    print(multiply(2,3))