from experta.fact import Fact
from experta import KnowledgeEngine, Rule

class Gejala(Fact):
    pass

class DogCareExpert(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.diagnosed = False

    @Rule(Gejala(agresif=True), Gejala(air_liur_berlebih=True))
    def rabies(self):
        self.diagnosed = True
        print("\nDIAGNOSIS: RABIES")
        print("Saran: Segera bawa anjing ke dokter hewan.")

    @Rule(Gejala(demam=True), Gejala(batuk=True))
    def distemper(self):
        self.diagnosed = True
        print("\nDIAGNOSIS: CANINE DISTEMPER")
        print("Saran: Isolasi anjing dan lakukan pemeriksaan medis.")

    @Rule(Gejala(gatal=True), Gejala(rontok_bulu=True))
    def skabies(self):
        self.diagnosed = True
        print("\nDIAGNOSIS: SKABIES")
        print("Saran: Jaga kebersihan dan lakukan perawatan kulit.")

    @Rule(
        Gejala(air_liur_berlebih=False),
        Gejala(batuk=False),
        Gejala(gatal=False),
        Gejala(rontok_bulu=False)
    )
    def tidak_terdiagnosis(self):
        print("\nDIAGNOSIS: TIDAK TERDETEKSI PENYAKIT")
        print("Saran: Anjing dalam kondisi normal atau gejala belum cukup.")        


def yn(j):
    return j.lower() == 'y'


if __name__ == "__main__":
    print("=== SISTEM PAKAR DOGCARE ===\n")

    mulai = input("Mulai sistem? (y): ").lower()
    if mulai != 'y':
        print("Sistem tidak dijalankan.")
        exit()

    nama_pemilik = input("Nama pemilik: ")
    no_telp = input("No. Telepon: ")
    nama_anjing = input("Nama anjing: ")
    umur = input("Umur anjing (tahun): ")

    print("\nJawab gejala dengan y / t\n")

    engine = DogCareExpert()
    engine.reset()

    engine.declare(Gejala(
        agresif=yn(input("Anjing agresif? ")),
        air_liur_berlebih=yn(input("Air liur berlebihan? ")),
        demam=yn(input("Demam? ")),
        batuk=yn(input("Batuk? ")),
        gatal=yn(input("Sering menggaruk? ")),
        rontok_bulu=yn(input("Bulu rontok? "))
    ))

    print("\n--- DATA PASIEN ---")
    print(f"Pemilik     : {nama_pemilik}")
    print(f"No. Telp    : {no_telp}")
    print(f"Nama Anjing : {nama_anjing}")
    print(f"Umur        : {umur} tahun")

    engine.run()
if not engine.diagnosed:
    print("\nDIAGNOSIS: TIDAK DAPAT DITENTUKAN")
    print("Keterangan: Gejala tidak cukup atau tidak sesuai aturan penyakit.")