from flask import Flask, request, redirect, url_for, render_template
from models import db, get_table1_and_fields, get_table2_and_fields, get_table3_and_fields, get_table4_and_fields, initialize_database





app = Flask(__name__)




# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solarCalc021.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create the table in the database
initialize_database(app)

'''
it does not accept in the listLoads
#calculate the total power
subTotalPower = 0
totalPower = 0
totalEnergyDay = 0 
totalEnergyNight = 0

'''
# instead global variable better use function
'''
totalPower1 = 0


def totalPowerCalc(subTotal):
    global totalPower1
    totalPower1 = totalPower1 + subTotal
    return totalPower1


'''

totalEnergyNight = 0

def totalEnergyNightCalc(eNight):
    global totalEnergyNight
    totalEnergyNight = totalEnergyNight + eNight
    print ('totalEnergyNight in def calc')
    print (totalEnergyNight)
    return totalEnergyNight 




totalEnergyDay = 0

def totalEnergyDayCalc(eDay):
    global totalEnergyDay
    totalEnergyDay = totalEnergyDay + eDay
    print ('totalEnergyDay in def calc')
    print (totalEnergyDay)
    return totalEnergyDay 


    

subTotalEnergyDay = 0
subTotalEnergyNight = 0

totalPower1 = 0

totalCalc1 = 0

def totalCalc(subTotal):
    global totalCalc1
    totalCalc1 = totalCalc1 + subTotal
    return totalCalc1

'''
index_add_counter = 0
def test():
    #global index_add_counter # means: in this scope, use the global name
    global totalPower11 # means: in this scope, use the global name
    #print(index_add_counter)
    print('totalPower11')
    print(totalPower11)
    return totalPower11
'''



# Home page - List all students
@app.route('/')
def index():
    #table, fields = get_table_and_fields()
    #students = db.session.query(table).all()
    return render_template('index.html')


## load

@app.route('/load')
def listLoads():
    table1, fields = get_table1_and_fields()
    loads = db.session.query(table1).all()

    
    #calculate the total power
    subTotalPower = 0
    totalPower = 0
    totalEnergyDay = 0
    totalEnergyNight = 0
  
    #global totalPower1 
    global totalCalc1 
    #totalPower1 = 0
    totalCalc1 = 0


    
    #print ('globTotalPower')
    #print (globTotalPower)

    for load in loads:
        subTotalPower = load.howMany * load.power 
        ##totalPower = totalPower + subTotalPower
        #globTotalPower = globTotalPower + subTotalPower
        #totalPower11 = totalPower(int(subTotalPower))        
        #totalPower11 = totalPowerCalc(5)        
        #totalPower11 = totalPowerCalc(subTotalPower) 
        #totalPower1 = totalCalc(subTotalPower) 
        totalCalc1 = totalCalc(subTotalPower) 
        #print ('totalPower1')       
        #print (totalPower1)       
        subTotalEnergyDay = subTotalPower * load.durationTotal

        #global totalEnergyDay


        totalEnergyDay = totalEnergyDay + subTotalEnergyDay   

        print ('totalEnergyDay')
        print (totalEnergyDay)

     

        subTotalEnergyNight = subTotalPower * load.durationNight
        totalEnergyNight = totalEnergyNight + subTotalEnergyNight        

    totalPower10 = totalPower
    print ('totalPower10')
    print (totalPower10)
    return render_template('listLoads.html', loads=loads, fields=fields, totalCalc1=totalCalc1, totalEnergyDay=totalEnergyDay, totalEnergyNight=totalEnergyNight)






# Create a new student
@app.route('/createLoad', methods=['GET', 'POST'])
def createLoad():
    table1, fields = get_table1_and_fields()
    if request.method == 'POST':
        data = {field: request.form[field] for field in fields}
        insert_query = table1.insert().values(**data)
        db.session.execute(insert_query)
        db.session.commit()
        return redirect(url_for('listLoads'))
    return render_template('createLoad.html', fields=fields)

