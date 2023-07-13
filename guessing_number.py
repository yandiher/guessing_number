print('pikirin angka dari satu sampai seratus')
nanya = input('udah? ')

# category 64
print(64,81,82,65,66,69,70,71,72,73)
print(74,78,79,75,76,77,84,85,86,87)
print(80,83,88,89,90,67,68,91,92,93)
print(88,89,95,96,90,92,93,91,94,97)
print(98,99,100)

category_64 = input('ada nomer yang elu pilih ga? (yes/no) ')

# category 32
print(32,35,36,37,38,39,96,97,40,41)
print(42,44,47,43,60,45,52,53,54,55)
print(48,49,46,50,33,34,51,98,99,100)
print(56,61,57,59,62,58,63)

category_32 = input('ada nomer yang elu pilih ga? (yes/no) ')

# category 16
print(16,18,92,17,93,95,23,94,24,25)
print(26,31,27,29,30,48,28,50,51,49)
print(52,59,53,56,54,55,60,57,58,61)
print(62,80,81,63,82,84,85,83,86,87)
print(88,20,89,22,90,91,19,21)

category_16 = input('ada nomer yang elu pilih ga? (yes/no) ')

# category 8
print(8,12,13,14,15,47,56,59,24,25,26)
print(27,28,29,30,31,40,41,42,43,44)
print(45,9,10,11,46,57,58,60,61,62)
print(63,72,74,75,78,76,73,77,79,88,)
print(89,90,91,92,93,94,95)

category_8 = input('ada nomer yang elu pilih ga? (yes/no) ')

# category 4
print(4,5,6,7,12,13,14,15,20,21,22,)
print(23,28,29,30,31,36,37,38,39,44,)
print(45,46,47,52,53,54,55,60,61,62,)
print(63,68,69,70,71,76,77,78,79)
print(84,85,86,87,92,93,94,95,100)

category_4 = input('ada nomer yang elu pilih ga? (yes/no) ')

# category 2
print(2,3,6,7,10,11,14,15,98,99,47)
print(18,19,22,23,26,27,30,31,54,55,)
print(34,35,38,39,42,43,46,50,51,58,)
print(59,62,63,66,67,70,71,74,75,78,)
print(79,82,83,86,87,90,91,94,95)

category_2 = input('ada nomer yang elu pilih ga? (yes/no) ')

# category 1
print(1,3,5,7,9,11,13,15,21,23,25)
print(17,19,27,29,31,33,35,37,39,97)
print(41,43,45,47,49,51,53,55,57)
print(59,61,63,65,67,69,71,73,75,99)
print(77,79,81,83,85,87,89,91,93,95)

category_1 = input('ada nomer yang elu pilih ga? (yes/no) ')

if category_64 == 'yes':
    enam_empat = 64
else:
    enam_empat = 0

if category_32 == 'yes':
    tiga_dua = 32
else:
    tiga_dua = 0
    
if category_16 == 'yes':
    enam_belas = 16
else:
    enam_belas = 0

if category_8 == 'yes':
    delapan = 8
else:
    delapan = 0

if category_4 == 'yes':
    empat = 4
else:
    empat = 0

if category_2 == 'yes':
    dua = 2
else:
    dua = 0

if category_1 == 'yes':
    satu = 1
else:
    satu = 0

hasil = enam_empat + tiga_dua + enam_belas + delapan + empat + dua + satu

print('paling ge nomer yang elu pilih', hasil, 'kan?')