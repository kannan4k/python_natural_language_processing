#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sent import *


def split_ln(fname):
    print 'Processing\t',fname
    #Imort the two required modules
    import re
    import csv
    outname=fname.replace(fname.split('.')[-1],'txt1') #replace the extension with "csv"
    #setup the output file. Maybe give the option for seperate text files, if desired.
    
    file_writer = open(fname.split('.')[0]+'.csv', 'wb')
    file_writer.close()
    

    lnraw=open(fname).read() #read the file
    meta_tuple=('FILENAME','TITLE','BY','TITLE','EDITION')
       
    workfile=re.sub('.*Copyright .*?\\n','ENDOFILE',lnraw) #silly hack to find the end of the documents
    workfile=workfile.replace('\xef\xbb\xbf\n','') 
    workfile=workfile.split('ENDOFILE') #split the file into a list of documents.
    wrk = ' '.join(workfile)
    
    


    #Figure out what special meta data is being reported
    meta_list=list(set(re.findall('\\n([A-Z][A-Z-]*?):',lnraw))) #Find them all
    for item in meta_list:
        meta_tuple=meta_tuple+(item,)
    #writer.writerow(meta_tuple+('TEXT',))  
    temp=0
    for f in workfile:
        #print "Processing"
        print temp
        temp+=1
        byline=""
        date=""
        length=""
        title=""
        content=""
        match = re.search(r'.*BYLINE:(?P<byline>.*)', f)
        if match:
            #print "##################################################################################\n";
            #print "##################################################################################\n";
            byline = match.groupdict()['byline'].strip()
            #print byline

        match = re.search(r'.*LOAD-DATE:(?P<date>.*)', f)
        if match:
            date = match.groupdict()['date'].strip()
            #print date

        match = re.search(r'.*LENGTH:(?P<length>.*)', f)
        if match:
            length = match.groupdict()['length'].strip()
            #print length

        
        match = re.findall(r'(?P<title>.*)LENGTH:', f,re.DOTALL)
        if match:
            title= match[0].rstrip().lstrip().strip()
            #print title

        match = re.findall(r'LENGTH:(?P<content>.*)LOAD-DATE:', f,re.DOTALL)
        if match:
            content= match[0].rstrip().lstrip().strip()
            #print content



        titCountList=[]
        artCountList=[]
        forWriteToFile=[]
        forWriteToFileList=[]
        mergedList=[]
        
        titCountList = getArticleCount(title) #Getting Title Count
        artCountList = getArticleCount(content) #Getting Article Count
        forWriteToFile = [fname,  byline, length, date]
        forWriteToFileList = [x.replace(',',' ').strip() for x in forWriteToFile] #Removing comma in the title and Author
        with open(fname.split('.')[0]+'.csv', 'a') as result_file:
            file_writer = csv.writer(result_file)
            #for i in range(item_length):
            mergedList = forWriteToFileList+titCountList+artCountList
            file_writer.writerow([x for x in mergedList]) #Writing the results to the csv file

            
 
        
    #writer.writerow(workfile)        
    print 'Wrote\t\t',fname.split('.')[0]+'.csv'
    

if __name__ == "__main__":
    import sys
    try: 
        flist=sys.argv[1:]
    except:
        print 'Only one argument please. But you can use things like *.txt'
    else:
        for fname in flist:
            split_ln(fname)
        
    
