import libnum
from secret import flag

class LCG:
    a = 0x7d62d58188f9ab4ebd1a55620bd5152960eacc0016b2ae6241136979da8b59d3
    b = 0xb6e6d2e6c34d71878e596b5ef97ce76ec63a09e279ff961ea86c845951063074
    n = 0x5105b78d4fbfe202ee2e4c02aba41d59f435143897286ec801dfb307da928aa636b4b8524625a5117dea790a518e39f7e4cf240f414e6b61871ee56cd0d7cc17

    def __init__(self, init_seed):
        assert init_seed < self.n
        self.state = init_seed

    def rand(self):
        self.state = (self.a * self.state + self.b) % self.n
        return self.state

    def __str__(self):
        return hex(self.rand())

seed = libnum.s2n(flag)
lcg = LCG(seed)

times = 2 ** 20
while times > 0:
    lcg.rand()
    times -= 1

print(lcg)

# trick
from gmpy2 import invert
a = lcg.a
b = lcg.b
n = lcg.n
x = 2**20 + 1
lcg2 = ( pow(a, x, n)*seed + b*(pow(a, x, n)-1)*invert(a-1, n) ) % n
print(hex(lcg2))


