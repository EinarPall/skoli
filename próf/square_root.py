## square root

import math

start_int = float(input("Input starting integer: "))

if start_int >= 2:
    output = start_int**(1/2)
    round_output = round(output,4)
    print(round_output)
    while output > 2:
        output = output**(1/2)
        round_output = round(output,4)
        print(round_output)





























