def pygLatin(str):
    if str[0]!='a' and str[0]!='e' and str[0]!='i' and str[0]!='0' and str[0]!='u':
        str=str[1:]+str[0]+'ay'
    else:
        str=str[1:]+str[0]+'hay'
    return str


print(pygLatin('waterworks'))
