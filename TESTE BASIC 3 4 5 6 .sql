--3/4
SELECT DISTINCT(City)
FROM Person.Address

--5
SELECT *
FROM Production.Product
WHERE Color = 'Red' AND ListPrice BETWEEN 500 AND 1000

--6
SELECT *
FROM Production.Product
WHERE Name LIKE '%ROAD%'