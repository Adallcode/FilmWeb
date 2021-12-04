import requests
from MySQLManager import AddToDatabase, filmExist
from flask import flash

class API:
    def __init__(self, config: dict, title: str) -> None:
        self.key = '43e40459'
        self.url = 'http://www.omdbapi.com/?'
        self.config = config
        self.title = title
        self.path = ''
        self.res = {}
        # In this list will be stored: json, title and  imgPath
        self.data = []


    def execute(self, ) -> bool:

        try:
            dic = {"apikey": self.key, "t": self.title}

            self.res = requests.get(self.url, params=dic)

            # Make a correct image path without space in the path to access the image
            list1 = self.title.split(' ')
            self.path = "static/images/" + ''.join(list1)
            self.path += '.png'
            
            # Check if the request was successfull
            if self.res.json()['Response'] == 'False':
                flash('Film with this title not found', category="info")
                return False

            if self.createImg():
                return True
            else:
                return False

        except Exception as err:
            print("Error in **API execute**", err)
            return False
    

    def createImg(self, ) -> bool:

        try:

            img = requests.get(self.res.json()['Poster'])
            file = open(self.path, 'wb')
            file.write(img.content)
            file.close()

            '''Add this new data in the database'''
            '''The path attribute was create in the execute funtion'''
            Temp = (self.res.json(), self.title, self.path, )

            if AddToDatabase(Temp, self.config):
                return True
            else:
                return False

        except Exception as err:
            print("Error in **API createImg**", err)
            flash('In this moment we are out of service please try later.', category="info")
            return False
    


    '''If the film exist just take the data'''
    
    def exist(self, show: str = 'show') -> bool:
        if filmExist(self.title, self.data, self.config, show):
            return True
        else:
            return False


    '''Pop the first 2 elements in the list'''

    def delete2(self, ) -> None:
        
        # Use the ( del ) to delete
        del self.data[0:2]


    '''Add the data to the list when a new film is created'''

    def addToList(self, ):
        
        keys = ('Released', 'Genre', 'Director', 'Writer', 'Actors', 'Awards')

        for i in keys:
            self.data.append(self.res.json()[ i ])
