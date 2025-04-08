def hitung_rating(ratings):
    return [min(ratings), max(ratings), round(sum(ratings) / len(ratings), 1)]

data1 = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0]
data2 = [5, 4, 2.5, 5, 3.6, 1.1, 3.6, 4, 4.2, 1.5]

print("Cek Rating Terendah, Tertinggi, Rata - Rata")
print(hitung_rating(data1)) 
print(hitung_rating(data2)) 
