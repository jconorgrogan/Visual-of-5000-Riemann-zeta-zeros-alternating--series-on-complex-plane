#!/usr/bin/env python3
"""
Compute high-precision Riemann zeta zeros 201-2200 (2000 zeros) with 25-digit precision.
"""

from mpmath import mp, zetazero

# Set precision high enough for 25 decimal digits
mp.dps = 30

print("Computing zeros 201-2200 (2000 zeros)...")
print("This will take about 3-4 minutes...")

zeros = []
for n in range(201, 2201):
    if (n - 200) % 100 == 0:
        print(f"Completed {n-200}/2000 zeros", flush=True)

    zero_im = zetazero(n)
    # Convert to string with 25 digits after decimal
    zero_str = mp.nstr(zero_im, 26, strip_zeros=False)
    zeros.append(zero_str)

# Save to file
output_file = "/Users/computer/Tensor/zeros_201_2200.txt"
with open(output_file, 'w') as f:
    for i, zero in enumerate(zeros, start=201):
        f.write(f'      "{zero}",\n')

print(f"\nCompleted! Saved {len(zeros)} zeros to {output_file}")
print(f"First few zeros:")
for i in range(min(5, len(zeros))):
    print(f"  Zero {201+i}: {zeros[i]}")
