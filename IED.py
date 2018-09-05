from Parameters import Parameters
from Meters import Meters


class IED(Parameters, Meters):
    def __init__(self, id_ied, equipament_type, num_factors, VA, VB, VC, VN, VG, IA, IB, IC, IN, IG, on_off):
        Parameters.__init__(self, id_ied, equipament_type, num_factors)
        Meters.__init__(self, VA, VB, VC, VN, VG, IA, IB, IC, IN, IG, on_off)
        Meters.on(self)
        Meters.off(self)


ied = IED(1, 'chave', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, False)

f = open('', 'r')
