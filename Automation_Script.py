 
from sys import *
import os
import time
import psutil
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Process(FileNmae, userID):

    listprocess = []

    if not os.path.exists(FileNmae):
        try:
            os.mkdir(FileNmae)
        except:
            pass

    separator ="-" * 80
    log_path = os.path.join(FileNmae,"MarvellousLog%s.log"%(time.ctime()))
    f=open("log_path",'w')
    f.write(separator + "\n")
    f.write("sum of all files :" + time.ctime()+"\n")    
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AcessDenied, psutil.ZombieProcess):
            pass

        for element in listprocess:
            f.write("%s\n"% element)

    origin = 'log_path'
    target = FileNmae

    shutil.copy(origin, target)

    fromaddr = "katorepratik5756@gmail.com"
    toaddr = userID

    password = 'edfvfzlsggctwkoi'
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "process running"

    body = "Body_of_the_mail"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    filename = "log_path"
    attachment = open('log_path', "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % log_path)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()



def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " + argv[0])
    user_email = input("Enter your email address: ")


    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    Process(argv[1],argv[2])
    time.sleep(6)

if __name__ == "__main__":
    main()