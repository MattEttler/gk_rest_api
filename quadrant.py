import pyodbc
import random
import image

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=S01519-7480;'
                      'Database=gk;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()


def getrandomquadrants():
    cursor.execute(
        'SELECT QuadrantID, ImageID, QuadrantAddress FROM dbo.Quadrants')
    return Quadrant(random.choice(cursor.fetchall()))


class Quadrant:
    """Quadrant of an Image"""

    def __init__(self, quad):
        self.id = quad[0]
        self.image = image.getimage(quad[1])
        self.quadrant_address = quad[2]
