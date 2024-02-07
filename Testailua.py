# Katotaan sujuuko commit ja silleen

import random
import sys

def laskut(n):

    try:
        n = int(n)
    
    except ValueError:
        print("Anna luku")

    else:
        for _ in range(n):
            a = random.randint(1,10)
            b = random.randint(1,10)
            print(f"{a} + {b} = {a+b}")


if __name__ == "__main__":
    
    if(len(sys.argv) == 1):
        laskut(10)
    else:
        laskut(sys.argv[1])
            
