import sys
from datetime import date
import pandas as pd
import array as arr
import datetime
import os
import csv
#from Classes.ADONet.ADONet import ADONet
from BuyersScoringList.Classes.ADONet.ADONet import ADONet

#deprecated
#from Package.libname.BuyersScoringUpdate import main

sys.path.append(os.path.dirname (os.path.dirname(os.path.realpath(__file__))) )
from BuyersScoringUpdate import main

#temp
""" import numpy as np
import random as rd
import math
import mysql.connector as mysql

from urllib.parse import urlparse
import unidecode
import unicodedata """
#end temp

class BuyersScoring:        
    fabortScoring = False

    #SQL Updates
    lstSQLUpdates = []    
    
    #scoring - results
    lstscoringResults = []

    #command
    command = ""

    #filters
    scoringType = 0

    #settings    
    contactID = ""
    #processFlagged = False

    def __init__(self):  
        "Buyers Scoring"

    """ temp
        def BuyersScoringResultsExportCSV(self, plstscoringResults, piScoringType, ptcontactID):     
        if piScoringType==0:
            tscoringtypeDescription = "Brands"                
        elif piScoringType==1:
            tscoringtypeDescription = "n/a"      
        elif piScoringType==10:
            tscoringtypeDescription = "All"
            
        #dev
        with open(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\csv\\accounts scoring-" + tscoringtypeDescription + "-" + f"{datetime.datetime.now():%Y-%m-%d}" + ".csv", 'a', newline='') as fileStream:        
        #with open(pROOTDIR + "/BuyersScoringList/csv/accounts scoring-" + tscoringtypeDescription + "-" + f"{datetime.datetime.now():%Y-%m-%d}" + ".csv", 'a', newline='') as fileStream:        
            writer = csv.writer(fileStream, delimiter=",")

            #scoring results - header
            if (ptcontactID=="" or "".__eq__(ptcontactID)):
                if (piScoringType==1):
                    writer.writerow(["uid", "id", "scoring", "scoring PL", "scoring China", "scoring USA", "owner_OwnerName", "accountName", "bVDID", "bRCCode", "instagramURL", "billingCountry", "zohoCompanyType", "bVDSizeOfCompany", "goldencategory1", "goldencategory2", "productTrend", "bVDStatus", "continent", "pLOrBrands", "tradeshows", "tradeshowsValid", "iFSCode", "website", "Tradeshows n-3", "Tradeshows n-2", "Tradeshows n-1", "Tradeshows n", "No PL Tradeshows", "Instagram", "LinkedIN", "Potential", "BVD", "Geography", "Certifications", "Customer Name", "Scoring Parameter"])                        
                else:
                    writer.writerow(["uid", "id", "scoring", "scoring PL", "scoring China", "scoring USA", "owner_OwnerName", "accountName", "bVDID", "bRCCode", "instagramURL", "billingCountry", "zohoCompanyType", "bVDSizeOfCompany", "goldencategory1", "goldencategory2", "maincategory", "bVDStatus", "continent", "pLOrBrands", "tradeshows", "tradeshowsValid", "iFSCode", "website", "Tradeshows n-3", "Tradeshows n-2", "Tradeshows n-1", "Tradeshows n", "No PL Tradeshows", "Instagram", "LinkedIN", "Potential", "BVD", "Geography", "Certifications", "Customer Name", "Scoring Parameter"])

            #scoring results
            writer.writerows(plstscoringResults) 
        end temp """

    def contactfieldValues (self, pdstAccounts, pirow, piScoringType, ptCommand):   
        #contacts        
        tid = pdstAccounts.at[pdstAccounts.index[pirow], 'accountName_ID'] or ""         
        tcontactID = pdstAccounts.at[pdstAccounts.index[pirow], 'contactID'] or "" 
        temail = pdstAccounts.at[pdstAccounts.index[pirow], 'email'] or "" 
        temail2 = pdstAccounts.at[pdstAccounts.index[pirow], 'email2'] or "" 
        temail3 = pdstAccounts.at[pdstAccounts.index[pirow], 'email3'] or "" 
        tphone = pdstAccounts.at[pdstAccounts.index[pirow], 'phone'] or "" 
        tphone2 = pdstAccounts.at[pdstAccounts.index[pirow], 'phone2'] or "" 
        tfirstName = pdstAccounts.at[pdstAccounts.index[pirow], 'firstName'] or "" 
        tlastName = pdstAccounts.at[pdstAccounts.index[pirow], 'lastName'] or "" 
        twabelID = pdstAccounts.at[pdstAccounts.index[pirow], 'wabelID'] or "" 
        tlinkedinUpdate = pdstAccounts.at[pdstAccounts.index[pirow], 'linkedinUpdate'] or "" 
        tuRLLinkedinProfile = pdstAccounts.at[pdstAccounts.index[pirow], 'uRLLinkedinProfile'] or "" 
        tcontactPosition = pdstAccounts.at[pdstAccounts.index[pirow], 'contactPosition'] or "" 
        tcategory1 = pdstAccounts.at[pdstAccounts.index[pirow], 'category1'] or "" 
        tcategory2 = pdstAccounts.at[pdstAccounts.index[pirow], 'category2'] or ""         
        twabelCategory2 = pdstAccounts.at[pdstAccounts.index[pirow], 'wabelCategory2'] or "" 
        twabelCategory3 = pdstAccounts.at[pdstAccounts.index[pirow], 'wabelCategory3'] or "" 
        tgoldenCategory1 = pdstAccounts.at[pdstAccounts.index[pirow], 'goldenCategory1'] or "" 
        tgoldenCategory2 = pdstAccounts.at[pdstAccounts.index[pirow], 'goldenCategory2'] or "" 
        tgoldenCategory3 = pdstAccounts.at[pdstAccounts.index[pirow], 'goldenCategory3'] or "" 
        temailingstatus = pdstAccounts.at[pdstAccounts.index[pirow], 'emailingstatus'] or ""         

        #accounts
        tzohocompanytype = pdstAccounts.at[pdstAccounts.index[pirow], 'zohocompanytype'] or "" 
        taccountName = pdstAccounts.at[pdstAccounts.index[pirow], 'accountName'] or "" 
        
        #contacts
        if (ptCommand=="scoringQuality"):
            return (tid, tcontactID ,temail ,temail2 ,temail3 ,tphone ,tphone2 ,tfirstName ,tlastName ,twabelID , tlinkedinUpdate, tuRLLinkedinProfile ,tcontactPosition ,tcategory1 ,tcategory2 ,twabelCategory2 ,twabelCategory3 ,tgoldenCategory1 ,tgoldenCategory2 ,tgoldenCategory3 ,temailingstatus ,tzohocompanytype, taccountName)
        elif (ptCommand=="scoring"):
            return (tid, tcontactID ,temail ,temail2 ,temail3 ,tphone ,tphone2 ,tfirstName ,tlastName ,twabelID ,tlinkedinUpdate, tuRLLinkedinProfile ,tcontactPosition ,tcategory1 ,tcategory2 , twabelCategory2 ,twabelCategory3 ,tgoldenCategory1 ,tgoldenCategory2 ,tgoldenCategory3 ,temailingstatus ,tzohocompanytype, taccountName)

    #to be implemented
    """ def ContactsScore (self, pfabortScoring, ptcontactID, piScoringType, plstscoringResults, ptCommand, pROOTDIR):
            iret = 0
            pfabortScoring = False

            iScoring = 0
            iScoringTotal = 0
            iScoringTotalAccount = 0

            #contacts
            tid = ""        
            tcontactid = ""
            temail = ""
            temail2 = ""
            temail3 = ""
            tphone = ""
            tphone2 = ""
            tfirstName = ""
            tlastName = ""
            twabelID = ""
            tlinkedinUpdate = ""
            tuRLLinkedinProfile = ""
            tcontactPosition = ""
            tcategory1 = ""
            tcategory2 = ""            
            twabelCategory2 = ""
            twabelCategory3 = ""
            tgoldenCategory1 = ""
            tgoldenCategory2 = ""
            tgoldenCategory3 = ""
            temailingstatus = ""

            #accounts
            taccountName = ""
            tzohocompanytype = ""
            tidPrev = ""

            #scoring - results
            lstscoringResults = []

            #scoring - results total
            lscoringresultsTotal = 0

            #connection
            objADONet = ADONet()
            objADONet.connectionMySQL = objADONet.connectionOpen(objADONet.connectionMySQL, 1)   

            fcontactIdFound = False
            fconnectionError = False

            try:        
                objADONet.connectionMySQL.close()            
            except Exception:
                fconnectionError = True

            if (fconnectionError):
                ptcontactID = tcontactid    

                iret = 1
                #contact ID - error log - write
                #dev
                with open(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\buyers_scoring\\Package\\BuyersScoringList\\logs\\contactID-scoring-" + str(piScoringType) + ".dat", 'wt', newline='') as fileStreamLog:
                #with open(pROOTDIR + "/BuyersScoringList/logs/contactID-scoring-" + str(piScoringType) + ".dat", 'wt', newline='') as fileStreamLog:
                    #writer = csv.writer(fileStream, delimiter=",")                    
                    #contact ID
                    fileStreamLog.write(str(tcontactid))

            objADONet = None

            return (iret, pfabortScoring, ptcontactID, plstscoringResults) """
    #end to be implemented
    #     
    def ContactsScoreQuality (self, pfabortScoring, ptcontactID, piScoringType, plstscoringResults, ptCommand, pROOTDIR):
        iret = 0
        pfabortScoring = False

        iScoring = 0
        iScoringTotal = 0
        iScoringTotalAccount = 0

        #contacts
        tid = ""        
        tcontactid = ""
        temail = ""
        temail2 = ""
        temail3 = ""
        tphone = ""
        tphone2 = ""
        tfirstName = ""
        tlastName = ""
        twabelID = ""
        tlinkedinUpdate = ""
        tuRLLinkedinProfile = ""
        tcontactPosition = ""
        tcategory1 = ""
        tcategory2 = ""        
        twabelCategory2 = ""
        twabelCategory3 = ""
        tgoldenCategory1 = ""
        tgoldenCategory2 = ""
        tgoldenCategory3 = ""
        temailingstatus = ""

        #accounts
        taccountName = ""
        tzohocompanytype = ""
        tidPrev = ""

        #scoring - results
        lstscoringResults = []

        #scoring - results total
        lscoringresultsTotal = 0   

        #connection
        objADONet = ADONet()
        objADONet.connectionMySQL = objADONet.connectionOpen(objADONet.connectionMySQL, 1)   

        print ("Fetching contacts ...")

        if (not ptcontactID == ""):            
            print ("Resuming from contactID: " + str(ptcontactID))   

        #deprecated
        """ tprocessFlaggedStr=""
        if (ptprocessFlagged):
            tprocessFlaggedStr = " AND (C.accountName_ID = '519498000305745001' OR  C.accountName_ID = '519498000315834635')"
        else:
            tprocessFlaggedStr = " AND NOT C.accountName_ID = '519498000305745001' AND NOT C.accountName_ID = '519498000315834635'"
 """
        if (int(piScoringType) == 0):
            tzohocompanytypeStr =" A.zohoCompanyType = 'Manufacturer' "
        elif (int(piScoringType) == 1):
            tzohocompanytypeStr =" A.zohoCompanyType = 'Purchasing Group' "
        elif (int(piScoringType) == 2):
            tzohocompanytypeStr =" NOT A.zohoCompanyType = 'Manufacturer' AND NOT A.zohoCompanyType = 'Purchasing Group' "
        elif (int(piScoringType) == 10):
            tzohocompanytypeStr =" A.zohoCompanyType LIKE '%%' "
        
        dstContacts = pd.read_sql_query ("SELECT A.zohocompanytype, A.accountName, C.accountName_ID, C.id AS contactID, " +
            " C.email, C.email2, C.email3, C.phone,C.phone2, C.firstName, " +
            " C.lastName, C.wabelID, C.linkedinUpdate, C.uRLLinkedinProfile, C.contactPosition," +
            " CC.category1, CC.category2, CC.wabelCategory2, " +
            " CC.wabelCategory3,C.goldenCategory1, C.goldenCategory2, C.goldenCategory3, " +
            " C.emailingstatus " +
            " FROM zoho_crm.contacts C" +
            " JOIN accounts A ON A.id = C.accountName_ID" +
            " LEFT JOIN data_team.zoho_crm_contacts_catagories CC ON CC.id = C.id " +
            " WHERE (" + tzohocompanytypeStr + " " #+ tprocessFlaggedStr +
            ") GROUP BY C.accountName_ID, C.id" +
            " ORDER BY C.accountName_ID, C.id limit 100", objADONet.connectionMySQL) 
 
        fcontactIdFound = False
        fconnectionError = False

        try:        
            objADONet.connectionMySQL.close()            
        except Exception:
            fconnectionError = True
            
        irow=0        
        while not (dstContacts.empty) and irow<len(dstContacts) and not pfabortScoring and not fconnectionError:            
            #contacts - field values
            objContactsScoring = BuyersScoring()            
            tid, tcontactid ,temail ,temail2 ,temail3 ,tphone ,tphone2 ,tfirstName,tlastName ,twabelID ,tlinkedinUpdate, tuRLLinkedinProfile ,tcontactPosition ,tcategory1 ,tcategory2 ,twabelCategory2 ,twabelCategory3 ,tgoldenCategory1 ,tgoldenCategory2 ,tgoldenCategory3 ,temailingstatus,tzohocompanytype, taccountName = objContactsScoring.contactfieldValues (dstContacts, irow, piScoringType, ptCommand)
        
            iScoring = 0
            iScoringTotal = 0            

            if (not tid == tidPrev):
                #account - contact quality score
                if (not tidPrev == ""):
                    try:
                        #deprecated
                        #dstcontactUpdate = objADONet.connectionMySQL.cursor()
                        #dstcontactUpdate.execute ("update accounts set contactqualityScore=" + str(iScoringTotalAccount) + " where id='" + tidPrev + "'")
                        #dstcontactUpdate.close()

                        lstSQLUpdatesItem = ["update accounts set contactqualityScore=" + str(iScoringTotalAccount) + " where id='" + tidPrev + "'"]
                        BuyersScoring.lstSQLUpdates.append (lstSQLUpdatesItem)
                        print ("\t" + tidPrev + "\t" + "Contact Quality Score (Account): " + str(iScoringTotalAccount))
                    except Exception:
                        tid = tid
                        #fconnectionError = True

                iScoringTotalAccount = 0                
            
            #ptcontactID= "519498000001298861"
            if (not fcontactIdFound and not ptcontactID == ""):
                icount = 0                
                while (icount<len(dstContacts) and not dstContacts.at[dstContacts.index[icount],'contactID']  == ptcontactID and not fcontactIdFound):
                    icount+=1

                if icount<len(dstContacts):
                    if (dstContacts.at[dstContacts.index[icount],'contactID']  == ptcontactID):
                        fcontactIdFound = True
                        irow = icount
                        
                        #contacts
                        objContactsScoring = BuyersScoring()            
                        tid, tcontactid ,temail ,temail2 ,temail3 ,tphone ,tphone2 ,tfirstName,tlastName ,twabelID ,tlinkedinUpdate, tuRLLinkedinProfile ,tcontactPosition ,tcategory1 ,tcategory2 ,twabelCategory2 ,twabelCategory3 ,tgoldenCategory1 ,tgoldenCategory2 ,tgoldenCategory3 ,temailingstatus,tzohocompanytype, taccountName = objContactsScoring.contactfieldValues (dstContacts, irow, piScoringType, ptCommand)
                else:
                    pfabortScoring=True

            objContactsScoring = None

            #contact - e-mail            
            iScoring = 0
            if (temailingstatus.lower().find("permanent")>-1):
                #bounce
                iScoring = -2
            else:
                if (temail=="" and temail2=="" and temail3==""):
                    #empty
                    iScoring = -1

                elif ((temail.lower().find("gmail")>-1 and temail.lower().find("yahoo")>-1 and                
                    temail.lower().find("outloook")>-1 and temail.lower().find("hotmail")>-1) and 
                    (temail2.lower().find("gmail")>-1 and temail2.lower().find("yahoo")>-1 and                
                    temail2.lower().find("outloook")>-1 and temail2.lower().find("hotmail")>-1) and
                    (temail3.lower().find("gmail")>-1 and temail3.lower().find("yahoo")>-1 and                
                    temail3.lower().find("outloook")>-1 and temail3.lower().find("hotmail")>-1)):
                    #generic
                    iScoring = 1                    
                else:
                    #non-generic
                    iScoring = 2

            iScoringTotal+= iScoring

            #contact - first name / last name
            iScoring = 0
            if (tlastName.lower().find("no name")<0):
                iScoring=1
            elif (tuRLLinkedinProfile!="" and tlastName!="" and tuRLLinkedinProfile.lower().find(tlastName.lower())>-1):
                iScoring=2
            if (tlastName.lower().find("no name")>-1 or tlastName == ""):
                iScoring=0

            iScoringTotal+= iScoring

            #contact - phone, phone2
            iScoring=0
            if (tphone == "" and tphone2 == ""):
                iScoring=0
            else:
                iScoring=1
            
            iScoringTotal+= iScoring

            #contact - linkedin URL + linkedin Update
            iScoring=0
            if (tuRLLinkedinProfile == "" and tlinkedinUpdate == ""):
                iScoring = -2
            elif (tuRLLinkedinProfile == "" and tlinkedinUpdate != ""):
                iScoring = -1
            elif (tuRLLinkedinProfile != "" and ( str(tlinkedinUpdate[:4]).isnumeric() 
            and (abs(int(str(tlinkedinUpdate[:4]).strip()) - int(str(datetime.datetime.today().year))) <=1 )
                )):
                iScoring = 2
            elif (tuRLLinkedinProfile != "" and ( str(tlinkedinUpdate[:4]).isnumeric() and 
                (abs(int(str(tlinkedinUpdate[:4]).strip()) - int(str(datetime.datetime.today().year))) >1 )
                )):
                iScoring = 1
            iScoringTotal+= iScoring

            #contact - categories
            iScoring=0
            if (not tcategory1=="" or not tcategory2==""):
                iScoring = 1                   
            if (not twabelCategory2=="" or not twabelCategory3==""):
                iScoring+= 1                   
            if (not tgoldenCategory1 =="" or not tgoldenCategory2=="" or not tgoldenCategory3==""):
                iScoring+= 1    

            iScoringTotal+= iScoring               
            
            #contact - position
            if (tcontactPosition != ""):
                iScoring=1

            iScoringTotal+= iScoring

            #account - scoring total
            iScoringTotalAccount+=iScoringTotal

            fconnectionError = False
            #objADONet.connectionMySQL.close()

            #if objADONet.connectionPing (objADONet.connectionMySQL, 1):
            #accounts - console/output            
            if (piScoringType==0):
                tscoringtypeDescription = "Manufacturer"
            if (piScoringType==1):
                tscoringtypeDescription = "Purchasing Group"   
            if (piScoringType==2):
                tscoringtypeDescription = "Other"
            if (piScoringType==10):
                tscoringtypeDescription = "All"
                
            print (str(lscoringresultsTotal+1) + "\t" + str(tcontactid) + "\t" + str(tfirstName + " " + tlastName) + "\t" + str(taccountName) + "\t" + str(iScoringTotal) + "\t" + tscoringtypeDescription)

            try:                
                #dstcontactUpdate = objADONet.connectionMySQL.cursor()
                #dstcontactUpdate.execute ("update contacts set contactqualityScore=" + str(iScoringTotal) + " where id='" + tcontactid + "'")
                #dstcontactUpdate.close()

                lstSQLUpdatesItem = ["update contacts set contactqualityScore=" + str(iScoringTotal) + " where id='" + tcontactid + "'"]
                BuyersScoring.lstSQLUpdates.append (lstSQLUpdatesItem)                        
            except Exception:
                lscoringresultsTotal = lscoringresultsTotal
                #fconnectionError = True
            
            #account ID - saves
            if irow<len(dstContacts):
                tidPrev = dstContacts.at[dstContacts.index[irow],'accountName_ID']

            #contacts - next
            irow+=1

            #scoring results - total
            lscoringresultsTotal+=1 
            #else:
            #fconnectionError = True                
        
        dstContacts = None
        
        #if (not fconnectionError):
        try:
            objADONet = ADONet()
            objADONet.connectionMySQL = objADONet.connectionOpen(objADONet.connectionMySQL, 1)
        except Exception:
            tcontactid = ptcontactID
            fconnectionError = True

        #accounts/contacts - contact quality score - updates
        irowSQLUpdates = 0
        print ("\n")

        while (irowSQLUpdates<len(BuyersScoring.lstSQLUpdates)) and not fconnectionError: 
            #try:                
            tcontactid = str(BuyersScoring.lstSQLUpdates[irowSQLUpdates]).lstrip('"[').rstrip(']"').replace("'","")[-18:]
            print (str(BuyersScoring.lstSQLUpdates[irowSQLUpdates]).lstrip('"[').rstrip(']"'))            
            
            #accounts/contacts - contact quality score - update
            fconnectionError = main.run (str(BuyersScoring.lstSQLUpdates[irowSQLUpdates]).lstrip('"[').rstrip(']"'))

            #next row
            irowSQLUpdates=irowSQLUpdates+1

        try:        
            objADONet.connectionMySQL.close()            
        except Exception:
            fconnectionError = True

        if (fconnectionError):
            ptcontactID = tcontactid    
            
            print ("contactID-scoringQuality-" + str(piScoringType) + ".dat")
            print (str(tcontactid))

            iret = 1
            #contact ID - error log - write
            #dev
            with open(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\buyers_scoring\\Package\\BuyersScoringList\\logs\\contactID-scoringQuality-" + str(piScoringType) + ".dat", 'wt', newline='') as fileStreamLog:
            #with open(pROOTDIR + "/BuyersScoringList/logs/contactID-scoringQuality-" + str(piScoringType) + ".dat", 'wt', newline='') as fileStreamLog:
                #contact ID                
                fileStreamLog.write(str(tcontactid))

        objADONet = None

        return (iret, pfabortScoring, ptcontactID, plstscoringResults)

    def query_contactsBuyersImporters(self, pfStageCOnly, pfbycontactPosition, pfadditionalFields):
        #connection
        objADONet = ADONet()
        objADONet.connectionMySQL = objADONet.connectionOpen(objADONet.connectionMySQL, 1)   

        Buyers = pd.read_sql_query("SELECT \
        a.accountName, \
        a.id as accountID, \
        c.accountName_Name, \
        c.linkedinCompany, \
        a.aliases, \
        a.zohoCompanyType, \
        a.specialization1, \
        a.specialization2, \
        a.billingCountry, \
        a.Continent, \
        a.bVDSizeOfCompany, \
        a.goldenRevenue, \
        a.partnershipStatus, \
        a.emailLogic, \
        a.priority, \
        a.companyWabelStatus, \
        a.brandsDistributed, \
        a.website , \
        a.importerCategory, \
        a.countryOfSales, \
        a.importerSize, \
        a.countryOfOriginOfProductsSold, \
        a.importerProductsSold, \
        a.pointsOfSalesCovered, \
        a.importerNameOfDistributionChannel, \
        c.source, \
        c.id, \
        c.createdTime, \
        c.linkedinName, \
        c.goldenPosition, \
        c.contactPosition, \
        c.goldenCategory1, \
        c.goldenCategory2, \
        c.goldenCategory3, \
        c.buyingScope, \
        c.descriptionOfCurrentJob, \
        c.profileSummary, \
        c.linkedinUpdate, \
        c.firstName, \
        c.lastName, \
        c.email, \
        c.email2, \
        c.phone, \
        c.wabelID, \
        c.goldenPhone	, \
        c.appearsOnWabel	, \
        c.visitorScore	, \
        c.lastActivityTime, \
        c.lastVisitedTime, \
        c.sourceDate, c.leadSourceAdditionalInfo AS `source Data`, \
        c.contactLatestDateOfConnectionOnWabel, \
        c.wabelNumberOfMessagesSent, \
        c.averageTimeSpentMinutes	, \
        c.uRLLinkedinProfile, \
        c.emailingStatus	, \
        c.contactWabelStatus	, \
        c.emailOptOut	, \
        c.doNotContactReason, \
        c.campaignScore	, \
        c.scoring, \
        c.contactqualityScore, \
        D.id as idDeal, \
        D.stage, \
        D.dealName, \
        D.stage AS `Max stage`, \
        D.owner_OwnerID	, \
        D.owner_OwnerName	, \
        D.accountScore1, \
        D.buyerScoring, \
        D.importerScore, \
        D.createdTime, \
        D.category2, \
        D.category3 , \
        a.pL, \
        a.brands, \
        c.plOrNb, \
        D.pLOrBrands, \
        D.potentialType, D.potentialCategory \
        /* B.`Bounce reason`*/ \
            from zoho_crm.accounts a \
            inner JOIN contacts c ON c.accountName_ID=a.id \
            LEFT JOIN deals D on D.accountName_ID=a.id \
            /* LEFT JOIN data_team.`zoho-campaigns-contacts-bounced` B ON (B.`Contact Email`=c.email)*/ \
            WHERE (a.zohoCompanyType LIKE '%purchasing group%' or a.zohoCompanyType LIKE '%importer%') \
            /*AND (a.specialization1 LIKE '%importer%' OR a.specialization2 LIKE '%importer%' OR \
            a.specialization2 LIKE '%packer%')*/ \
            AND (LEFT(UCASE(D.stage),1)='C') \
            AND D.potentialTarget like '%buyer%' AND right(D.dealName,4)>=2000 \
            AND (c.contactPosition LIKE '%purchasing%' OR \
        c.contactPosition LIKE '%purchase%' OR \
        c.contactPosition LIKE '%compra%' OR \
        c.contactPosition LIKE '%comprador%' OR \
        c.contactPosition LIKE '%buyer%' OR \
        c.contactPosition LIKE '%buying%' OR \
        c.contactPosition LIKE '%category%' OR \
        c.contactPosition LIKE '%cat.%' OR \
        c.contactPosition LIKE '%categoria%' OR \
        c.contactPosition LIKE '%des achats%' OR \
        c.contactPosition LIKE '%de achats%' OR \
        c.contactPosition LIKE '%categorie%' OR \
        c.contactPosition LIKE '%acheteu%') \
        GROUP BY (c.id) \
        order by a.id, c.id, left(D.stage, 2) DESC;",objADONet.connectionMySQL)

        # Buyers = pd.read_sql_query("SELECT c.id, \
        #     c.wabelID, \
        #     c.source, \
        #     c.contactWabelStatus, \
        #     c.emailingStatus, \
        #     c.fullName,\
        #     c.goldenPhone,\
        #     c.email,\
        #     c.goldenPosition,\
        #     c.linkedinCategory, \
        #     c.linkedinPosition, \
        #     c.linkedinUpdate, \
        #     c.goldencategory1,\
        #     c.goldencategory2,\
        #     c.buyingScope,\
        #     a.accountName,\
        #     a.zohoCompanyType,\
        #     a.specialization1,\
        #     a.specialization2 \
        # FROM \
        #     zoho_crm.contacts c \
        #         LEFT JOIN zoho_crm.accounts a ON c.accountName_ID = a.id \
        # WHERE a.id= '519498000001318019' AND \
        #     (a.zohoCompanyType LIKE '%Purchasing%' \
        #         OR a.zohoCompanyType LIKE '%importer%');",objADONet.connectionMySQL)
         
        Buyers.loc[Buyers['wabelID'].notnull(),'wabelID']=Buyers.loc[Buyers['wabelID'].notnull(),'wabelID'].astype(int)
        Buyers.loc[Buyers['wabelID'].notnull(),'wabelID']=Buyers.loc[Buyers['wabelID'].notnull(),'wabelID'].astype(str)
        
        try:        
            objADONet.connectionMySQL.close()                    
        except Exception:
            Buyers = Buyers

        objADONet = ADONet()
        objADONet.connectionMySQL = objADONet.connectionOpen(objADONet.connectionMySQL, 1)   

        Buyers_Deals = pd.read_sql_query("SELECT \
            d.contactName_ID , \
            d.accountName_ID, \
            d.dealName as 'Potential Name', \
            d.potentialCategory, \
            d.potentialType, \
            right(d.dealName,4) as 'Year', \
            d.stage as 'Potential Stage', \
            left(d.stage,2) as 'Stage simplified' , \
            d.owner_OwnerName as 'Potential Owner', \
            d.owner_OwnerID as 'Potential Owner ID' \
        FROM \
            zoho_crm.deals d \
            where d.potentialTarget like '%buyer%' AND (LEFT(UCASE(d.stage),1)='C') and right(d.dealName,4)>=2000;", objADONet.connectionMySQL) #and right(left(d.stage,2),1) > 3

        Buyers_Deals.loc[Buyers_Deals['Year'].isin([ 'pany', 'null', ' Box', 'uyer','OUR-','S', 'tial', 's']),'Year']=0
        Buyers_Deals['Year'] = Buyers_Deals['Year'].astype(int)
        idx = Buyers_Deals.groupby(['contactName_ID'])['Stage simplified'].transform(max) == Buyers_Deals['Stage simplified']
        Max_stage = Buyers_Deals[idx].sort_values(by='contactName_ID')
        Max_stage['Max deals infos'] = Max_stage['Potential Name'] +' - '+ Max_stage['potentialCategory'] +' - '+ Max_stage['Year'].astype(str) +' - '+ Max_stage['Potential Stage'] + ' - '+Max_stage['Potential Owner']
        Max_stage['Max deals infos'] = Max_stage['Max deals infos'].astype(str)
        Max_stage_test = Max_stage.reset_index(drop=True).groupby('contactName_ID')['Max deals infos'].apply(lambda Maxdeals: '; '.join(Maxdeals) )
        Max_stage_test=pd.DataFrame(Max_stage_test)

        Max_stage['Year'] = Max_stage['Year'].astype(str)
        Maxstage_year = Max_stage.sort_values(by='Year').groupby('contactName_ID')['Year'].apply(lambda Maxyear: '; '.join(Maxyear) )
        Maxstage_year =pd.DataFrame(Maxstage_year)

        Max_stage['potentialCategory'] = Max_stage['potentialCategory'].astype(str)
        Maxstage_Cat = Max_stage.sort_values(by='potentialCategory').groupby('contactName_ID')['potentialCategory'].apply(lambda Maxyear: '; '.join(Maxyear) )
        Maxstage_Cat =pd.DataFrame(Maxstage_Cat)

        MaXStageAllTime = Max_stage_test.merge(Max_stage[['contactName_ID','Stage simplified']].drop_duplicates(subset = ['contactName_ID']), on='contactName_ID', how = 'left').merge(Maxstage_year,on='contactName_ID', how = 'left').merge(Maxstage_Cat,on='contactName_ID', how = 'left')

        MaXStageAllTime = MaXStageAllTime.set_index('contactName_ID').rename(columns={"Max deals infos": "Maxdeals All Time", "Stage simplified": "MaxStage All Time","Year" : "Max Stage Year AllTime"})

        Buyers = Buyers.merge(MaXStageAllTime, left_on='id', right_on='contactName_ID', how='left')

        Buyers[Buyers['Max Stage Year AllTime'].notnull()]

        try:        
            objADONet.connectionMySQL.close()                    
        except Exception:
            Buyers = Buyers

        objADONet = ADONet()
        objADONet.connectionMySQL = objADONet.connectionOpen(objADONet.connectionMySQL, 1)   

        Member_participation = pd.read_sql_query("select idmember,group_concat(event_code) as 'EventParticipation'  from wabel.certain_event_registrations group by idmember;",objADONet.connectionMySQL)

        # Member_participation
        Member_participation['idmember']=Member_participation['idmember'].astype(str)
        
        Buyers = Buyers.merge(Member_participation, left_on='wabelID', right_on='idmember', how='left')

        Member_Meetings = pd.read_sql_query("SELECT \
            event_code, \
            idcompany_buyer, \
            cb.name as 'BuyerCompanyName', \
            idmember_buyer, \
            idcompany_supplier, \
            cs.name as 'SupplierCompanyName', \
            idmember_supplier \
        FROM \
            wabel.meetings \
                LEFT JOIN \
            wabel.companies cb ON cb.idcompany = meetings.idcompany_buyer \
            left join wabel.companies cs on cs.idcompany = wabel.meetings.idcompany_supplier \
            ", objADONet.connectionMySQL)

        Member_Meetings= Member_Meetings[Member_Meetings['idmember_buyer'].notnull()]
        Member_Meetings['idmember_buyer']=Member_Meetings['idmember_buyer'].astype(str)
        Member_Meetings['Infos']=  Member_Meetings['event_code']  + ' - '+ Member_Meetings['SupplierCompanyName'].astype(str)
        Member_Meetings

        Concat_Meetings = pd.DataFrame(data=Member_Meetings.groupby('idmember_buyer').apply(lambda x: '; '.join(str(x.Infos))),index=None, columns=['Meetings Infos'])
        Concat_Events = pd.DataFrame(data=Member_Meetings.drop_duplicates(subset=['idmember_buyer','event_code']).groupby('idmember_buyer').apply(lambda x: '; '.join(x.event_code)),index=None, columns=['EventParticipation'])
        Concat_companies_met = pd.DataFrame(data=Member_Meetings.drop_duplicates(subset=['idmember_buyer','SupplierCompanyName']).groupby('idmember_buyer').apply(lambda x: '; '.join(str(x.SupplierCompanyName))),index=None, columns=['SupplierCompanyMet'])
        Meetings_Recap = Concat_Meetings.merge(Concat_Events, on ='idmember_buyer').merge(Concat_companies_met,on ='idmember_buyer')
        Meetings_Recap

        Buyers = Buyers.merge(Meetings_Recap, left_on='wabelID', right_on='idmember_buyer', how='left')

        Members_on_needl = pd.read_sql_query("select m.idmember, m.zoho_id \
        from wabel.members m \
        left join wabel.companies com on com.idcompany = m.idcompany \
        where (m.status LIKE 'accepted'  OR m.status LIKE 'auto-accepted') \
                AND m.date_last_activity IS NOT NULL \
                AND com.status LIKE 'ON' ;",objADONet.connectionMySQL)
        
        Buyers.loc[Buyers['id'].isin(Members_on_needl['zoho_id']),'MemberOnNeedl']='Yes'
        Buyers[Buyers['MemberOnNeedl'].notnull()]

        #dev
        Buyers.to_csv(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\Buyers Lists recap rev1-by contact position.csv", header=True, index=False, sep='\t')
        #Buyers.to_excel(os.getcwd() + "\\buyers_scoring\\Buyers Lists recap rev1.xlsx", index=False)

        objADONet.connectionMySQL.close()
        objADONet = None
        
