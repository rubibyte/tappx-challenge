kata = (2019, 9, 25, 3, 30)

date = f"{str(kata[1]).zfill(2)}/{str(kata[2]).zfill(2)}/{str(kata[0])}"
time = f"{str(kata[3]).zfill(2)}:{str(kata[4]).zfill(2)}"

print(f"{date} {time}")
