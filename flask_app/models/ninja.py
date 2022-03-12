from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:
    db = 'dojos_and_ninjas1'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of dojos
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def getOne(cls,data):
        query = 'SELECT * FROM ninjas WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results(0))

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);'
        results = connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE ninjas SET name=%(name)s;'
        results = connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s'
        results = connectToMySQL(cls.db).query_db(query,data)