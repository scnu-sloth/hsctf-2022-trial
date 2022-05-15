from gmpy2 import invert
import libnum

a = 0x7d62d58188f9ab4ebd1a55620bd5152960eacc0016b2ae6241136979da8b59d3
b = 0xb6e6d2e6c34d71878e596b5ef97ce76ec63a09e279ff961ea86c845951063074
n = 0x5105b78d4fbfe202ee2e4c02aba41d59f435143897286ec801dfb307da928aa636b4b8524625a5117dea790a518e39f7e4cf240f414e6b61871ee56cd0d7cc17


times = 2 ** 100
x = times + 1
c = 0x9746d7770d1296870dbd8eaf03658d3e3ca2ceb5e28988ecc0557bdd0d44d811cacda444c91cafde598bf26ff108bfe36ca6e71f088f1eb2d648d59b3d96ab7
seed = (c - b*(pow(a, x, n)-1)*invert(a-1, n)) * pow(invert(a, n), x, n) % n
flag = libnum.n2s(int(seed))
print(flag)


