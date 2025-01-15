class Buah:
    def _init_(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setnama(self, nama):
        self.nama = nama

    def setwarna(self, warna):
        self.warna = warna

    def setrasa(self, rasa):
        self.rasa = rasa


buah1 = Buah("Apel", "Merah", "Manis")

buah1.setnama("alpukat")
buah1.setwarna("apel")
buah1.setrasa("anggur")

print(f"Nama: {buah1.nama}, Warna: {buah1.warna}, Rasa: {buah1.rasa}")