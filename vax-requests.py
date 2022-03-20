from flask import Flask, render_template, request
import random
import csv

app = Flask(  
	__name__,
	template_folder='templates',  
	static_folder='static'  
)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/getInfo', methods= ['GET', 'POST'])
def getInfo():
  info = ""
  state = request.form['select1']
  vaccine = request.form['select2']


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
        if (vaccine == "Meningococcal conjugate") & (row[0] == "Meningococcal Conjugate"):
          info = info + vaccine + " vacinations with a " + row[1] + " have a " + row[7] + "% coverage in your state."
        elif (vaccine == "Tdap") & (row[0] == "Tdap"):
          info = info + vaccine + " vacinations with a " + row[1] + " have a " + row[7] + "% coverage in your state."
        elif (vaccine == "Vericella") & (row[0] == "Vericella"):
          info = info + vaccine + " vacinations with a " + row[1] + " have a " + row[7] + "% coverage in your state."
        elif (vaccine == "HPV") & (row[0] == "HPV"):
          info = info + vaccine + " vacinations with a " + row[1] + " have a " + row[7] + "% coverage in your state."
        elif (vaccine == "Hepatitis A") & (row[0] == "Hep A"):
          info = info + vaccine + " vacinations with a " + row[1] + " have a " + row[7] + "% coverage in your state."
        elif (vaccine == "MMR") & (row[0] == "MMR"):
          info = info + vaccine + " vacinations with a " + row[1] + " have a " + row[7] + "% coverage in your state."
        elif (vaccine == "Hepatitis B") & (row[0] == "Hep B"):
          info = info + vaccine + " vacinations with a " + row[1] + " have a " + row[7] + "% coverage in your state."
        
  

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

  if vaccine == "Meningococcal conjugate":
    if (requirement(1, state) == "true"):
      info += " " + vaccine + " is mandated for students in this state."
    else:
      info += " " + vaccine + " is not mandated for students in this state."
  elif vaccine == "Tdap":
    if (requirement(2, state) == "true"):
      info += " " + vaccine + " is mandated for students in this state."
    else:
      info += " " + vaccine + " is not mandated for students in this state."
  elif vaccine == "Varicella":
    if (requirement(3, state) == "true"):
      info += " " + vaccine + " is mandated for students in this state."
    else:
      info += " " + vaccine + " is not mandated for students in this state."
  elif vaccine == "HPV":
    if (requirement(4, state) == "true"):
      info += " " + vaccine + " is mandated for students in this state."
    else:
      info += " " + vaccine + " is not mandated for students in this state."
  elif vaccine == "Hepatitis A":
    if (requirement(5, state) == "true"):
      info += " " + vaccine + " is mandated for students in this state."
    else:
      info += " " + vaccine + " is not mandated for students in this state."
  elif vaccine == "MMR":
    if (requirement(6, state) == "true"):
      info += " " + vaccine + " is mandated for students in this state."
    else:
      info += " " + vaccine + " is not mandated for students in this state."
  elif vaccine == "Hepatitis B":
    if (requirement(7, state) == "true"):
      info += " " + vaccine + " is mandated for students in this state."
    else:
      info += " " + vaccine + " is not mandated for students in this state."

  return render_template('index.html', info = info)
 

if __name__ == "__main__":  
	app.run( 
		host='0.0.0.0',  
		port=random.randint(2000, 9000),  
    debug = True
	)
