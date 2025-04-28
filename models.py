from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the table dynamically
def create_table1():
    from sqlalchemy import Table, Column, Integer, String, MetaData
    metadata = MetaData()
    table1 = Table(
        #'student', metadata,
        'load', metadata,
        Column('id', Integer, primary_key=True),
        # from here zou chan change add delete the field of your new table
        Column('name', String(100), nullable=False),
        Column('howMany', Integer, nullable=False),
        Column('power', Integer, nullable=False),
        Column('durationTotal', Integer, nullable=False),
        Column('durationNight', Integer, nullable=False),
    )
    return table1

# Get the table and field names
def get_table1_and_fields():
    table1 = create_table1()
    fields = [column.name for column in table1.columns if column.name != 'id']
    return table1, fields

def create_table2():
    from sqlalchemy import Table, Column, Integer, String, MetaData
    metadata = MetaData()
    table2 = Table(
        'panel', metadata,
        Column('id', Integer, primary_key=True),
        # from here you chan change add delete the field of your new table
        Column('name', String(100), nullable=False),
        Column('howMany', Integer, nullable=False),
        Column('power', Integer, nullable=False),
        Column('durationTotalDay', Integer, nullable=False),
    )
    return table2

# Get the table and field names
def get_table2_and_fields():
    table2 = create_table2()
    fields = [column.name for column in table2.columns if column.name != 'id']
    return table2, fields


# Define the table dynamically
def create_table3():
    from sqlalchemy import Table, Column, Integer, String, MetaData
    metadata = MetaData()
    table3 = Table(
        'battery', metadata,
        Column('id', Integer, primary_key=True),
        # from here zou chan change add delete the field of your new table
        Column('name', String(100), nullable=False),
        Column('howMany', Integer, nullable=False),
        Column('power', Integer, nullable=False),
        Column('voltage', Integer, nullable=False),
    )
    return table3

# Get the table and field names
def get_table3_and_fields():
    table3 = create_table3()
    fields = [column.name for column in table3.columns if column.name != 'id']
    return table3, fields

# Define the table dynamically
def create_table4():
    from sqlalchemy import Table, Column, Integer, String, MetaData
    metadata = MetaData()
    table4 = Table(
        'wattEnergy', metadata,
        Column('id', Integer, primary_key=True),
        # from here zou chan change add delete the field of your new table
        Column('totalPower', Integer(), nullable=False), 
        Column('totalEnergyDay', Integer, nullable=False), 
        Column('totalEnergyNight', Integer, nullable=False), 
    )
    return table4

# Get the table and field names
def get_table4_and_fields():
    table4 = create_table4()
    fields = [column.name for column in table4.columns if column.name != 'id']
    return table4, fields





# Create the table in the database
def initialize_database(app):
    with app.app_context():
        table1, _ = get_table1_and_fields()
        table1.create(db.engine, checkfirst=True)

        table2, _ = get_table2_and_fields()
        table2.create(db.engine, checkfirst=True)

        table3, _ = get_table3_and_fields()
        table3.create(db.engine, checkfirst=True)

        table4, _ = get_table4_and_fields()
        table4.create(db.engine, checkfirst=True)


