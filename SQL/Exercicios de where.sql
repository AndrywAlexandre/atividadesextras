
SELECT * FROM Production.Product
WHERE Weight>500 AND Weight<700
-- RETORNO 4 LINHAS DE RESULTADO
/*
SELECT * FROM HumanResources.Employee
WHERE MaritalStatus = 'S' and SalariedFlag = 1
-- 24 Rows result

SELECT Person.EmailAddress.EmailAddress
FROM Person.Person
INNER JOIN Person.EmailAddress ON Person.Person.BusinessEntityID = Person.EmailAddress.BusinessEntityID
WHERE FirstName = 'Peter' and LastName='Krebs' 
-- 1 ROWS RESULT 
*/