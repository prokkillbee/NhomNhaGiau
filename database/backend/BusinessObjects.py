class Customer:
    def __init__(self, CustomerID = None, CustomerName = None, ContactName= None, Address= None, City= None, PostalCode= None, Country= None):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.ContactName = ContactName
        self.Address = Address
        self.City = City
        self.PostalCode = PostalCode
        self.Country = Country
    def fetch_data(self , data):
        self.CustomerID = data[0]
        self.CustomerName = data[1]
        self.ContactName = data[2]
        self.Address = data[3]
        self.City = data[4]
        self.PostalCode = data[5]
        self.Country = data[6]
    def to_json(self):
        return{
            'CustomerId' : self.CustomerID,
            'CustomerName': self.CustomerName,
            'ContactName': self.ContactName,
            'Address': self.Address,
            'City': self.City,
            'PostalCode': self.PostalCode,
            'Country': self.Country
        }
class Categories:
    def __init__(self, CategoryID = None, CategoryName = None, Description = None):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName
        self.Description = Description
    def fetch_data(self,data):
        self.CategoryID = data[0]
        self.CategoryName = data[1]
        self.Description = data[2]
    def to_json(self):
        return{
            'CategoryID' : self.CategoryID,
            'CategoryName' : self.CategoryName,
            'Description' : self.Description
        }
class Employees:
    def __init__(self,EmployeeID = None, LastName = None, FirstName = None, BirthDate = None, Photo = None, Notes = None):
        self.EmployeeID = EmployeeID
        self.LastName = LastName
        self.FirstName = FirstName
        self.BirthDate = BirthDate
        self.Photo = Photo
        self.Notes = Notes
    def fetch_data(self,data):
        self.EmployeeID = data[0]
        self.LastName = data[1]
        self.FirstName = data[2]
        self.BirthDate = data[3]
        self.Photo = data[4]
        self.Notes = data[5]
    def to_json(self):
        return{
            'EmployeeID' : self.EmployeeID,
            'LastName' : self.LastName,
            'FirstName' : self.FirstName,
            'BirthDate' : self.BirthDate,
            'Photo' : self.Photo,
            'Notes' : self.Notes
        }
class OrderDetails:
    def __init__(self, OrderDetailID = None, OrderID = None, ProductID = None, Quantity = None):
        self.OrderDetailID = OrderDetailID
        self.OrderID = OrderID
        self.ProductID = ProductID
        self.Quantity = Quantity
    def fetch_data(self,data):
        self.OrderDetailID = data[0]
        self.OrderID = data[1]
        self.ProductID = data[2]
        self.Quantity = data[3]
    def to_json(self):
        return{
            'OrderDetailID' : self.OrderDetailID,
            'OrderID' : self.OrderID,
            'ProductID' : self.ProductID,
            'Quantity' : self.Quantity
        }
class Orders:
    def __init__(self, OrderID = None, CustomerID = None, EmployeeID = None, OrderDate = None, ShipperID = None):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.EmployeeID = EmployeeID
        self.OrderDate = OrderDate
        self.ShipperID = ShipperID
    def fetch_data(self,data):
        self.OrderID = data[0]
        self.CustomerID = data[1]
        self.EmployeeID = data[2]
        self.OrderDate = data[3]
        self.ShipperID = data[4]
    def to_json(self):
        return{
            'OrderID' : self.OrderID,
            'CustomerID' : self.CustomerID,
            'EmployeeID' : self.EmployeeID,
            'OrderDate' : self.OrderDate,
            'ShipperID' : self.ShipperID
        }
class Products:
    def __init__(self,ProductID = None, ProductName = None, SupplierID = None, CategoryID = None, Unit = None, Price = None):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.SupplierID = SupplierID
        self.CategoryID = CategoryID
        self.Unit = Unit
        self.Price = Price
    def fetch_data(self,data):
        self.ProductID = data[0]
        self.ProductName = data[1]
        self.SupplierID = data[2]
        self.CategoryID = data[3]
        self.Unit = data[4]
        self.Price = data[5]
    def to_json(self):
        return{
            'ProductID' : self.ProductID,
            'ProductName' : self.ProductName,
            'SupplierID' : self.SupplierID,
            'CategoryID' : self.CategoryID,
            'Unit' : self.Unit,
            'Price' : self.Price
        }

class Shippers:
    def __init__(self, ShipperID = None, ShipperName = None, Phone = None):
        self.ShipperID = ShipperID
        self.ShipperName = ShipperName
        self.Phone = Phone
    def fetch_data(self,data):
        self.ShipperID = data[0]
        self.ShipperName = data[1]
        self.Phone = data[2]
    def to_json(self):
        return{
            'ShipperID' : self.ShipperID,
            'ShipperName' : self.ShipperName,
            'Phone' : self.Phone
        }
class Suppliers:
    def __init__(self, SupplierID = None, SupplierName = None, ContactName = None, Address = None, City = None, PostalCode = None, Country = None, Phone = None):
        self.SupplierID = SupplierID
        self.SupplierName = SupplierName
        self.ContactName = ContactName
        self.Address = Address
        self.City = City
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
    def fetch_data(self,data):
        self.SupplierID = data[0]
        self.SupplierName = data[1]
        self.ContactName = data[2]
        self.Address = data[3]
        self.City = data[4]
        self.PostalCode = data[5]
        self.Country = data[6]
        self.Phone = data[7]
    def to_json(self):
        return{
            'SupplierId' : self.SupplierID,
            'SupplierName' : self.SupplierName,
            'ContactName' : self.ContactName,
            'Address' : self.Address,
            'City' : self.City,
            'Country' : self.Country,
            'Phone' : self.Phone
        }

if __name__ == "__main__":
    print('this is business object package')