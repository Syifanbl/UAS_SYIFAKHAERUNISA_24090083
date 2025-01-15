

import data as df

def main():

    data = {}
    Nama = ["Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    Algoritma_dan_Struktur_Data  = [90, 50, 65],
    Matematika_Numerik = [80, 60, 70]

    df = df.DataFrame(data)

    rata_per_mata_kuliah = df.iloc[1:].mean()
    print("Rata-rata setiap mata kuliah :")
    print(rata_per_mata_kuliah)

    rata_per_mahasiswa = df.iloc[1:].mean(axis=1)
    print("Rata-rata nilai setiap mahasiswa :")
    for nama,rata in zip(df["Nama"],rata_per_mahasiswa):
        print(f"{nama}: {rata:2}")

if _name_ == "_main_":
    main()