import re
import math

pdb = open("data/3W8W.pdb", "r")

results = open("results/3W8W_result.txt", "w")

# רשימה שתשמור את מיקום כל האטומים (x,y,z)
atoms = []

# מעבר על הקובץ שורה שורה
for line in pdb:
    if line.startswith("ATOM"):
        # בודקים שהאטום שייך לשרשרת A
        if line[21] == "A":
            numbers = re.findall(r"-?\d+\.\d+", line)
            # שלושת המספרים האחרונים הם הקואורדינטות X,Y,Z
            x = float(numbers[-3])
            y = float(numbers[-2])
            z = float(numbers[-1])
            # מוסיפים את האטום לרשימה
            atoms.append((x, y, z))


max_distance = 0

# חישוב המרחק בין כל שני אטומים
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):

        # הפרש בין הקואורדינטות
        dx = atoms[i][0] - atoms[j][0]
        dy = atoms[i][1] - atoms[j][1]
        dz = atoms[i][2] - atoms[j][2]

        distance = math.sqrt(dx*dx + dy*dy + dz*dz)

        # אם מצאנו מרחק גדול יותר, נשמור אותו
        if distance > max_distance:
            max_distance = distance


# כתיבת התוצאה לקובץ
results.write("Maximum distance in chain A:\n")
results.write(str(max_distance) + " Angstrom")

# סגירת הקבצים
pdb.close()
results.close()