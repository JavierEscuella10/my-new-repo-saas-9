from services.database import db_connect


                    
def DB_access(db_query,variables):
 conn = db_connect()
 cursor = conn.cursor()
 variable_values = [variables.get(key) for key in variables.keys()]
 cursor.execute(db_query,variable_values)
 #commit_or_fetch
 conn.close()
 #return_db_response

#code_here
                     

                    
def DB(db_query,variables):
 conn = db_connect()
 cursor = conn.cursor()
 variable_values = [variables.get(key) for key in variables.keys()]
 cursor.execute(db_query,variable_values)
 #commit_or_fetch
 conn.close()
 #return_db_response

#code_here
                     