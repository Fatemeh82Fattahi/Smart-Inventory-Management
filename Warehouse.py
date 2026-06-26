import pyodbc
connection_config = (
    "Driver={SQL Server};"
    "Server=DESKTOP-TJB4IUA;"
    "Database=SmartInventoryDB;"
    "Trusted_Connection=yes;"
)

try:
    connection = pyodbc.connect(connection_config)
    cursor = connection.cursor()

    select_query = """
        SELECT w.Name, p.Name 
        FROM Inventory i 
        JOIN Warehouses w ON i.WarehouseID = w.WarehouseID 
        JOIN Products p ON i.ProductID = p.ProductID 
        WHERE i.Quantity < i.MinRequired;
    """

    cursor.execute(select_query)
    low_stock_items = cursor.fetchall()

    print("\n--- Digikala Low Stock Report ---")

    for row in low_stock_items:
        warehouse_name = row[0]
        product_name = row[1]
        print(
            f"Warehouse: {warehouse_name} | Product: {product_name} -> [ALERT: Low Stock]")
except Exception as error:
    print("Error connecting to database:", error)
