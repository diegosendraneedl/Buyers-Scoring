from logging import exception
import os
import sys
sys.path.append(os.path.dirname (os.path.dirname(os.path.realpath(__file__))) )
from BuyersScoringUpdate.Classes.ADONet.ADONet import ADONet

SVC_DIR = ""
ROOT_DIR = ""
conf_file_path = ""

def run(ptSQLUpdate, conf_file_path=False): #conf_file="conf.ini"
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #log folder - creation
    #log/  

    #ADO.Net - Environment Variables - Connection
    #dev
    ADONet.connectionEnvironmentVariables(os.path.dirname(ROOT_DIR) + '\\BuyersScoring.env')
    #ADONet.connectionEnvironmentVariables(os.path.dirname(ROOT_DIR) + '/BuyersScoring.env')

    fconnectionError = False

    #connection
    objADONet = ADONet()
    objADONet.connectionMySQL = objADONet.connectionOpen(objADONet.connectionMySQL, 1)   

    try:
        dstcontactUpdate = objADONet.connectionMySQL.cursor()    
        dstcontactUpdate.execute (ptSQLUpdate)
        dstcontactUpdate.close() 
      
    except Exception:
        fconnectionError = True
    
    try:
        #connection - close
        objADONet.connectionMySQL.close()

    except Exception:
        fconnectionError = True

    objADONet = None

    return(fconnectionError)

if (__name__ == "__main__"):
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #dev
    conf_file_path = os.path.dirname(os.path.abspath(__file__)) + '\\conf.ini'
    #conf_file_path = os.path.dirname(os.path.abspath(__file__)) + '/conf.ini'

    #log folder - creation
    #log/    

    fconnectionError=False

    #dev
    #sys.argv = ["main.py", "update contacts set contactqualityScore=0 where id='519498000067144592'"] 

    #command-line parameters - read
    if len(sys.argv)>1:        
        #SQL update
        sys.argv[1] = sys.argv[1].strip()

        #ADO.Net - Environment Variables - Connection
        #dev
        ADONet.connectionEnvironmentVariables(os.path.dirname(ROOT_DIR) + '\\BuyersScoring.env')
        #ADONet.connectionEnvironmentVariables(os.path.dirname(ROOT_DIR) + '/BuyersScoring.env')

        #main - run        
        fconnectionError = run (sys.argv[1])        