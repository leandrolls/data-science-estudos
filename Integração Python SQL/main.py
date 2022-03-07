import pyodbc

dados_conexao = ("Driver={SQL Server}; Server=PCLEO; Database=PythonSql;")
conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")

cursor = conexao.cursor()
comando = """CREATE TABLE Teste (
            UserId int Primary Key not null,
            FirstName varchar (50) not null,
            LastName varchar (50) not null,
            BirthDay date not null,
            Age int not null,
            LicenseMotorist bit default 0 
);

            INSERT INTO Teste (UserId,FirstName,LastName,BirthDay,Age,LicenseMotorist)
            values
            (1,'Leandro','Da Silva','1000-01-01',19,0),
            (2,'Joao','Da Silva','1000-01-01',19,0),
            (3,'Davi','Da Silva','1000-01-01',19,0),
            (4,'Pedro','Da Silva','1000-01-01',19,0);"""

cursor.execute(comando)
cursor.commit()