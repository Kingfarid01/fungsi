'''
Fungsi menghitung nilai akhir
'''
def htg_nilai(tugas,uts,uas):
  na = 0.25 * tugas + 0.3 * uts + 0.45 * uas
  return na

na_deri = htg_nilai(80,90,100)
na_iwan = htg_nilai(50,70,100)
print(htg_nilai(80,90,100), na_deri)

'''
Fungsi menghitung nilai akhir
'''
def htg_nilai(tugas,uts,uas):
  na = 0.25 * tugas + 0.3 * uts + 0.45 * uas
  return na

'''
Fungsi menghitung grade dari nilai akhir
'''
def htg_grade(nilai):
  grade = "E"
  if nilai >= 85:
    grade = "A"
  elif nilai >= 70:
    grade = "B"
  elif nilai >= 55:
    grade = "C"
  elif nilai >= 40:
    grade = "D"
  return grade

na_deri = htg_nilai(80,90,100)
na_iwan = htg_nilai(50,70,100)
print(f"Nilai akhir deri {na_deri}, grade {htg_grade(na_deri)}")
print(f"Nilai akhir deri {na_iwan}, grade {htg_grade(na_iwan)}")
