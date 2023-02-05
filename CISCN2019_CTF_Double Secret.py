def rc4(data, key):
    S = list(range(256))
    j = 0
    out = bytearray()
    
    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(char ^ S[(S[i] + S[j]) % 256])
    
    return out

# Example usage
data = input(":")
key = "HereIsTreasure"
encrypted_data = rc4(data.encode(), key.encode())
print(encrypted_data)
#encrypt rc4 payload to ssti
