per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
money = float(input("deposit amount"))
deposit_TKB = int((money/100) * (per_cent['TKB']))
deposit_SKB = int((money/100) * (per_cent['SKB']))
deposit_VTB = int((money/100) * (per_cent['VTB']))
deposit_SBER = int((money/100) * (per_cent['SBER']))
deposit = deposit_TKB, deposit_SKB, deposit_VTB, deposit_SBER
print("TKB", "SKB", "VTB", "SBER", deposit)
max_deposit = max(deposit)
print("Max deposit", max_deposit)




