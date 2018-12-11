import pyodbc
import random

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=S01519-7480;'
                      'Database=gk;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()


def getrandomfeature():
    cursor.execute('SELECT * FROM dbo.Features')
    return Feature(random.choice(cursor.fetchall()))


class Feature:
    """Feature of a quadrant"""

    def __init__(self, feature):
        self.id = feature[0]
        self.code = feature[1]
        self.description = feature[2]
