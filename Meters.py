class Meters(object):

    def __init__(self, VA, VB, VC, VN, VG, IA, IB, IC, IN, IG, on_off):
        self.VA = VA
        self.VB = VB
        self.VC = VC
        self.VN = VN
        self.VG = VG
        self.IA = IA
        self.IB = IB
        self.IC = IC
        self.IN = IN
        self.IG = IG
        self.on_off = on_off

    def on(self):
        self.on_off = True

    def off(self):
        self.on_off = False

    def setVA(self, new_VA):
        self.VA = new_VA

    def setVB(self, new_VB):
        self.VB = new_VB

    def setVC(self, new_VC):
        self.VC = new_VC

    def setVN(self, new_VN):
        self.VN = new_VN

    def setVG(self, new_VG):
        self.VG = new_VG

    def setIA(self, new_IA):
        self.IA = new_IA

    def setIB(self, new_IB):
        self.IB = new_IB

    def setIC(self, new_IC):
        self.IC = new_IC

    def setIN(self, new_IN):
        self.IN = new_IN

    def setIG(self, new_IG):
        self.IG = new_IG