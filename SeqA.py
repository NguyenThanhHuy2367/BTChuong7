import random
def ngaunhien(N):
  seqA = []
  for i in range(N):
    dulieu = random.choice(['int', 'float'])          
    if dulieu == 'int':   
      so = random.randint(-79, 39)
    else:
      so = round(random.uniform(-79, 39), 2)
      seqA.append(so)
      return seqA
N = random.randint(30, 80)
seqA = ngaunhien(N)
print("Danh sách ngẫu nhiên:", seqA)        

def kiem_tra_kieu_du_lieu(danh_sach):
  for i, phan_tu in enumerate(danh_sach):
    print(f"Phần tử thứ {i+1}: {phan_tu}, Kiểu dữ liệu: {type(phan_tu)}")
    
def thong_ke_so_luong(danh_sach):
      return len(danh_sach) 
  
def sap_xep_tang_dan(danh_sach):
      danh_sach_sap_xep = sorted(danh_sach)
      return danh_sach_sap_xep
  
def tinh_trung_binh(danh_sach):
  if len(danh_sach) == 0:
    return None  
  else:
    tong = sum(danh_sach)
    trung_binh = tong / len(danh_sach)
    return trung_binh