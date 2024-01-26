import platform
import psutil

# İşletim sistemi bilgileri
sistem_bilgisi = {
    'OS': platform.system(),
    'OS Version': platform.version(),
    'OS Architecture': platform.architecture(),
    'OS Computer Name': platform.node(),
    'OS User Name': platform.uname(),
}

# CPU bilgileri
cpu_bilgisi = {
    'CPU Name': platform.processor(),
    'CPU Count': psutil.cpu_count(logical=False),
    'Total Numbers of Logical CPUs': psutil.cpu_count(logical=True),
    'CPU Frequence': psutil.cpu_freq(),
}

# Bellek (RAM) bilgileri
bellek_bilgisi = {
    'Total Memory': round(psutil.virtual_memory().total / (1024 ** 3), 2),  # GB cinsinden
    'Used Memory': round(psutil.virtual_memory().used / (1024 ** 3), 2),
    'Free Memory': round(psutil.virtual_memory().available / (1024 ** 3), 2),
}

# Disk bilgileri
disk_bilgisi = {
    'Total Disk Space': round(psutil.disk_usage('/').total / (1024 ** 3), 2),  # GB cinsinden
    'Used Disk Space': round(psutil.disk_usage('/').used / (1024 ** 3), 2),
    'Free Disk Space': round(psutil.disk_usage('/').free / (1024 ** 3), 2),
    'Disk Usage Rate': psutil.disk_usage('/').percent,
}

# Ağ bilgileri
ag_bilgisi = {
    'IP Address': psutil.net_if_addrs()['Ethernet'][0].address,  # Örnek olarak 'Ethernet' kullanıldı, sisteminize göre değişebilir
    'Network Speed': psutil.net_if_stats()['Ethernet'].speed,
}

# Tüm bilgileri birleştirme
tum_bilgiler = {
    'System Info': sistem_bilgisi,
    'CPU Info': cpu_bilgisi,
    'Memory Info': bellek_bilgisi,
    'Disk Info': disk_bilgisi,
    'Network Info': ag_bilgisi,
}

# Tüm bilgileri ekrana yazdırma
def all():
    for kategori, bilgiler in tum_bilgiler.items():
        print(f"{kategori}:\n{bilgiler}\n")