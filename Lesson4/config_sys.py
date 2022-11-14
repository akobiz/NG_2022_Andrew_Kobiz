import platform
import cpuinfo
import psutil

def writePCInfo(path):
    sys = platform.uname()
    with open(path, 'a', encoding = 'utf-8') as file:
        file.write("OS INFO BLOCK ----------------------------\n\n")
        file.write("System PC: " + sys.system + '\n')
        file.write("Node Name PC: " + sys.node + '\n')
        file.write("Release: " + sys.release + '\n')
        file.write("Version: " + sys.version + '\n')
        file.write("Machine: " + sys.machine + '\n\n')

def writeProccesorInfo(path):
    infoCPU = cpuinfo.get_cpu_info()
    with open(path, 'a', encoding= 'utf-8') as file:
        file.write("PROCESSOR INFO BLOCK ----------------------------\n\n")
        file.write("Proccesor Name: " + infoCPU["brand_raw"] + '\n')
        file.write("Architecture: " + infoCPU["arch"] + '\n')
        file.write("Model: " + str(infoCPU["model"]) + " and Family: " + str(infoCPU["family"]) + '\n')
        file.write("Current frequency: " + str(psutil.cpu_freq()[0]) + "hz\n\n")

def writeRamInfo(path):
    totalRam = round((psutil.virtual_memory()[0]/1000000000) - 1, 0)
    usedRam = round(psutil.virtual_memory()[-2]/1000000000, 1)
    availableRam = round((psutil.virtual_memory()[-1]/1000000000 - 1), 1)
    with open(path, "a", encoding='utf-8') as file:
        file.write("RAM INFO BLOCK ----------------------------\n\n")
        file.write("Total Ram: " + str(totalRam) + 'GB\n')
        file.write("Used RAM: " + str(usedRam) + "GB | Available RAM: " + str(availableRam) + "GB\n\n")

def writeStorageInfo(path):
    hdd = psutil.disk_usage('\\')
    with open(path, 'a', encoding='utf-8') as file:
        file.write("STORAGE INFO BLOCK ----------------------------\n\n")
        file.write("Total storage space: " + str(int(hdd.total / (2**30))) + "GB\n")
        file.write("Used storage space: " + str(int(hdd.used / (2**30))) + "GB(" + str(hdd.percent) + "%)\n")
        file.write("Free storage space: " + str(int(hdd.free / (2**30))) + "GB\n")
        for info in psutil.disk_partitions():
            file.write("Disk partitions on device: " + info.device + '\n')
            file.write("Mountpoint system: " + info.mountpoint + '\n')
            file.write("File system type: " + info.fstype + '\n\n')