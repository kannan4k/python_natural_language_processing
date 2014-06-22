import subprocess
import os
from sent import *
 
def divide(fileName):
	''' Seperate each and every articles in the pdf and calling the corresponding sentimental analysis function'''
	split_pages = 1
	print fileName
	fileList = []
	fileList.append(fileName) 
	hashDelimiter = "\n#################################################\n"  #Delimiter to find the new document
	fo = open(fileName.split('.')[0]+'.txt', 'wb') #Opening the txt file to push each articles with delimiters
	fo.close()
	for i in range(1,500):
		p = subprocess.Popen(['pdf2txt.py', '-p',str(i),fileName], stdout=subprocess.PIPE,stderr=subprocess.PIPE)  #Using PDFMiner we are reading the pdf page by page
		out, err = p.communicate()
	#	print out
		#This if condition pushes the each and every article with delimiters. 
		if out != '':
			if out.find('The New York Times Company. All Rights Reserved.') != -1:
				print 'Reading Page',i
				
				# Open a file
				with open(fileName.split('.')[0]+".txt", "a") as fo:
					fo.write(hashDelimiter)
					fo.write(out)
					split_pages = split_pages+1
					# Close opend file
					fo.close()
			else:
				print 'Reading Page',i
				split_pages =split_pages-1
				with open(fileName.split('.')[0]+'.txt', "a") as myfile:
					myfile.write(out)
	
	#Opening the csv file to write the results
	file_writer = open(fileName.split('.')[0]+'.csv', 'wb')
	file_writer.close()
	
	fileReader = open(fileName.split('.')[0]+'.txt')
	full_paper = fileReader.read() #Contains the whole pdf contains all the articles seperated by delimiter
	
	split_paper = full_paper.split('\n#################################################\n')
	for i in range(1,len(split_paper)):
		''' This For loop is used to read each and every article form the txt file.'''
		print 'Analyzing Article',i
		#print split_paper[i].split('The New York Times\n')[0].split('\n')[-5:-1]
		titCountList = getArticleCount(split_paper[i].split('The New York Times\n')[0].split('\n')[-5:-1][0]) #Getting Title Count
		artCountList = getArticleCount(split_paper[i].split('The New York Times Company. All Rights Reserved.')[1]) #Getting Article Count
		forWriteToFile = split_paper[i].split('The New York Times\n')[0].split('\n')[-5:-1] # Addlind additional parameters like word count, Date
		forWriteToFileList = [x.replace(',',' ') for x in forWriteToFile] #Removing comma in the title and Author
		with open(fileName.split('.')[0]+'.csv', 'a') as result_file:
			file_writer = csv.writer(result_file)
			#for i in range(item_length):
			mergedList = fileList+forWriteToFileList+titCountList+artCountList
			file_writer.writerow([x for x in mergedList]) #Writing the results to the csv file
	return 1




# Enter Your File names like the below format		
#divide('carlo.pdf')

divide('sample.pdf')



