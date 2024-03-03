
def cek_lulus_dan_konversi(nilai):
    if nilai > 75:
        lulus = True
    else:
        lulus = False
    
    if nilai < 50:
        grade = 'E'
    elif nilai < 60:
        grade = 'D'
    elif nilai < 70:
        grade = 'C'
    elif nilai < 80:
        grade = 'B'
    else:
        grade = 'A'
    
    return lulus, grade


def hitung_ipk(nilai_matkul):
    bobot_matkul = {
        'Algoritma': 3,
        'Perancangan Objek': 3,
        'Kalkulus': 4,
        'Etika Profesi': 2,
        'Databases': 3,
        'English 1': 2
    }
    total_bobot = 0
    total_sks = 0
    for matkul, nilai in nilai_matkul.items():
        total_bobot += nilai * bobot_matkul[matkul]
        total_sks += bobot_matkul[matkul]
    ipk = total_bobot / total_sks
    return ipk

def saran_jurusan(ipk, jenis_kelamin):
    if ipk >= 80 and jenis_kelamin == 'Laki-laki':
        return 'Teknik Informatika'
    elif ipk >= 80 and jenis_kelamin == 'Perempuan':
        return 'Sistem Informasi'
    else:
        return 'DKV'
def pendaftaran():
    nama = input("Masukkan nama: ")
    tempat_lahir = input("Masukkan tempat lahir: ")
    tanggal_lahir = int(input("Masukkan tanggal lahir: "))
    bulan_lahir = int(input("Masukkan bulan lahir: "))
    tahun_lahir = int(input("Masukkan tahun lahir: "))
    nilai_english = float(input("Masukkan nilai English: "))
    nilai_matematika = float(input("Masukkan nilai Matematika: "))
    nilai_indonesia = float(input("Masukkan nilai Bahasa Indonesia: "))
    jenis_kelamin = input("Masukkan jenis kelamin (Laki-laki/Perempuan): ")
    
    
    from datetime import datetime
    today = datetime.now()
    umur = today.year - tahun_lahir - ((today.month, today.day) < (bulan_lahir, tanggal_lahir))
    
    if umur >= 25:
        print("Maaf, Anda tidak memenuhi syarat umur untuk mendaftar.")
        return
    

    nilai_rata_rata = (nilai_english + nilai_matematika + nilai_indonesia) / 3
    

    jurusan = saran_jurusan(nilai_rata_rata, jenis_kelamin)
    
    print("\n=== Informasi Pendaftaran ===")
    print("Nama:", nama)
    print("Tempat Lahir:", tempat_lahir)
    print("Tanggal Lahir:", f"{tanggal_lahir}/{bulan_lahir}/{tahun_lahir}")
    print("Jenis Kelamin:", jenis_kelamin)
    print("Rata-rata Nilai:", nilai_rata_rata)
    print("Saran Jurusan:", jurusan)

nilai = float(input("Masukkan nilai: "))

lulus, grade = cek_lulus_dan_konversi(nilai)
print("Status Kelulusan:", "Lulus" if lulus else "Tidak Lulus")
print("Nilai konversi:", grade)

nilai_matkul = {}
for matkul in ['Algoritma', 'Perancangan Objek', 'Kalkulus', 'Etika Profesi', 'Databases', 'English 1']:
    nilai = float(input(f"Masukkan nilai untuk mata kuliah {matkul}: "))
    nilai_matkul[matkul] = nilai


ipk = hitung_ipk(nilai_matkul)
print("IPK Anda untuk semester ini:", ipk)


pendaftaran()