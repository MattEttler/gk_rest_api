import pyodbc
import random

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=S01519-7480;'
                      'Database=gk;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()


def getrandomimage():
    cursor.execute('SELECT ImageID, ImageUrl FROM dbo.Images')
    return Image(random.choice(cursor.fetchall()))


def getimage(imageid):
    cursor.execute(
        'SELECT ImageID, ImageUrl FROM dbo.Images WHERE ImageID = {0}'.format(int(imageid)))
    return Image(random.choice(cursor.fetchall()))


class Image:
    """Image"""

    def __init__(self, image):
        self.id = image[0]
        self.url = image[1]
