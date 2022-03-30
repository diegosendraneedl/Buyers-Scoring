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
                with open(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\buyers_scoring\\logs\\contactID-scoring-" + str(piScoringType) + ".dat", 'wt', newline='') as fileStreamLog:
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
            #with open(os.getenv('APPDATA') + "\\Diego Sendra\\code\\Python\\pierre_asseo\\buyers_scoring\\buyers_scoring\\logs\\contactID-scoringQuality-" + str(piScoringType) + ".dat", 'wt', newline='') as fileStreamLog:
            with open(pROOTDIR + "/BuyersScoringList/logs/contactID-scoringQuality-" + str(piScoringType) + ".dat", 'wt', newline='') as fileStreamLog:
                #contact ID                
                fileStreamLog.write(str(tcontactid))

        objADONet = None

        return (iret, pfabortScoring, ptcontactID, plstscoringResults)