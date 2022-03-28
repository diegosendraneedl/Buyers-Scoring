import sys
import csv
import os
from datetime import date
import datetime
import configparser

sys.path.append(os.path.dirname (os.path.dirname(os.path.realpath(__file__))) )
from BuyersScoring.Classes.Methods.BuyersScoring import BuyersScoring
from BuyersScoring.Classes.ADONet.ADONet import ADONet

SVC_DIR = ""
ROOT_DIR = ""
conf_file_path = ""

def commandlineUsage():
    print ("Invalid command-line parameters. Usage: ")
    print ("command:")
    print ("--scoring, --scoringQuality\n")
    
    print ("scoringType:")
    print ("--0\t0=All\n") #--1 Importers
    
    print ("scoringType (Quality Scoring):")
    print ("--0, --1, --2\t0=Manufacturer, 1=Purchasing Group, 2=Other\n")
    
    print ("contactID")
    print ("--id:contactID\n")    

    #print ("Flagged")
    #print ("--flagged:yes\n")
    
    print ("Examples:")
    print ("main.py --scoring --0\t#performs buyers scoring")
    print ("main.py --scoringQuality --1\t#performs quality scoring on purchasing groups")
    print ("main.py --scoringQuality --2 --id:contactID\t#performs quality scoring on everything but manufacturers and purchasing groups, from contactID onwards")
    #print ("main.py --scoringQuality --0 --flagged:yes\t#performs quality scoring on manufacturers (Flagged contacts)")

