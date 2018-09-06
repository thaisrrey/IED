from Parameters import Parameters
from Meters import Meters
import time


class IED(Parameters, Meters):
    def __init__(self, id_ied, equipament_type, num_factors, VA, VB, VC, VN, VG, IA, IB, IC, IN, IG, on_off):
        Parameters.__init__(self, id_ied, equipament_type, num_factors)
        Meters.__init__(self, VA, VB, VC, VN, VG, IA, IB, IC, IN, IG, on_off)
        Meters.on(self)
        Meters.off(self)


f = open('C:/IED/IED/leitor.txt', 'r')
id = f.readline()
ty = f.readline()
elements = f.readline()
p = []
elements = int(elements)
while 1:
    i = 0
    while i < elements:
        p.append(f.readline())
        i = i + 1

    time.sleep(1)
    break

print(p)

f.close()
ied = IED(id, ty, elements, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, False)
print(ied.id_ied, ied.equipament_type, ied.num_factors)
