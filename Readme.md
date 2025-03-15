# **DB Migrator** 🚀  
A universal **any-to-any** database migration tool that allows seamless transfer of tables, views, and data between different database systems using simple **command-line inputs**.  

## **Features**  
✅ Supports **PostgreSQL, MySQL, SQLite, SQL Server, and more**  
✅ Migrates **tables, views, and data**  
✅ Uses **SQLAlchemy** for cross-database compatibility  
✅ Works via **command-line inputs**  
✅ **Lightweight & Easy to Use**  

---

## **Installation**  
### **1. Clone the Repository**  
```sh
git clone https://github.com/yourusername/easymigrate.git
cd easymigrate
```

### **2. Install Dependencies**  
```sh
pip install -e .
```

---

## **Usage**  
Run the migration using the command-line tool:  
```sh
easymigrate "<source_db_url>" "<target_db_url>"
```
### **Example Commands**
#### **PostgreSQL to MySQL**
```sh
easymigrate "postgresql://user:password@localhost/old_db" "mysql://user:password@localhost/new_db"
```
#### **SQLite to PostgreSQL**
```sh
easymigrate "sqlite:///old_database.db" "postgresql://user:password@localhost/new_db"
```
#### **MySQL to SQL Server**
```sh
easymigrate "mysql://user:password@localhost/old_db" "mssql+pyodbc://user:password@server/new_db"
```

---

## **Supported Databases**  
This tool works with any database supported by **SQLAlchemy**, including:  
- **PostgreSQL**
- **MySQL**
- **SQLite**
- **SQL Server**
- **MariaDB**
- **OracleDB** (partial support)

---

## **How It Works**  
1. **Connects** to both source and target databases using SQLAlchemy.  
2. **Extracts schema** (tables, columns, views).  
3. **Creates the schema** in the target database.  
4. **Transfers data** from the source to the target database.  

---

## **Development**  
### **Run Tests**  
```sh
pytest tests/
```

### **Contribute**  
Want to improve this tool? Fork it and submit a **pull request**!  

---

## **License**  
This project is licensed under the **MIT License**.  

📌 **Author**: GAURAV N V  
📌 **GitHub**: easymigrate (https://github.com/naga251602/easymigrate)  

---

This README is **detailed, clear, and professional**—it ensures users can easily install, use, and contribute to your package. Let me know if you'd like any tweaks! 🚀