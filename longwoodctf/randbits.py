from random import getrandbits

phases = 8
seed = getrandbits(64 * phases)
hidden_state_1 = getrandbits(64)
hidden_state_2 = getrandbits(64)
mask_64 = (1 << 64) - 1

print(mask_64)

def draw_number():
    global phases, seed, hidden_state_1, hidden_state_2, mask_64
    result = seed & mask_64
    seed >>= 64
    refill = (result * hidden_state_1 + hidden_state_2) & mask_64
    refill ^= seed & mask_64
    seed |= refill << ((phases - 1) * 64)
    return result

def give_numbers():
    base = draw_number()
    numbers = []
    for i in range(0, 8):
        numbers += [base & 0xFF]
        base >>= 8
    return numbers

print("Numbers for the next month:")
print([give_numbers() for i in range(0, 31)])

#numbers: [156,25,149,89,246,234,241,138]