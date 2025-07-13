class Siswa:

    def __init__(self, year, school, grade = "7 smp"):
        self.year = year
        self.school = school
        self.grade = grade
        

    def info(self):
        print("Kias adalah murid tahun", self.year)
        print("dia bersekolah di ", self.school)
        print("Kias sekarang kelas", self.grade)


siswa = Siswa(year=2025, school="SMPN1")
siswa.info()
siswa.year = "2025"