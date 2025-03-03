def is_valid(bits, S):
    if bits == "":
        return True  
    for s in S:
        if bits.startswith(s):  
            if is_valid(bits[len(s):], S):  
                return True
    return False 

S = {"00", "10", "010", "01001"}

test_bits = input("Masukkan Binary yang akan di check : ")
print(is_valid(test_bits, S))  
