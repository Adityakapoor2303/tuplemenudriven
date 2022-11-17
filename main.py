while True:
    a=tuple(input("Enter a tuple"))
    print('''
            To count Number of occurrence of specific value type 1 
             To count first occurrence of specific value type 2''')
    b=input("Enter the method to be used: ")
    if b=="1":
        d=input("Enter the value to be counted: ")
        e=a.count(d)
        print(e)
    elif b=="2":
        c=input("Enter the value of which index is required: ")
        f=a.index(c)
        print(f)
    break



