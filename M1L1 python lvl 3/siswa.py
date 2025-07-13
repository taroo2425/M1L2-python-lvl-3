class Siswa:

    nama = "nama"
    asal = "asal"
    hobi = "hobi"
    persona = "persona"

    def study(self):
        print("belajar")
    
    def play(self):
        print("bermain")

    def about_siswa(self):
        print("nama siswa: ", self.nama, ", siswa tersebut berasal dari: ", self.asal, "hobi siswa tersbut: ", self.hobi, "MBTI siswi tersebut: ", self.persona)

siswa = Siswa()

print(siswa.nama)
print(siswa.asal)
print(siswa.hobi)
print(siswa.persona)

siswa.nama = "kias"
siswa.asal = "Jawa Timur"
siswa.hobi = "membaca"
siswa.persona = "ENTP"

siswa.study()
siswa.play()
siswa.about_siswa()
