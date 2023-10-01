def mera_filter(Pattern,repl,arg):
    a=arg
    b=""
    for i in a:
        if i not in Pattern:
            b+=i
        else:
            b+=repl
    print(b)    