#!/usr/bin/env python3
"""
Compute high-precision Riemann zeta zeros in batches.
This script computes zeros 201-10,000 with 25-digit precision.
"""

from mpmath import mp, zetazero
import json

# Set precision high enough for 25 decimal digits
mp.dps = 30

def compute_zeros_batch(start, end, batch_size=100):
    """Compute zeros in batches to show progress"""
    all_zeros = []

    for batch_start in range(start, end + 1, batch_size):
        batch_end = min(batch_start + batch_size - 1, end)
        print(f"Computing zeros {batch_start}-{batch_end}...", flush=True)

        batch_zeros = []
        for n in range(batch_start, batch_end + 1):
            zero_im = zetazero(n)
            # Convert to string with 25 digits after decimal
            zero_str = mp.nstr(zero_im, 26, strip_zeros=False)
            batch_zeros.append(zero_str)

        all_zeros.extend(batch_zeros)
        print(f"  Completed {len(all_zeros)}/{end - start + 1} zeros", flush=True)

    return all_zeros

# Compute zeros 201-10000
print("Starting computation of zeros 201-10,000...")
print("This will take several minutes...")
zeros = compute_zeros_batch(201, 10000, batch_size=100)

# Save to file
output_file = "/Users/computer/Tensor/zeros_201_10000.txt"
with open(output_file, 'w') as f:
    for i, zero in enumerate(zeros, start=201):
        f.write(f'      "{zero}",\n')

print(f"\nCompleted! Saved {len(zeros)} zeros to {output_file}")
print(f"First few zeros:")
for i in range(min(5, len(zeros))):
    print(f"  Zero {201+i}: {zeros[i]}")
