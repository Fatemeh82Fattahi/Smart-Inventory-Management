# Smart Inventory Management System (Digikala Case Study)

This project is a smart inventory monitoring tool designed for modern fulfillment centers like Digikala. It bridges a relational database management system (SQL Server) with an automation script (Python) to keep track of product stocks in real-time and alert managers about critical low-stock items.

##  Tech Stack & Architecture
* Database: SQL Server (SSMS) - Handles relational data, automatic indexing, and constraints.
* Backend: Python 3 - Connects to SQL Server using pyodbc to execute queries and process logic.
* Core Logic: Uses JOIN queries and conditional thresholds (MinRequired) to detect shortages.

---

## floppy_disk: Database Schema (SQL Server)
Run this script in your SSMS to create the database and sample dataset:

`sql
CREATE DATABASE SmartInventoryDB;
GO
USE SmartInventoryDB;

CREATE TABLE Products (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    SKU VARCHAR(50) UNIQUE NOT NULL,
    Name NVARCHAR(100) NOT NULL,
    Category NVARCHAR(50)
);

CREATE TABLE Warehouses (
    WarehouseID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    City NVARCHAR(50)
);

CREATE TABLE Inventory (
    InventoryID INT IDENTITY(1,1) PRIMARY KEY,
    WarehouseID INT FOREIGN KEY REFERENCES Warehouses(WarehouseID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT NOT NULL DEFAULT 0,
    MinRequired INT NOT NULL DEFAULT 10
);

 How to Run the Python Automation
1. Install the required driver package:
pip install pyodbc
2. Run the monitoring script:
python warehouse.py


