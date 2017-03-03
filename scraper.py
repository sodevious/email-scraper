import csv, glob, time, datetime
from bs4 import BeautifulSoup

# Directory of html files
input_dir = "src/"
generated = time.strftime("%I:%M:%S, %d/%m/%Y")
timestamp = datetime.datetime.now()

# Create the CSV and header row
f = csv.writer(open("src/exported_emails_%s.csv" % timestamp, "w"))

# Clean slate
emailList= []
index = 0

# Write to CSV
for file_name in glob.glob(input_dir+ "*.html"):

    # Open the HTML files
    with open(file_name) as fp:
        record = BeautifulSoup(fp, "html.parser")

        mailtos = record.select('a[href^=mailto]')

        for i in mailtos:
            href=i['href']
            try:
                str1, str2 = href.split(':')
            except ValueError:
                break
            
            emailList.append(str2)
            
    # Write each email
    for email in emailList:
        index = index + 1

        f.writerow([index,email])