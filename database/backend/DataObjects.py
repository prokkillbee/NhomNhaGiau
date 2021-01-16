import psycopg2
from BusinessObjects import Customer as CustomerEntity
from BusinessObjects import Categories as CategoriesEntity
from BusinessObjects import Employees as EmployeesEntity
from BusinessObjects import OrderDetails as OrderDetailsEntity
from BusinessObjects import Orders as OrdersEntity
from BusinessObjects import Products as ProductsEntity
from BusinessObjects import Shippers as ShippersEntity
from BusinessObjects import Suppliers as SuppliersEntity


class Customer:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, customer):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO TblCustomers(CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (%s, %s, %s, %s, %s, %s)"
            record_to_insert = (customer.CustomerName, customer.ContactName, customer.Address, customer.City, customer.PostalCode, customer.Country)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblCustomers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            # sql = "SELECT * FROM TblCustomers"
            sql = "SELECT * FROM TblCustomers"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = CustomerEntity()
                c.fetch_data(row)
                result.append(c.to_json())
                con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self , customer : CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM TblCustomers WHERE CustomerID = %s"
            cur.execute(sql, (customer.CustomerID, ))
            con.commit() 
            row = cur.fetchone()
            if row:
                c = CustomerEntity()
                c.fetch_data(row)
                return c , 200
            con.close()
            return 'Customer ID not found' , 404
            
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def delete(self , customer : CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM TblCustomers WHERE CustomerID = %s"
            cur.execute(sql, (customer.CustomerID,))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted customer' , 200
            con.close()
            return 'Customer ID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self , customer : CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE TblCustomers SET CustomerName = %s, ContactName = %s, Address = %s, City = %s, PostalCode = %s, Country = %s WHERE CustomerID = %s"
            cur.execute(sql, (customer.CustomerName, customer.ContactName, customer.Address, customer.City,customer.PostalCode, customer.Country, customer.CustomerID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated customer' , 200
            con.close()
            return 'Customer ID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
# -------------------------------------------------------

class Categories:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, categories : CategoriesEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO Categories(CategoryName, Description) VALUES (%s, %s)"
            record_to_insert = (categories.CategoryName, categories.Description)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert Categories successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            # sql = "SELECT * FROM TblCustomers"
            sql = "SELECT * FROM Categories"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = CategoriesEntity()
                c.fetch_data(row)
                result.append(c.to_json())
                con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()    
    def get_by_id(self , categories : CategoriesEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Categories WHERE CategoryID= %s"
            cur.execute(sql, (categories.CategoryID, ))
            con.commit() 
            row = cur.fetchone()
            if row:
                c = CategoriesEntity()
                c.fetch_data(row)
                return c , 200
            con.close()
            return 'CategoryID not found' , 404
            
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()   
    def delete(self , categories : CategoriesEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM Categories WHERE CategoryID = %s"
            cur.execute(sql, (categories.CategoryID,))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted Categories' , 200
            con.close()
            return 'Categories ID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self , categories : CategoriesEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE Categories SET CategoryName = %s, Description= %s WHERE CategoryID= %s"
            cur.execute(sql, (categories.CategoryName , categories.Description , categories.CategoryID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated Categories ' , 200
            con.close()
            return 'Categories ID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()     
# -------------------------------------------------------------------------------------------------------------------------
class Employees:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, employess: EmployeesEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO Employees(LastName, FirstName, BirthDate, Photo, Notes) VALUES (%s, %s, %s, %s, %s)"
            record_to_insert = (employess.LastName, employess.FirstName , employess.BirthDate, employess.Photo , employess.Notes)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert Employees successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            # sql = "SELECT * FROM TblCustomers"
            sql = "SELECT * FROM Employees"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = EmployeesEntity()
                c.fetch_data(row)
                result.append(c.to_json())
                con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()    
    def get_by_id(self , employees : EmployeesEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Employees WHERE EmployeeID= %s"
            cur.execute(sql, (employees.EmployeeID, ))
            con.commit() 
            row = cur.fetchone()
            if row:
                c = EmployeesEntity()
                c.fetch_data(row)
                return c , 200
            con.close()
            return 'EmployeesID not found' , 404
            
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()   
    def delete(self , employees : EmployeesEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM Employees WHERE EmployeeID = %s"
            cur.execute(sql, (employees.EmployeeID,))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted Employees' , 200
            con.close()
            return 'Employees ID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self , employees : EmployeesEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE Employees SET LastName = %s, FirstName= %s, BirthDate = %s,Photo=%s, Notes=%s WHERE EmployeeID= %s"
            cur.execute(sql, (employees.LastName , employees.FirstName , employees.BirthDate, employees.Photo, employees.Notes , employees.EmployeeID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated Employees ' , 200
            con.close()
            return 'Employees ID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()  
# --------------------------------------------------------------------------------------------------

class OrderDetails:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, oderdetails : OrderDetailsEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO OrderDetails(OrderID, ProductID, Quantity) VALUES (%s, %s, %s)"
            record_to_insert = (oderdetails.OrderID, oderdetails.ProductID, oderdetails.Quantity)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert OrderDetails successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM OrderDetails"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = OrderDetailsEntity()
                c.fetch_data(row)
                result.append(c.to_json())
                con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()    
    def get_by_id(self , oderdetails : OrderDetailsEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM OrderDetails WHERE OrderDetailID= %s"
            cur.execute(sql, (oderdetails.OrderDetailID, ))
            con.commit() 
            row = cur.fetchone()
            if row:
                c = EmployeesEntity()
                c.fetch_data(row)
                return c , 200
            con.close()
            return 'OrderDetails' , 404
            
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()   
    def delete(self ,  oderdetails : OrderDetailsEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM OrderDetails WHERE OrderDetailID = %s"
            cur.execute(sql, (oderdetails.OrderDetailID,))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted OrderDetails' , 200
            con.close()
            return 'OrderDetails ID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self , oderdetails : OrderDetailsEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE OrderDetails SET OrderID = %s, ProductID = %s, Quantity = %s WHERE OrderDetailID= %s"
            cur.execute(sql, (oderdetails.OrderID , oderdetails.ProductID , oderdetails.Quantity , oderdetails.OrderDetailID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated OrderDetails ' , 200
            con.close()
            return 'OrderDetailsID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()  
# ---------------------------------------------------
class Orders:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, oders : OrdersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO Orders(CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (%s, %s, %s, %s)"
            record_to_insert = (oders.CustomerID ,oders.EmployeeID , oders.OrderDate, oders.ShipperID)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert Orders successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Orders "
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = OrdersEntity()
                c.fetch_data(row)
                result.append(c.to_json())
                con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()    
    def get_by_id(self , oders : OrdersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Orders WHERE OrderID = %s"
            cur.execute(sql, (oders.OrderID, ))
            con.commit() 
            row = cur.fetchone()
            if row:
                c = OrdersEntity()
                c.fetch_data(row)
                return c , 200
            con.close()
            return 'OrderDetails' , 404
            
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()   
    def delete(self ,  oders : OrdersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM Orders WHERE OrderID= %s"
            cur.execute(sql, (oders.OrderID,))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted Orders' , 200
            con.close()
            return 'Orders ID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self , oders : OrdersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE Orders SET CustomerID = %s, EmployeeID = %s, OrderDate  = %s , ShipperID = %s  WHERE OrderID= %s"
            cur.execute(sql, (oders.CustomerID , oders.EmployeeID , oders.OrderDate , oders.ShipperID , oders.OrderID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated Orders ' , 200
            con.close()
            return 'OrdersID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close() 
# --------------------------------------------------------------------
class Products:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, products : ProductsEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO Products(ProductName, SupplierID , CategoryID, Unit ,Price ) VALUES (%s, %s, %s, %s, %s)"
            record_to_insert = (products.ProductName , products.SupplierID , products.CategoryID , products.Unit, products.Price)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert Products successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Products "
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = ProductsEntity()
                c.fetch_data(row)
                result.append(c.to_json())
                con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()    
    def get_by_id(self , products : ProductsEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Products WHERE ProductID = %s"
            cur.execute(sql, (products.ProductID, ))
            con.commit() 
            row = cur.fetchone()
            if row:
                c = ProductsEntity()
                c.fetch_data(row)
                return c , 200
            con.close()
            return 'OrderDetails' , 404
            
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()   
    def delete(self , products : ProductsEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM Products WHERE ProductID= %s"
            cur.execute(sql, (products.ProductID,))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted ProductID' , 200
            con.close()
            return 'ProductID ID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self , products : ProductsEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE Products SET ProductName = %s, SupplierID = %s, CategoryID  = %s , Unit = %s, Price =%s  WHERE ProductID= %s"
            cur.execute(sql, (products.ProductName , products.SupplierID , products.CategoryID , products.Unit , products.Price , products.ProductID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated Products ' , 200
            con.close()
            return 'Products not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close() 
# -------------------------------------------------------------------
class Shippers:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, shippers : ShippersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO Shippers(ShipperName, Phone ) VALUES (%s, %s)"
            record_to_insert = (shippers.ShipperName , shippers.Phone)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert Shippers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Shippers"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = ShippersEntity()
                c.fetch_data(row)
                result.append(c.to_json())
                con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()    
    def get_by_id(self , shippers : ShippersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Shippers WHERE ShipperID = %s"
            cur.execute(sql, (shippers.ShipperID, ))
            con.commit() 
            row = cur.fetchone()
            if row:
                c = ShippersEntity()
                c.fetch_data(row)
                return c , 200
            con.close()
            return 'Shipper' , 404
            
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()   
    def delete(self , shippers : ShippersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM Shippers WHERE ShipperID= %s"
            cur.execute(sql, (shippers.ShipperID ,))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted ShipperID' , 200
            con.close()
            return 'ShipperID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self , shippers : ShippersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE Shippers SET ShipperName = %s, Phone = %s WHERE ShipperID= %s"
            cur.execute(sql, ( shippers.ShipperName , shippers.Phone , shippers.ShipperID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Shippers Products ' , 200
            con.close()
            return 'Shippers not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close() 
class Suppliers:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, suppliers : SuppliersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO Suppliers(SupplierName,ContactName,Address, City , PostalCode , Country ,  Phone ) VALUES (%s, %s,%s, %s,%s, %s,%s)"
            record_to_insert = (suppliers.SupplierName, suppliers.ContactName , suppliers.Address , suppliers.City , suppliers.PostalCode , suppliers.Country , suppliers.Phone)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert Shippers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Suppliers"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = SuppliersEntity()
                c.fetch_data(row)
                result.append(c.to_json())
                con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()    
    def get_by_id(self , suppliers : SuppliersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Suppliers WHERE SupplierID = %s"
            cur.execute(sql, (suppliers.SupplierID, ))
            con.commit() 
            row = cur.fetchone()
            if row:
                c = ShippersEntity()
                c.fetch_data(row)
                return c , 200
            con.close()
            return 'Shipper' , 404
            
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()   
    def delete(self , suppliers : SuppliersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM Suppliers WHERE SupplierID= %s"
            cur.execute(sql, (suppliers.SupplierID ,))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted SuppliersID' , 200
            con.close()
            return 'SuppliersID not found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self , suppliers : SuppliersEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE Suppliers SET SupplierName = %s,ContactName = %s ,Address= %s , City = %s , Country = %s , Phone = %s  WHERE SupplierId= %s"
            cur.execute(sql, ( suppliers.SupplierName , suppliers.ContactName , suppliers.Address , suppliers.City , suppliers.Country , suppliers.Phone , suppliers.SupplierID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'SuppliersID update' , 200
            con.close()
            return 'SuppliersIDnot found' ,200
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close() 

if __name__ == "__main__":
    print('this is data object package')