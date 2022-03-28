#import mysql.connector
import pymysql
import sqlalchemy
from sqlalchemy.engine.url import make_url
import os
from dotenv import load_dotenv
from pathlib import Path

class ADONet:
    #  ADO.net 
    connectionTimeout = 480 

    # connection - MySQL 
    connectionMySQL = None  
    connectionMySQLDT = None    

    #connection - MySQL 
    #userMySQL = ""
    #passwordMySQL = ""
    #serverMySQL = ""
    #databaseMySQL = ""
    databaseMySQLZoho_CRMURL = ""
    
    #connection - MySQL 
    #databaseMySQLDT= ""
    databaseMySQLdata_teamURL = ""
    
    def __init__(self):  
       "ADONet"
    
    def connectionEnvironmentVariables(ppath):
        load_dotenv(dotenv_path=Path(ppath))
        
        #connection - MYSQL
        ADONet.databaseMySQLZoho_CRMURL = make_url(os.getenv('ZOHO_CRM_DBURL'))
        ADONet.databaseMySQLdata_teamURL = make_url(os.getenv('DATA_TEAM_DBURL'))

        """ ADONet.userMySQL = os.getenv('userMySQL')
        ADONet.passwordMySQL = os.getenv('passwordMySQL')
        ADONet.serverMySQL = os.getenv('serverMySQL')
        ADONet.databaseMySQL = os.getenv('databaseMySQL') """
        
    def connectionOpen(self, pconnection, piconnectionType):
        if piconnectionType==1:
            #connection - MySQL - zoho_crm
            #pconnection = mysql.connector.connect (user = ADONet.userMySQL, password = ADONet.passwordMySQL , database = ADONet.databaseMySQL, host = ADONet.serverMySQL, connection_timeout=ADONet.connectionTimeout, autocommit=True)
            pconnection = pymysql.connect(
                user=ADONet.databaseMySQLZoho_CRMURL.username,
                password=ADONet.databaseMySQLZoho_CRMURL.password,
                database=ADONet.databaseMySQLZoho_CRMURL.database,
                host=ADONet.databaseMySQLZoho_CRMURL.host,
                port=ADONet.databaseMySQLZoho_CRMURL.port)
        
        if piconnectionType==4:
            #connection - MySQL - data_team
            #pconnection = mysql.connector.connect (user = ADONet.userMySQL, password = ADONet.passwordMySQL , database = ADONet.databaseMySQLDT, host = ADONet.serverMySQL, connection_timeout=ADONet.connectionTimeout, autocommit=True)
            pconnection = pymysql.connect(
                user=ADONet.databaseMySQLdata_teamURL.username,
                password=ADONet.databaseMySQLdata_teamURL.password,
                database=ADONet.databaseMySQLdata_teamURL.database,
                host=ADONet.databaseMySQLdata_teamURL.host,
                port=ADONet.databaseMySQLdata_teamURL.port)

        return (pconnection)

    def connectionPing(self, pconnection, piconnectionType):        
        if piconnectionType==1 or piconnectionType==4:
            #connection - MySQL
            iret = pconnection.is_connected()
        #elif piconnectionType==2:        
            #connection - SQL Server
        #elif piconnectionType==3:
            #connection - Access 97/2000 - open */

        return (iret)