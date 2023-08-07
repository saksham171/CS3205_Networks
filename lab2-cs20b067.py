import os
import sys
import socket

# NAME: Saksham Singh
# Roll Number: CS20B067
# Course: CS3205 Jan. 2023 semester
# Lab number: 2
# Date of submission: 02/03/2023
# I confirm that the source file is entirely written by me without
# resorting to any dishonest means.
# Website(s) that I used for basic socket programming code are:
# URL(s): StackOverflow, Python Documentation

# Global Variables
ADS1_websites = {}
ADS2_websites = {}
ADS3_websites = {}
ADS4_websites = {}
ADS5_websites = {}
ADS6_websites = {}


def client():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while(1):        
        website = input("Enter Server Name: ")
        if website == "bye":
            clientSocket.sendto(str.encode(website), (NR_ip, startPort + 53))
            print("All Server Processes are killed. Exiting.")
            break
        else:
            clientSocket.sendto(str.encode(website), (NR_ip, startPort + 53))
            ret = clientSocket.recvfrom(100)
            if(ret[0].decode() == "NOPE"):
                print("No DNS record found.\n")
            else:
                print("DNS Mapping: " + ret[0].decode())

def NameResolver():
    NRsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    NRsocket.bind((NR_ip, startPort + 53))
    while(1):
        recv = NRsocket.recvfrom(1024)
        website = recv[0]
        clientIP = recv[1]
        f = open("NR.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            NRsocket.sendto("bye".encode(), (Root_ip, startPort + 54))
            NRsocket.sendto("bye".encode(), (TDS_com_ip, startPort + 55))
            NRsocket.sendto("bye".encode(), (TDS_edu_ip, startPort + 56))
            NRsocket.sendto("bye".encode(), (ADS1_ip, startPort + 57))
            NRsocket.sendto("bye".encode(), (ADS2_ip, startPort + 58))
            NRsocket.sendto("bye".encode(), (ADS3_ip, startPort + 59))
            NRsocket.sendto("bye".encode(), (ADS4_ip, startPort + 60))
            NRsocket.sendto("bye".encode(), (ADS5_ip, startPort + 61))
            NRsocket.sendto("bye".encode(), (ADS6_ip, startPort + 62))
            #close log file
            f.close()
            break
        NRsocket.sendto(website, (Root_ip, startPort + 54))
        domain = NRsocket.recvfrom(100)
        if domain[0].decode() == ".com":
            NRsocket.sendto(website, (TDS_com_ip, startPort + 55))
            ads = NRsocket.recvfrom(100)
            if ads[0].decode() == "ADS1":
                NRsocket.sendto(website, (ADS1_ip, startPort + 57))
                ret = NRsocket.recvfrom(100)
                log = "Response: " + ret[0].decode()
                f.write(log)
                f.close()
                NRsocket.sendto(ret[0], clientIP)
            elif ads[0].decode() == "ADS2":
                NRsocket.sendto(website, (ADS2_ip, startPort + 58))
                ret = NRsocket.recvfrom(100)
                log = "Response: " + ret[0].decode()
                f.write(log)
                f.close()
                NRsocket.sendto(ret[0], clientIP)
            elif ads[0].decode() == "ADS3":
                NRsocket.sendto(website, (ADS3_ip, startPort + 59))
                ret = NRsocket.recvfrom(100)
                log = "Response: " + ret[0].decode()
                f.write(log)
                f.close()
                NRsocket.sendto(ret[0], clientIP)
            else:
                log = "Response: NOPE\n"
                f.write(log)
                f.close()
                NRsocket.sendto("NOPE".encode(), clientIP)
        elif domain[0].decode() == ".edu":
            NRsocket.sendto(website, (TDS_edu_ip, startPort + 56))
            ads = NRsocket.recvfrom(100)
            if ads[0].decode() == "ADS4":
                NRsocket.sendto(website, (ADS4_ip, startPort + 60))
                ret = NRsocket.recvfrom(100)
                log = "Response: " + ret[0].decode()
                f.write(log)
                f.close()
                NRsocket.sendto(ret[0], clientIP)
            elif ads[0].decode() == "ADS5":
                NRsocket.sendto(website, (ADS5_ip, startPort + 61))
                ret = NRsocket.recvfrom(100)
                log = "Response: " + ret[0].decode()
                f.write(log)
                f.close()
                NRsocket.sendto(ret[0], clientIP)
            elif ads[0].decode() == "ADS6":
                NRsocket.sendto(website, (ADS6_ip, startPort + 62))
                ret = NRsocket.recvfrom(100)
                log = "Response: " + ret[0].decode()
                f.write(log)
                f.close()
                NRsocket.sendto(ret[0], clientIP)
            else:
                log = "Response: NOPE\n"
                f.write(log)
                f.close()
                NRsocket.sendto("NOPE".encode(), clientIP)
        else:
            log = "Response: NOPE\n"
            f.write(log)
            f.close()
            NRsocket.sendto("NOPE".encode(), clientIP)

def RootDNS():
    Rootsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Rootsocket.bind((Root_ip, startPort + 54))
    while(1):
        recv = Rootsocket.recvfrom(1024)
        website = recv[0]
        NR_IP = recv[1]
        f = open("RDS.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            f.close()
            break
        if website.find('.com'.encode()) != -1:
            log = "Response: .com " + TDS_com_ip
            f.write(log)
            f.write("\n")
            f.close()
            Rootsocket.sendto(".com".encode(), NR_IP)
        elif website.find('.edu'.encode()) != -1:
            log = "Response: .edu " + TDS_edu_ip
            f.write(log)
            f.write("\n")
            f.close()
            Rootsocket.sendto(".edu".encode(), NR_IP)
        else:
            log = "Response: NOPE"
            f.write(log)
            f.write("\n")
            f.close()
            Rootsocket.sendto("NOPE".encode(), NR_IP)

def TDS_com():
    TDScom_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    TDScom_socket.bind((TDS_com_ip, startPort + 55))
    while(1):
        recv = TDScom_socket.recvfrom(1024)
        website = recv[0]
        NR_IP = recv[1]
        f = open("TDS_com.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            f.close()
            break
        if website.find(ADS1_company.encode()) != -1:
            log = "Response: ADS1 " + ADS1_ip
            f.write(log)
            f.write("\n")
            f.close()
            TDScom_socket.sendto("ADS1".encode(), NR_IP)
        elif website.find(ADS2_company.encode()) != -1:
            log = "Response: ADS2 " + ADS2_ip
            f.write(log)
            f.write("\n")
            f.close()
            TDScom_socket.sendto("ADS2".encode(), NR_IP)
        elif website.find(ADS3_company.encode()) != -1:
            log = "Response: ADS3 " + ADS3_ip
            f.write(log)
            f.write("\n")
            f.close()
            TDScom_socket.sendto("ADS3".encode(), NR_IP)
        else:
            log = "Response: NOPE"
            f.write(log)
            f.write("\n")
            f.close()
            TDScom_socket.sendto("NOPE".encode(), NR_IP)

def TDS_edu():
    TDSedu_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    TDSedu_socket.bind((TDS_edu_ip, startPort + 56))
    while(1):
        recv = TDSedu_socket.recvfrom(1024)
        website = recv[0]
        NR_IP = recv[1]
        f = open("TDS_edu.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            f.close()
            break
        if website.find(ADS4_company.encode()) != -1:
            log = "Response: ADS4 " + ADS4_ip
            f.write(log)
            f.write("\n")
            f.close()
            TDSedu_socket.sendto("ADS4".encode(), NR_IP)
        elif website.find(ADS5_company.encode()) != -1:
            log = "Response: ADS5 " + ADS5_ip
            f.write(log)
            f.write("\n")
            f.close()
            TDSedu_socket.sendto("ADS5".encode(), NR_IP)
        elif website.find(ADS6_company.encode()) != -1:
            log = "Response: ADS6 " + ADS6_ip
            f.write(log)
            f.write("\n")
            f.close()
            TDSedu_socket.sendto("ADS6".encode(), NR_IP)
        else:
            log = "Response: NOPE"
            f.write(log)
            f.write("\n")
            f.close()
            TDSedu_socket.sendto("NOPE".encode(), NR_IP)

def ADS1():
    ADS1_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ADS1_socket.bind((ADS1_ip, startPort + 57))
    while(1):
        recv = ADS1_socket.recvfrom(1024)
        website = recv[0]
        NR_IP = recv[1]
        f = open("ADS1.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            f.close()
            break
        if ADS1_websites.get(website.decode()) != None:
            log = "Response: " + ADS1_websites.get(website.decode())
            f.write(log)
            f.close()
            ADS1_socket.sendto(ADS1_websites.get(website.decode()).encode(), NR_IP)
        else:
            log = "Response: NOPE"
            f.write(log)
            f.close()
            ADS1_socket.sendto("NOPE".encode(), NR_IP)

def ADS2():
    ADS2_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ADS2_socket.bind((ADS2_ip, startPort + 58))
    while(1):
        recv = ADS2_socket.recvfrom(1024)
        website = recv[0]
        NR_IP = recv[1]
        f = open("ADS2.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            f.close()
            break
        if ADS2_websites.get(website.decode()) != None:
            log = "Response: " + ADS2_websites.get(website.decode())
            f.write(log)
            f.close()
            ADS2_socket.sendto(ADS2_websites.get(website.decode()).encode(), NR_IP)
        else:
            log = "Response: NOPE"
            f.write(log)
            f.close()
            ADS2_socket.sendto("NOPE".encode(), NR_IP)

def ADS3():
    ADS3_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ADS3_socket.bind((ADS3_ip, startPort + 59))
    while(1):
        recv = ADS3_socket.recvfrom(1024)
        website = recv[0]
        NR_IP = recv[1]
        f = open("ADS3.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            f.close()
            break
        if ADS3_websites.get(website.decode()) != None:
            log = "Response: " + ADS3_websites.get(website.decode())
            f.write(log)
            f.close()
            ADS3_socket.sendto(ADS3_websites.get(website.decode()).encode(), NR_IP)
        else:
            log = "Response: NOPE"
            f.write(log)
            f.close()
            ADS3_socket.sendto("NOPE".encode(), NR_IP)

def ADS4():
    ADS4_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ADS4_socket.bind((ADS4_ip, startPort + 60))
    while(1):
        recv = ADS4_socket.recvfrom(1024)
        website = recv[0]
        NR_IP = recv[1]
        f = open("ADS4.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            f.close()
            break
        if ADS4_websites.get(website.decode()) != None:
            log = "Response: " + ADS4_websites.get(website.decode())
            f.write(log)
            f.close()
            ADS4_socket.sendto(ADS4_websites.get(website.decode()).encode(), NR_IP)
        else:
            log = "Response: NOPE"
            f.write(log)
            f.close()
            ADS4_socket.sendto("NOPE".encode(), NR_IP)

def ADS5():
    ADS5_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ADS5_socket.bind((ADS5_ip, startPort + 61))
    while(1):
        recv = ADS5_socket.recvfrom(1024)
        website = recv[0]
        NR_IP = recv[1]
        f = open("ADS5.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            f.close()
            break
        if ADS5_websites.get(website.decode()) != None:
            log = "Response: " + ADS5_websites.get(website.decode())
            f.write(log)
            f.close()
            ADS5_socket.sendto(ADS5_websites.get(website.decode()).encode(), NR_IP)
        else:
            log = "Response: NOPE"
            f.write(log)
            f.close()
            ADS5_socket.sendto("NOPE".encode(), NR_IP)

def ADS6():
    ADS6_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ADS6_socket.bind((ADS6_ip, startPort + 62))
    while(1):
        recv = ADS6_socket.recvfrom(1024)
        website = recv[0]
        NR_IP = recv[1]
        f = open("ADS6.output", "a")
        log = "Query: " + website.decode() + " "
        f.write(log)
        if website.decode() == "bye":
            f.close()
            break
        if ADS6_websites.get(website.decode()) != None:
            log = "Response: " + ADS6_websites.get(website.decode())
            f.write(log)
            f.close()
            ADS6_socket.sendto(ADS6_websites.get(website.decode()).encode(), NR_IP)
        else:
            log = "Response: NOPE"
            f.write(log)
            f.close()
            ADS6_socket.sendto("NOPE".encode(), NR_IP)

def PrintDetails():
    print("NR: " + NR_ip)
    print("Root: " + Root_ip)
    print("TDS_com: " + TDS_com_ip)
    print("TDS_edu: " + TDS_edu_ip)
    print("ADS1: " + ADS1_ip)
    print("ADS2: " + ADS2_ip)
    print("ADS3: " + ADS3_ip)
    print("ADS4: " + ADS4_ip)
    print("ADS5: " + ADS5_ip)
    print("ADS6: " + ADS6_ip)
    print("List of ADS1: ")
    for key in ADS1_websites:
        print(key + " " + ADS1_websites.get(key))

startPorttmp = sys.argv[1]
startPort = int(startPorttmp)
fileName = sys.argv[-1]
# print("Start Port: " + startPorttmp)
# print("File Name: " + fileName)

# read the file
count = 1
file = open(fileName, "r")
for line in file:
    line = line.strip().split()
    #print(line)
    if line[0] == 'BEGIN_DATA':
        #print("File Read")
        continue
    elif line[0] == 'END_DATA':
        break
    elif line[0] == 'NR':
        NR_ip = line[1]
    elif line[0] == 'RDS':
        Root_ip = line[1]
    elif line[0] == 'TDS_com':
        TDS_com_ip = line[1]
    elif line[0] == 'TDS_edu':
        TDS_edu_ip = line[1]
    elif line[0] == 'List_of_ADS1':
        for i in range(5):
            line = next(file)
            if i == 0:
                tmp = line.split(" ")[0]
                ADS1_company = tmp.split(".")[1]
                #print("ADS1_company: " + ADS1_company)
            ADS1_websites[line.split(" ")[0]] = line.split(" ")[1]
    elif line[0] == 'List_of_ADS2':
        for i in range(5):
            line = next(file)
            if i == 0:
                tmp = line.split(" ")[0]
                ADS2_company = tmp.split(".")[1]
                #print("ADS2_company: " + ADS2_company)
            ADS2_websites[line.split(" ")[0]] = line.split(" ")[1]
    elif line[0] == 'List_of_ADS3':
        for i in range(5):
            line = next(file)
            if i == 0:
                tmp = line.split(" ")[0]
                ADS3_company = tmp.split(".")[1]
                #print("ADS3_company: " + ADS3_company)
            ADS3_websites[line.split(" ")[0]] = line.split(" ")[1]
    elif line[0] == 'List_of_ADS4':
        for i in range(5):
            line = next(file)
            if i == 0:
                tmp = line.split(" ")[0]
                ADS4_company = tmp.split(".")[1]
                #print("ADS4_company: " + ADS4_company)
            ADS4_websites[line.split(" ")[0]] = line.split(" ")[1]
    elif line[0] == 'List_of_ADS5':
        for i in range(5):
            line = next(file)
            if i == 0:
                tmp = line.split(" ")[0]
                ADS5_company = tmp.split(".")[1]
                #print("ADS5_company: " + ADS5_company)
            ADS5_websites[line.split(" ")[0]] = line.split(" ")[1]
    elif line[0] == 'List_of_ADS6':
        for i in range(5):
            line = next(file)
            if i == 0:
                tmp = line.split(" ")[0]
                ADS6_company = tmp.split(".")[1]
                #print("ADS6_company: " + ADS6_company)
            ADS6_websites[line.split(" ")[0]] = line.split(" ")[1]
    elif count == 1:
        ADS1_ip = line[1]
        count += 1
    elif count == 2:
        ADS2_ip = line[1]
        count += 1
    elif count == 3:
        ADS3_ip = line[1]
        count += 1
    elif count == 4:
        ADS4_ip = line[1]
        count += 1
    elif count == 5:
        ADS5_ip = line[1]
        count += 1
    elif count == 6:
        ADS6_ip = line[1]
        count += 1
    else:
        print("Error")

file.close()

#PrintDetails()

# create 10 child processes
for i in range(10):
    pid = os.fork()
    if pid == 0:
        if i == 0:
            NameResolver()
        elif i == 1:
            RootDNS()
        elif i == 2:
            TDS_com()
        elif i == 3:
            TDS_edu()
        elif i == 4:
            ADS1()
        elif i == 5:
            ADS2()
        elif i == 6:
            ADS3()
        elif i == 7:
            ADS4()
        elif i == 8:
            ADS5()
        elif i == 9:
            ADS6()
        sys.exit(0)

client()
sys.exit(0)

