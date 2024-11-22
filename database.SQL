CREATE TABLE product (
    ProductID INT PRIMARY KEY IDENTITY(1,1), 
    Name NVARCHAR(255) NOT NULL,            
    Quantity INT NOT NULL                   
);

INSERT INTO product (Name, Quantity)
VALUES 
('Laptop', 10), 
('Mouse', 50), 
('Keyboard', 20), 
('Monitor', 15);