def run(conf_file_path=False): 
    iret = 0
    objBuyersScoring = BuyersScoring()
    BuyersScoring.scoringType=int(BuyersScoring.scoringType)

    if (BuyersScoring.command ==  "scoringQuality"):           
        if BuyersScoring.scoringType==0:
            tscoringtypeDescription = "Manufacturer"    
        elif BuyersScoring.scoringType==1:            
            tscoringtypeDescription = "Purchasing Group"      
        elif BuyersScoring.scoringType==2:            
            tscoringtypeDescription = "Others"      

        iret, objBuyersScoring.fabortScoring, BuyersScoring.contactID, objBuyersScoring.lstscoringResults = objBuyersScoring.ContactsScoreQuality(
                objBuyersScoring.fabortScoring, BuyersScoring.contactID, BuyersScoring.scoringType, objBuyersScoring.lstscoringResults, BuyersScoring.command)

    elif (BuyersScoring.command ==  "scoring"):
        BuyersScoring.scoringType=int(BuyersScoring.scoringType)
        
        if BuyersScoring.scoringType==0:
            tscoringtypeDescription = "Importers"    
        elif BuyersScoring.scoringType==1:            
            tscoringtypeDescription = "n/a"
        elif BuyersScoring.scoringType==10:            
            tscoringtypeDescription = "All"

        iret, objBuyersScoring.fabortScoring, BuyersScoring.contactID, objBuyersScoring.lstscoringResults = objBuyersScoring.ContactsScore(
            objBuyersScoring.fabortScoring, BuyersScoring.contactID, BuyersScoring.scoringType, objBuyersScoring.lstscoringResults, BuyersScoring.command)
        
        #buyers scoring results - CSV - write
        #if len(objBuyersScoring.lstscoringResults)>0: #is not None
        #    objBuyersScoring.BuyersScoringResultsExportCSV (objBuyersScoring.lstscoringResults, BuyersScoring.scoringType, BuyersScoring.contactID)
    
    objBuyersScoring = None   

    if (iret == 0):
        #contacts scoring - success    
        print ("\nContacts " + BuyersScoring.command + " completed succesfully!")
    else:
        #contacts scoring - error    
        print ("\nContacts " + BuyersScoring.command + " returned an error. Check log in \logs subfolder.")

        #contacts scoring - error log - write  

        if (BuyersScoring.command ==  "scoringQuality"):            
            #dev
            with open(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\logs\\contacts-scoringQuality-" + tscoringtypeDescription.replace("/","-") + "-log.txt", 'a', newline='') as fileStreamLog:
            #with open(os.getcwd() + "\\buyers_scoring\\logs\\contacts-scoringQuality-log.txt", 'wt', newline='') as fileStream:
                #contacts scoring - error log - account ID - write 
                fileStreamLog.write (str(datetime.datetime.today()) + " - " + tscoringtypeDescription + " - Lost connection to MySQL server at 34.76.45.236:3306 at id: " + str(BuyersScoring.contactID) + ". Start the scoring script again to resume using this contactID, also found in contactID-" + str(BuyersScoring.scoringType) + ".dat.\r\n- i.e. main.py --scoringQuality --0 --id:contactID\r\nCurrent parameters: " + str(sys.argv) + "\r\n")

        elif (BuyersScoring.command ==  "scoring"):
            #dev
            with open(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\logs\\contacts-scoring-" + tscoringtypeDescription.replace("/","-") + "-log.txt", 'a', newline='') as fileStreamLog:
            #with open(os.getcwd() + "\\buyers_scoring\\logs\\contacts-scoring-log.txt", 'wt', newline='') as fileStream:
                #contacts scoring - error log - account ID - write 
                fileStreamLog.write (str(datetime.datetime.today()) + " - " + tscoringtypeDescription + " - Lost connection to MySQL server at 34.76.45.236:3306 at id: " + str(BuyersScoring.contactID) + ". Start the scoring script again to resume using this contactID, also found in contactID-" + str(BuyersScoring.scoringType) + ".dat.\r\n- i.e. main.py --scoring --0 --id:contactID\r\nCurrent parameters: " + str(sys.argv) + "\r\n")
    
if __name__ == "__main__":
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #dev
    conf_file_path = os.path.dirname(os.path.abspath(__file__)) + '\\conf.ini'
    #conf_file_path = os.path.dirname(os.path.abspath(__file__)) + '/conf.ini'

    #log folder - creation
    #log/

    #settings
    BuyersScoring.scoringType = 0
    BuyersScoring.command = "scoring"
    #BuyersScoring.processFlagged = False

    #command-line parameters - read
    fcommandlineError=False

    #dev
    #sys.argv = ["main.py", "--scoringQuality", "--1"] #"--id:519498000001298871"

    if len(sys.argv)>1:            
        if ((str(sys.argv[1]).lower().find ("scoringquality")>-1) or (str(sys.argv[1]).lower().find ("scoring")>-1)):
            #scoring / quality scoring   
            #command   
            BuyersScoring.command = sys.argv[1].replace("-","")

            #contactID (id:value)
            BuyersScoring.contactID = ""
            
            if ( len(sys.argv)>2 and ((str(sys.argv[2]).find ("0")>-1) or (str(sys.argv[2]).find ("1")>-1) or (str(sys.argv[2]).find ("2")>-1) or (str(sys.argv[2]).find ("3")>-1))
                ):
                #scoring type (--0 a --3)
                BuyersScoring.scoringType = int(sys.argv[2].replace("-","").strip())

                #Contact ID - log - read
                #dev
                if (os.path.exists(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\logs\\ContactID-scoringQuality-" + str(BuyersScoring.scoringType) + ".dat")):
                #if (os.path.exists(os.getcwd() + "\\buyers_scoring\\logs\\ContactID-scoringQuality-" + str(piscoringType) + ".dat")):
                    #dev
                    with open(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\logs\\ContactID-scoringQuality-" + str(BuyersScoring.scoringType) + ".dat", 'r', newline='') as fileStreamLog:
                    #with open(os.getcwd() + "\\buyers_scoring\\logs\\ContactID-scoringQuality-" + str(piscoringType) + ".dat", 'r', newline='') as fileStreamLog:
                        #Contact ID (id:value)
                        BuyersScoring.ContactID = fileStreamLog.readline()

                    #Contact ID - log - delete                
                    #dev
                    os.remove(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\logs\\ContactID-scoringQuality-" + str(BuyersScoring.scoringType) + ".dat")
                    #os.remove(os.getcwd() + "\\buyers_scoring\\logs\\ContactID-scoringQuality-" + str(BuyersScoring.scoringType) + ".dat")

                #contact ID (id:value)
                if len(sys.argv)>3:
                    if ((str(sys.argv[3]).lower().find ("id:")>-1)):
                        BuyersScoring.contactID = sys.argv[3].lower().replace("-","").replace("id:","").strip()
                    #elif ((str(sys.argv[3]).lower().find ("flagged:")>-1)):
                    #    if (sys.argv[3].lower().replace("-","").replace("flagged:","").strip()=="yes"):
                    #        BuyersScoring.processFlagged = True
                    else:
                        fcommandlineError=True
                        commandlineUsage()
                
                    #deprecated
                    """ #flagged
                    if len(sys.argv)>4:
                        if ((str(sys.argv[4]).lower().find ("flagged:")>-1)):
                            if (sys.argv[3].lower().replace("-","").replace("flagged:","").strip()=="yes"):
                                BuyersScoring.processFlagged = True
                        else:
                            fcommandlineError=True
                            commandlineUsage() """

            else:
                fcommandlineError=True
                commandlineUsage()
        else:
            fcommandlineError=True
            commandlineUsage()
    #end settings
                
        if not fcommandlineError:
            #ADO.Net - Environment Variables - Connection
            #dev
            ADONet.connectionEnvironmentVariables(os.path.dirname(ROOT_DIR) + '\\BuyersScoring.env')
            #ADONet.connectionEnvironmentVariables(os.path.dirname(ROOT_DIR) + '/BuyersScoring.env')

            #main - run
            run()

    else:    
        commandlineUsage()