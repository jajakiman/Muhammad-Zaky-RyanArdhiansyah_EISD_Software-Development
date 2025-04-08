def palindrom(kalimat):
    cek_palindrom = ''.join(char.lower() for char in kalimat if char.isalnum())
    return "eureeka!" if cek_palindrom == cek_palindrom[::-1] else "suka blyat"

print("Angsa:", palindrom("Angsa"))
print("KataK:", palindrom("KataK"))  
print("kasur empuk:", palindrom("kasur empuk"))
print("Aku Suka Kamu:", palindrom("Aku Suka Kamu"))  
print("Ibu Ratna antar ubi.:", palindrom("Ibu Ratna antar ubi."))