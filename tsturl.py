#This code is for taking URLs and printing their status code.
import sys
import requests
file_name = sys.argv[1]
fwrite=open('/home/Arch0/Documents/lern/report.csv','w') 
fopen=open(file_name, 'r')
counter = 0
for x in fopen.readlines():
    counter = counter + 1
    url = x.strip('\n')
    req = requests.get(url)
    try:
        req = requests.get(url)
        success = 'true'
    except Exception as e:
       (print (e))
    success = 'false'
    if (success == 'false'):
        (print ( '[-] ' + url.strip('\n') + ',' + ',' + '\n'))
        fwrite.write('[-],' + str(counter) +',' + url.strip('\n') + 'No Result' + ',' + '\n')
    else:
        if (req.status_code == 200):
            (print ('[+] ' + url.strip('\n') + ',' + str(req.status_code) + ',' + '\n'))
            fwrite.write('[+],' + str(counter) + ',' + url.strip('\n') + ',' + str(req.status_code) + ',' + '\n')
        else:
            (print ('[-] ' + url.strip('\n') + ',' + str(req.status_code) + ',' + '\n'))
            fwrite.write('[-],' + str(counter) +',' + url.strip('\n') + ',' + str(req.status_code) + ',' + '\n')
fwrite.close()
fopen.close()

:!q