# Update a student
@app.route('/updateLoad/<int:id>', methods=['GET', 'POST'])
def updateLoad(id):
    table1, fields = get_table1_and_fields()
    load = db.session.query(table1).filter(table1.c.id == id).first()
    if request.method == 'POST':
        data = {field: request.form[field] for field in fields}
        update_query = table1.update().where(table1.c.id == id).values(**data)
        db.session.execute(update_query)
        db.session.commit()
        return redirect(url_for('listLoads'))
    return render_template('updateLoad.html', load=load, fields=fields, table1=table1)

# Delete a student
@app.route('/deleteLoad/<int:id>', methods=['GET', 'POST'])
def deleteLoad(id):
    table1, _ = get_table1_and_fields()
    if request.method == 'POST':
        delete_query = table1.delete().where(table1.c.id == id)
        db.session.execute(delete_query)
        db.session.commit()
        return redirect(url_for('listLoads'))
    student = db.session.query(table1).filter(table1.c.id == id).first()
    return render_template('deleteLoad.html', student=student)


##### panel

@app.route('/panel')
def listPanels():
    table2, fields = get_table2_and_fields()
    panels = db.session.query(table2).all()
    print ('totalPower1')
    print (totalPower1)
    totalWattDay = 0
    totalWattNight = 0
    #totalPower2 = test()
    #print ('totalPower2')
    #print (totalPower2)

    global totalEnergyDay
    print ('totalEnergyDay')
    print (totalEnergyDay)

    for panel in panels:
        totalWattDay = totalWattDay + (panel.power * panel.howMany * panel.durationTotalDay)
        print ('totalWattDay')
        print (totalWattDay)

        totalEnergyDay =  totalEnergyDayCalc(totalWattDay)
        print ('totalEnergyDay')
        print (totalEnergyDay)

        #totalWattNight = totalWattNight + (panel.power * panel.howMany * panel.durationNight)
        totalWattNight = totalWattNight + (panel.power * panel.howMany * 5)
        print ('totalWattNight')
        print (totalWattNight)



        totalEnergyNight =  totalEnergyDayCalc(totalWattNight)
        print ('totalEnergyNight')
        print (totalEnergyNight)


    return render_template('listPanels.html', panels=panels, fields=fields, totalWattDay=totalWattDay, totalEnergyDay=totalEnergyDay, totalEnergyNight=totalEnergyNight)



# Create a new panel
@app.route('/createPanel', methods=['GET', 'POST'])
def createPanel():
    table2, fields = get_table2_and_fields()
    print ('fields')
    print (fields)
    if request.method == 'POST':
        data = {field: request.form[field] for field in fields}
        insert_query = table2.insert().values(**data)
        db.session.execute(insert_query)
        db.session.commit()
        return redirect(url_for('listPanels'))
    return render_template('createPanel.html', fields=fields)

# Update a panel
@app.route('/updatePanel/<int:id>', methods=['GET', 'POST'])
def updatePanel(id):
    table2, fields = get_table2_and_fields()
    panel = db.session.query(table2).filter(table2.c.id == id).first()
    if request.method == 'POST':
        data = {field: request.form[field] for field in fields}
        print ('data')
        print (data)
        update_query = table2.update().where(table2.c.id == id).values(**data)
        db.session.execute(update_query)
        db.session.commit()
        return redirect(url_for('listPanels'))
    return render_template('updatePanel.html', panel=panel, fields=fields, table2=table2)


# Delete a panel
@app.route('/deletePanel/<int:id>', methods=['GET', 'POST'])
def deletePanel(id):
    table2, _ = get_table2_and_fields()
    if request.method == 'POST':
        delete_query = table2.delete().where(table2.c.id == id)
        db.session.execute(delete_query)
        db.session.commit()
        return redirect(url_for('listPanels'))
    panel = db.session.query(table2).filter(table2.c.id == id).first()
    return render_template('deletePanel.html', panel=panel)





## batterry

@app.route('/batterry')
def listBatterrys():
    table3, fields = get_table3_and_fields()
    batterrys = db.session.query(table3).all()
    
    #totalEnergyNight =  totalEnergyDayCalc(totalEnergyNight)
    totalEnergyNight =  totalEnergyDayCalc(0)
    print ('totalEnergyNight')
    print (totalEnergyNight)


    return render_template('listBatterrys.html', batterrys=batterrys, fields=fields, totalEnergyNight=totalEnergyNight)


