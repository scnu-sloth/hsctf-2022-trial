import libnum

flag = 'HSCTF{C4n_Y0u_Op3n_Y0ur_M1cr0ph0n3_???}'

def encode(m):
    enChart = {'4': '6', '3': '5', '2': '4', '1': '7', '0': '2'}
    mm = libnum.s2n(m)
    res = ''
    while mm > 0:
        res = str(mm%5) + res
        mm //= 5
    res = ''.join([enChart[r] for r in res])
    return int(res)

def decode(c):
    deChart = {'6': '4', '5': '3', '4': '2', '7': '1', '2': '0'}
    cc = ''.join([deChart[ci] for ci in str(c)])
    res = int(cc, 5)
    return libnum.n2s(res).decode()

c = encode(flag)
m = decode(c)
assert m == flag
print(c)