import eel
from time import sleep
import csv
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime
import wiringpi as pi
import time
import mcp_adc

def main():
    # load web file
    eel.init("web")
    eel.start("main.html")


@eel.expose
def js_func(a):
    print("measure.py")
    
    sleep(5)

    print("measurement start!!")

    SPI_CE = 0
    SPI_SPEED = 1000000
    READ_CH = 0
    VREF = 3.3
     
    # Storage parameters above to "adc" 
    adc = mcp_adc.mcp3208( SPI_CE, SPI_SPEED, VREF )

    # Get time and date and storage it to "now"
    today = datetime.date.today()
    now = datetime.datetime.now()
    
    # insert citycity to City for the test
    City = 'mari'

    if not os.path.exists('python-data/%s' % today):
            print('This is the first experiment today. New repository coreated %s' % today)
            os.mkdir('python-data/%s'% today)
   

    # make file whose file name is 
    fmt_name = "python-data/{0}/test_{1:%Y%m%d-%H%M%S}.csv".format(today,now)

    print('start collecting data...')

    # edit text with open-method
    # open(file location,mode).
    # shorten open-method as "f" 

    with open(fmt_name,'w') as f:
        # edit the file in range of 0 to 50 of i.
        for i in range(0,50):
            now = datetime.datetime.now()
            value = adc.get_value( READ_CH )

            # lineteriminator will be set at the end of each row.
            writer = csv.writer(f, lineterminator='\n')

            # write each row with this command
            writer.writerow([now,value,City])

            # sumpling frequency. set the number in parenthesis here
            time.sleep( 0.1 )
    
    f.close()

    print( 'New file has created. Its name is ')
    print(fmt_name)
    print('    ')

    # commands necessary for Google Drive
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)


    f = drive.CreateFile({'title': "/{0:%Y%m%d-%H%M%S}.csv".format(now), 'mimeType': 'text/comma-separated-values'})
    f.SetContentFile('%s' % fmt_name)
    print('uploading files to Google Drive... ...')
    f.Upload()

    print('Completed uploading files')
  

    sleep(1)
    # expose and fire js function with argument "maririnrin"
    eel.my_javascript_function('%s' % fmt_name)
    
