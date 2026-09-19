import mysql.connector
from .database import MySQLDataBase

TABLE_NAME = 'categories'

class Categories:
    """
    Класс таблицы Categories
    
    Methods:
        
        select_all_categories(): Получение всех категорий из таблицы
        select_category_by_id(id:int): Получение категории по id
        create_category(name:str,slug:str): Создание новой категории
        update_category(category_id:int, **kwargs:list): Обновление категории
        delete_category(category_id:int): Удаление категории
    """
    
    
    @staticmethod
    def select_all_categories():
        """
        Получение всех категорий из таблицы
        """
        
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
    def select_category_by_id(id:int):
        """
        Получение категории по id
        
        Args:
            id: ID категории
        """
        
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
    def isExistCategoryByName(name:str):
        db = MySQLDataBase()
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)
                    
            try:
                cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE name = '{name}'")
                row = cursor.fetchone()
            except mysql.connector.Error as e:
                print(f"Ошибка запроса {e}")
            finally:
                cursor.close()
                db.connection.disconnect()
                
            if  row is None:
                return False

            return True

    @staticmethod
    def create_category(name:str,slug:str):
        """
        Создание новой категории
        Args:
            name: Название категории
            slug: Англ версия названия
        """
        
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
    def update_category(category_id:int, **kwargs:list):
        """
        Обновление категории
        
        Args:
            category_id: ID категории
            **kwargs: список полей для изменения
        """
        
        db = MySQLDataBase()
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)            
                        
            try:
                updates = []
                            
                for key,value in kwargs.items():
                    if key in ['name', 'slug']:
                        updates.append(f'{key} = "{value}"')
                    
                    if not updates:
                        return False
                    
                query = f"UPDATE {TABLE_NAME} SET {', '.join(updates)} WHERE id = {category_id}"
                            
                cursor.execute(query)
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
    def delete_category(category_id:int):
        """
        Удаление категории
        
        Args:
            category_id: ID категории
        """
        
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