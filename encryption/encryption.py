# https://www.urionlinejudge.com.br/judge/en/problems/view/1024

def shift_ascii(letter, n):
    if letter>='A' and letter<='Z' or letter>='a' and letter<='z':
        return chr(ord(letter) + n)
    else:
        return letter

def shift_all_ascii(letter, n ):
    return chr(ord(letter) + n)

N = int(input())

for i in range(N):
    output = ''
    input_data = input()
    for c in reversed(input_data):
        output += shift_ascii(c, 3)
    
    count=0
    output = [c for c in output]
    while count != len(output):
        if count >= len(output)//2:
            output[count] = shift_all_ascii(output[count], -1)
        count += 1  
    output = ''.join(output)
    print(output)