# Create a new batterry
@app.route('/createBatterry', methods=['GET', 'POST'])
def createBatterry():
    table3, fields3 = get_table3_and_fields()
    if request.method == 'POST':
        data = {field3: request.form[field3] for field3 in fields3}
        print ('data')
        print (data)
        insert_query = table3.insert().values(**data)
        db.session.execute(insert_query)
        db.session.commit()
        return redirect(url_for('listBatterrys'))
    return render_template('createBatterry.html', fields3=fields3)

# Update a batterry
@app.route('/updateBatterry/<int:id>', methods=['GET', 'POST'])
def updateBatterry(id):
    table3, fields = get_table3_and_fields()
    batterry = db.session.query(table3).filter(table3.c.id == id).first()
    if request.method == 'POST':
        data = {field: request.form[field3] for field3 in fields3}
        update_query = table3.update().where(table3.c.id == id).values(**data)
        db.session.execute(update_query)
        db.session.commit()
        return redirect(url_for('listBatterrys'))
    return render_template('updateBatterry.html', batterry=batterry, fields=fields
)


# Delete a batterry
@app.route('/deleteBatterry/<int:id>', methods=['GET', 'POST'])
def deleteBatterry(id):
    table3, _ = get_table3_and_fields()
    if request.method == 'POST':
        delete_query = table3.delete().where(table3.c.id == id)
        db.session.execute(delete_query)
        db.session.commit()
        return redirect(url_for('listBatterys'))
    batterry = db.session.query(table3).filter(table3.c.id == id).first()
    return render_template('deleteBatterry.html', batterry=batterry)


@app.route('/powerEnergy')
def listPowerEnergys():
    table4, fields = get_table4_and_fields()
    powerEnergys = db.session.query(table4).all()
    #print ('totalPower10')
    #print (totalPower10)
    totalWattDay = 0
    #totalPower2 = test()
    #print ('totalPower2')
    #print (totalPower2)

    #for powerEnergy in powerEnergys:
        #totalWattDay = totalWattDay + (powerEnergy.power * powerEnergy.howMany * powerEnergy.durationTotalDay)
    return render_template('listPowerEnergys.html', powerEnergys=powerEnergys, fields=fields, totalPower10=totalPower10)


# Create a new panel
@app.route('/createPowerEnergy', methods=['GET', 'POST'])
def createPowerEnergy():
    table4, fields = get_table4_and_fields()
    print ('fields')
    print (fields)
    if request.method == 'POST':
        data = {field: request.form[field] for field in fields}
        print ('data')
        print (data)
        insert_query = table4.insert().values(**data)
        db.session.execute(insert_query)
        db.session.commit()
        return redirect(url_for('listPowerEnergys'))
    return render_template('createPowerEnergy.html', fields=fields)

# Update a panel
@app.route('/updatePowerEnergy/<int:id>', methods=['GET', 'POST'])
def updatePowerEnergy(id):
    table4, fields = get_table4_and_fields()
    powerEnergy = db.session.query(table4).filter(table4.c.id == id).first()
    if request.method == 'POST':
        data = {field: request.form[field] for field in fields}
        update_query = table4.update().where(table4.c.id == id).values(**data)
        db.session.execute(update_query)
        db.session.commit()
        return redirect(url_for('listPowerEnergys'))
    return render_template('updatePowerEnergy.html', powerEnergy=powerEnergy, fields=fields)

# Delete a panel
@app.route('/deletePowerEnergy/<int:id>', methods=['GET', 'POST'])
def deletePowerEnergy(id):
    table4, _ = get_table4_and_fields()
    if request.method == 'POST':
        delete_query = table4.delete().where(table4.c.id == id)
        db.session.execute(delete_query)
        db.session.commit()
        return redirect(url_for('listPowerEnergys'))
    powerEnergy = db.session.query(table4).filter(table4.c.id == id).first()
    return render_template('deletePowerEnergy.html', powerEnergy=powerEnergy)








# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    #app.run(debug=True)
