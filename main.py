# 1
d = {}
print(f"{d}")
# 2
talaba = {"ism": "Ali",
          "yosh": 20,
          "shahar": "Toshkent"}
# 3
talaba = {"ism": "Sardor",
          "yosh": 22,
          "shahar": "Samarqand"}

print(talaba["ism"])
# 4
talaba = {"ism": "Malika",
          "yosh": 19,
          "shahar": "Buxoro",
          "telefon": "+998901234567"}

print(talaba["telefon"])
# 5
talaba = {"ism": "Jasur",
          "yosh": 21,
          "shahar": "Namangan"}
talaba["yosh"] = 23
print(talaba)
# 6
talaba = {"ism": "Dilnoza",
          "yosh": 20,
          "shahar": "Andijon",
          "kurs": 2}

del talaba["shahar"]
print(talaba)
# 7
meva = {"olma": 15000,
        "nok": 12000,
        "uzum": 20000,
        "shaftoli": 18000}

print(meva)
print(meva.keys())
# 8
meva = {"olma": 15000,
        "nok": 12000,
        "uzum": 20000,
        "shaftoli": 18000}

print(meva)
print(meva.values())
# 9
kitob = {"nomi": "O'tkan kunlar",
         "muallif": "Abdulla Qodiriy",
         "yil": 1925,
         "sahifa": 320}
print(kitob)
print(kitob.items())
# 10
kitob = {"nomi": "Mehrobdan chayon",
         "muallif": "Abdulla Qahhor",
         "sahifa": 280}
print("muallif" in kitob)
# 11
rang = {"qizil": "red",
        "ko'k": "blue",
        "yashil": "green",
        "sariq": "yellow",
        "qora": "black"
}
print(rang)
print(len(rang))
# 12
foydalanuvchi = {"ism": "Aziza",
                 "yosh": 25,
                 "shahar": "Farg'ona"
}

print(foydalanuvchi)

print(foydalanuvchi.get('Email', "Email topilmadi."))
# 13
mahsulot = {"nomi": "Telefon",
            "brend": "Samsung",
            "narx": 3500000,
            "rang": "qora"}

print(mahsulot.pop(""))
# 14
sozlamalar = {"til": "uz",
              "rang_rejim": "tungi",
              "shrift": "14px",
              "ovoz": True}
print(sozlamalar.clear())
# 15
asl_dict = {"a": 1,
            "b": 2,
            "c": 3,
            "d": 4}

print(asl_dict.copy())
# 16
maktab = {
    "10-A": {"o'quvchilar": 25,
             "sinf_rahbar": "Olimova N."},
    "10-B": {"o'quvchilar": 28,
             "sinf_rahbar": "Karimov S."},
    "11-A": {"o'quvchilar": 22,
             "sinf_rahbar": "Rahimova D."}
}

print(maktab)
# 17-m
maktab = {
    "10-A": {"o'quvchilar": 25,
             "sinf_rahbar": "Olimova N."},
    "10-B": {"o'quvchilar": 28,
             "sinf_rahbar": "Karimov S."}
}

print(maktab)

print(len(maktab['10-A']))
# 18-m
dict1 = {"a": 1,
         "b": 2,
         "c": 3}
dict2 = {"c": 10,
         "d": 4,
         "e": 5
}

print(dict1)
# 19
davlatlar = {"UZ": "O'zbekiston",
             "RU": "Rossiya",
             "US": "Amerika",
             "TR": "Turkiya"}
for davlatlar in davlatlar:
    print(davlatlar)
# 20
baholar = {"Matematika": 5,
           "Fizika": 4,
           "Kimyo": 5,
           "Biologiya": 4,
           "Tarix": 5}

print(baholar.items())
# 21
shaxs = {"ism": "Jamshid",
         "yosh": 21,
         "shahar": "Xorazm",
         "Talaba": "kasb"}
print(shaxs)
print(shaxs.setdefault("kasb"))
# 22
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

print(dict1, dict2, dict3)

birlashtirilgan = {**dict1, **dict2, **dict3}

print(birlashtirilgan)
# 23-m
talaba = {
    "ism": "Nodira",
    "familiya": "Rahimova",
    "yosh": 20,
    "kurs": 3,
    "fakultet": "Dasturiy injiniring",
    "stipendiya": True
}

print(talaba)
# 24
narxlar = {
    "Non": 3000,
    "Sut": 9000,
    "Tuxum": 18000,
    "Go'sht": 85000,
    "Yog'": 45000,
    "Sabzi": 7000
}
print(narxlar)
print(max(narxlar))
# 25
matn = "salom dunyo salom python python python dunyo"


print(f"salom soni: {matn.count("salom")}")
print(f"dunyo soni: {matn.count("dunyo")}")
print(f"python soni: {matn.count("python")}")
