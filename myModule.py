def myderive(f, var):
    if(type(f) == int or type(f) == float):
        return 0
    elif(type(f) == str):
        if(f == var):
            return 1
        else:
            return 0
    elif(f[0] == '+'):
        return ["+" ,myderive(f[1], var), myderive(f[2], var)]
    elif(f[0] == '-'):
        return ["-" ,myderive(f[1], var), myderive(f[2], var)]
    elif(f[0] == '*'):
        return ["+", ["*", myderive(f[1], var), f[2]], ["*", f[1], myderive(f[2], var)]]
    elif(f[0] == '/'):
        return ["/", ["-", ["*", myderive(f[1], var), f[2]], ["*", f[1], myderive(f[2], var)]], ["*", f[2], f[2]]]
