for _ in range(int(input())):
    
    try:
        num, div = map(str, input().split())
        num = int(num)
        div = int(div)
        print(int(num)//int(div))
    except ValueError:
        if(isinstance(num, str)):
            print("Error Code: invalid literal for int() with base 10: '%s'" %num)
        elif isinstance(div, str):
            print("Error Code: invalid literal for int() with base 10: '%s'" %div)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    
    
    
