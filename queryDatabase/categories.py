import mysql.connector
from database import MySQLDataBase

TABLE_NAME = 'categories'

class Categories:
    @staticmethod
    def select_all_categories():
        db = MySQLDataBase()
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)
            
            try:
                cursor.execute(f"SELECT * FROM {TABLE_NAME}")
                return cursor.fetchall()
            except mysql.connector.Error as e:
                print(f"Ошибка запроса {e}")
            finally:
                cursor.close()
                db.connection.close()
                
    @staticmethod
    def select_category_by_id(id):
        db = MySQLDataBase()
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)
            
            try:
                cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = {id}")
                return cursor.fetchone()
            except mysql.connector.Error as e:
                print(f"Ошибка запроса {e}")
            finally:
                cursor.close()
                db.connection.disconnect()

    @staticmethod
    def create_category(name,slug):
        db = MySQLDataBase()
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)            
                
            try:
                cursor.execute(f'INSERT INTO {TABLE_NAME}(name,slug) VALUES ("{name}","{slug}")')
                db.connection.commit()
                category_id = cursor.lastrowid
                print(f"Создана категория {name} с ID {category_id}")
                return category_id
            except mysql.connector.Error as e:
                print(f"Ошибка запроса {e}")
                db.connection.rollback()
                return None
            finally:
                cursor.close()    
                db.connection.disconnect()
        
    @staticmethod
    def update_category(self, category_id, **kwargs):
        db = MySQLDataBase()
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)            
                        
            try:
                updates = []
                values = []
                            
                for key, value in kwargs.items():
                    if key in ['name', 'slug']:
                        updates.append(f"{key} = %s")
                        values.append(value)
                    
                    if not updates:
                        return False
                    
                query = f"UPDATE {TABLE_NAME} SET {', '.join(updates)} WHERE id = %s"
                values.append(category_id)            
                            
                cursor.execute(query, values)
                db.connection.commit()
                return cursor.rowcount > 0
            except mysql.connector.Error as e:
                print(f"Ошибка запроса {e}")
                db.connection.rollback()
                return None
            finally:
                cursor.close()    
                db.connection.disconnect()
        
    @staticmethod
    def delete_category(category_id):
        db = MySQLDataBase()
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)            
                        
        try:
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = {category_id}")
            db.connection.commit()
        except mysql.connector.Error as e:
            print(f"Ошибка запроса {e}")
            db.connection.rollback()
        finally:
            cursor.close()    
            db.connection.disconnect()