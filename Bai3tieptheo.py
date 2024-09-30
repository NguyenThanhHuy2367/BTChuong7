# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:31:37 2024

@author: NGUYEN THANH HUY
"""

def trung_binh_giua(seq):
  n = len(seq)
  if n % 2 == 0:  
    return (seq[n//2 - 1] + seq[n//2]) / 2
  else: 
    return seq[n//2]
def khoang_cach_max_min(seq):
  return max(seq) - min(seq)
ket_qua_cau_5 = 10
def so_sanh_ket_qua(trung_binh, ket_qua_cau_5):
  if trung_binh > ket_qua_cau_5:
    print("Giá trị trung bình lớn hơn kết quả câu 5.")
  elif trung_binh < ket_qua_cau_5:
    print("Giá trị trung bình nhỏ hơn kết quả câu 5.")
  else:
    print("Giá trị trung bình bằng kết quả câu 5.")
seqA = [1,9]
seqB = [2, 4, 6, 8]
trung_binh_A = trung_binh_giua(seqA)
trung_binh_B = trung_binh_giua(seqB)

khoang_cach_A = khoang_cach_max_min(seqA)
khoang_cach_B = khoang_cach_max_min(seqB)

print("Trung bình giữa của seqA:", trung_binh_A)
print("Trung bình giữa của seqB:", trung_binh_B)
print("Khoảng cách max-min của seqA:", khoang_cach_A)
print("Khoảng cách max-min của seqB:", khoang_cach_B)

so_sanh_ket_qua(trung_binh_A, ket_qua_cau_5)