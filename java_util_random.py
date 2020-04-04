# Simple Java java.util.random() in Python
import ctypes

def int_overflow(val):
    maxint = 2**31 - 1
    if not -maxint - 1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shitf(n, i):
    if n < 0:
        n = ctypes.c_uint32(n).value
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)
    
class JavaRandom():
    serialVersionUID = 3905348978240129619  # Long
    # seed = 0
    multiplier = 0x5DEECE66D  # Long
    addend = 0xB
    mask = (1 << 48) - 1
    DOUBLE_UNIT = 1.0 / (1 << 53)

    # IllegalArgumentException messages
    BadBound = "bound must be positive"
    BadRange = "bound must be greater than origin"
    BadSize = "size must be non-negative"

    def __init__(self, seed):
        self.seed = self.initialScramble(seed)

    def initialScramble(self, seed) -> int:
        return (seed ^ self.multiplier) & self.mask

    def setSeed(self, seed: int) -> None:
        self.seed = self.initialScramble(seed)

    def next(self, bits: int) -> int:
        # seed = self.seed
        oldseed = self.seed
        while True:
            nextseed = (oldseed * self.multiplier + self.addend) & self.mask
            if nextseed != oldseed:
                self.seed = nextseed
                return int(unsigned_right_shitf(nextseed, 48 - bits))
            else:
                oldseed = nextseed

    def nextBytes(self, bytes: bytearray):  # void
        # i = 0
        # while True:
        #
        pass

    def internalNextLong(self, origin: int, bound: int) -> int:
        pass

    def internalNextInt(self, origin: int, bound: int) -> int:
        pass

    def internalNextDouble(self, origin: float, bound: float) -> float:
        pass

    def nextInt(self, *bound: int) -> int:
        if bound:
            bound = bound[0]
            if bound <= 0:
                raise ValueError(self.BadBound)
            if (bound & -bound) == bound:
                return int((bound * self.next(31)) >> 31)
            while True:
                bits = self.next(31)
                val = bits % bound
                if bits - val + (bound - 1) > 0: return val
        else:
            return self.next(32)

    def nextLong(self) -> int:
        return (int(self.next(32) << 32) + self.next(32))

    def nextBoolean(self) -> bool:
        return self.next(1) != 0

    def nextFloat(self) -> float:
        return self.next(24) / (float(1 << 24))

    def nextDouble(self) -> float:
        return ((int(self.next(26)) << 27) + self.next(27)) * self.DOUBLE_UNIT
