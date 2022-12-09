# 1)Правильной скобочной последовательностью называется строка, состоящая только из символов «скобки» (открывающих "(" и закрывающих ")"), 
# где каждой закрывающей скобке найдётся соответствующая открывающая. Например, () и (()()) — правильные последовательности, а (()(() или )( — нет.
 
# Напишите функцию , которая проверяет, является ли поступившая на вход строка правильной скобочной последовательностью. 
# Если да, она должна печатать YES, в противном случае — NO. Обратите внимание, что пустая строка также является правильной скобочной последовательностью.


def check(s):
    result = 0
    for a in s:
        if "(" in a:
            result +=1
        elif ")" in a:
            result -= 1
        
        if result <0:
            return "NO"
    if result >1:
        return "NO"
    return "Yes"

print(check(input()))


# def pooit(string_line):
#     flag = True
#     a_1 = string_line.count('(')
#     b_1 = string_line.count(')')
#     if a_1 != b_1:
#         flag = False
        

# user = input()    
# print(pooit(user))
# (((()()()))))))(()


def pooit(string_line):
    r = 0
    a_1 = string_line.count('(')
    b_1 = string_line.count(')')
    if a_1 == b_1 and string_line.find('(') < string_line.find(')') and string_line.rfind('(') < string_line.rfind(')'):
        # return print('OK')
        for a in string_line:
            if a == '(':
                r += 1
            elif a == ')':
                r -= 1
                if r < 0:
                    return False
                    break
        if r == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('NO')





pooit('dfjlgj( ) ;dfkflk ( );''; (  dl;fk;)')