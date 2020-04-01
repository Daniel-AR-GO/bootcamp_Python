import datetime

ahora= datetime.datetime.now()

iron_man = datetime.timedelta(hours=2, minutes=6)
hulk = datetime.timedelta(hours=1, minutes=52)
iron_man2 = datetime.timedelta(hours=2, minutes=5)
thor = datetime.timedelta(hours=1, minutes=54)
cp_america = datetime.timedelta(hours=2, minutes=4)
avengers = datetime.timedelta(hours=2, minutes=23)
iron_man3 = datetime.timedelta(hours=2, minutes=11)
thor_2 = datetime.timedelta(hours=1, minutes=52)
cp_america2 = datetime.timedelta(hours=2, minutes=16)
guardians = datetime.timedelta(hours=2, minutes=2)
avengers_2 = datetime.timedelta(hours=2, minutes=21)
ant_man = datetime.timedelta(hours=1, minutes=57)
cp_america3 = datetime.timedelta(hours=2, minutes=27)
dr_strange = datetime.timedelta(hours=1, minutes=55)
guardians_2 = datetime.timedelta(hours=2, minutes=17)
spider_man = datetime.timedelta(hours=2, minutes=13)
thor_3 = datetime.timedelta(hours=2, minutes=10)
black_panther = datetime.timedelta(hours=2, minutes=14)
avengers_3 = datetime.timedelta(hours=2, minutes=40)
ant_man_wasp = datetime.timedelta(hours=2, minutes=5)
cp_marvel = datetime.timedelta(hours=2, minutes=5)
avengers_4 = datetime.timedelta(hours=3, minutes=2)

ucm = [iron_man, hulk, iron_man2, thor, cp_america, avengers, iron_man3, thor_2, cp_america2, guardians, avengers_2, ant_man, cp_america3, dr_strange, guardians_2, spider_man, thor_3, black_panther, avengers_3, ant_man_wasp, cp_marvel, avengers_4]

total = datetime.timedelta()

for peli in ucm:
    total+=peli

print(total)

hp_1 = datetime.timedelta(minutes=152)
hp_2 = datetime.timedelta(minutes=161)
hp_3 = datetime.timedelta(minutes=142)
hp_4 = datetime.timedelta(minutes=157)
hp_5 = datetime.timedelta(minutes=138)
hp_6 = datetime.timedelta(minutes=153)
hp_7 = datetime.timedelta(minutes=146)
hp_8 = datetime.timedelta(minutes=130)

universo_hp = [hp_1, hp_2, hp_3, hp_4, hp_5, hp_6, hp_7, hp_8]

for peli in universo_hp:
    total += peli

print(total)

fast_1 = datetime.timedelta(minutes=106)
fast_2 = datetime.timedelta(minutes=107)
fast_3 = datetime.timedelta(minutes=104)
fast_4 = datetime.timedelta(minutes=107)
fast_5 = datetime.timedelta(minutes=130)
fast_6 = datetime.timedelta(minutes=130)

universo_ff = [fast_1, fast_2, fast_3, fast_4, fast_5, fast_6]

for peli in universo_ff:
    total += peli

print(total)
print(ahora + total)