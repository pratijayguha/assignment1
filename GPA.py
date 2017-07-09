def gpa(n,credit,grade):
    gpa=0
    for i in range(n):
        gpa+=credit[i]*grade[i]
    net_gpa=gpa/sum(n)
    if net_gpa<5:
        return 'sed_lyf'
    elif net_gpa>9:
        return 'GGWP'
