# module
import geocoder,os,sys,time

os.system("clear")
os.system("figlet LACAK-V1")
print("==============================================")
teks = input("masukin ip lacak: ")

xy = geocoder.ip(teks)
time.sleep(3)
print(xy.json)
# module
os.system("clear")
# hasil lacak
os.system("figlet lokasi..")
print("Address   : ",xy.address)
print("kota      : ",xy.city)
print("Negara    : ",xy.country)
print("IP Address: ",xy.ip)
print("latitude  : ",xy.lat)
print("Longtitude: ",xy.lng)
print("ok        : ",xy.ok)
print("organisasi: ",xy.org)
