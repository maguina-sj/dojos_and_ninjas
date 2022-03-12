from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    db = 'dojos_and_ninjas1'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojos_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at':row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name) VALUES(%(name)s);'
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE dojos SET name=%(name)s;'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM dojos WHERE id = %(id)s'
        return connectToMySQL(cls.db).query_db(query,data)