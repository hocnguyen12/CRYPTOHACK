"""
    Inferius Prime challenge
"""

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

n = 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

import primefac
fact = primefac.primefac(n)
#print(list(fact))

# factorization
p = 848445505077945374527983649411
q = 1160939713152385063689030212503

print(f"n : {n}")
print(f"p * q : {p * q}")

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

plaintext = pow(ct, d, n)
decrypted = long_to_bytes(plaintext)

print(f"flag : {decrypted}")
