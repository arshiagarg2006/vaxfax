import csv
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


state = "Columbia"




vaxfile = "static/vax.csv"
 
fields = []
rows = []
 
with open(vaxfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter="\t")
     
    fields = next(csvreader)
 
    for row in csvreader:
        rows.append(row)


for row in rows:
  if (state in row[3]) & ("2020" in row[4]) & ("13-17" in row[6]):
    if ((row[0] == "HPV") & ("Males and Females" in row[1])) or row[0] != "HPV":
      print(row[0] + " " + fields[1] + row[1] + " " + fields[7] + row[7])

vaccine = "Meningococcal"

reqfile = "static/req.csv"
 
fields1 = []
rows1 = []

def requirement(num, state): 
  for row in rows1:
    if state in row[0]:
      return row[num]

 
with open(reqfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
     
    fields1 = next(csvreader)
 
    for row in csvreader:
        rows1.append(row)

if vaccine == "Meningococcal":
  print(requirement(1, state))
elif vaccine == "TDAP":
  print(requirement(2, state))
elif vaccine == "Vericella":
  print(requirement(3, state))
elif vaccine == "HPV":
  print(requirement(4, state))
elif vaccine == "HepA":
  print(requirement(5, state))
elif vaccine == "MMR":
  print(requirement(6, state))
elif vaccine == "HepB":
  print(requirement(7, state))
if __name__ == '__main__':
	app.run()



