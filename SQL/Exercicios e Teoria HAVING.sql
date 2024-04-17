--Aula 14 HAVING
/*
O havnig � basicamente muito usado em jun��o com o group by para filtrar o resultados de um agrupamento.

basicamente ele � um where para dados agrupados

SELECT COLUNA1, FUNCAOAGREGACAO(COLUNA2)
FROM NOME TABELA
GROUP BY COLUNA1
HAVING CONDI��O

Uma grande diferen�a entre o HAVING E WHERE	� que o Group by � aplicado depois que os dados j� foram agrupagos, enquanto o WHERE � aplicado antes dos dados serem agrupados.

--EXEMPLO
	VAMOS DIZER QUE QUEREMOS SABER QUAIS NOMES NO SISTEMA TEM UMA OCORENCIA MAIOR QUE 10 VEZES
		
		SELECT FIRSTNAME,COUNT(FIRSTNAME) AS "QUANTIDADE"
		FROM PERSON.PERSON
		GROUP BY FIRSTNAME
		HAVING COUNT(FRISTNAME)>10

*/

SELECT StateProvinceID, COUNT(StateProvinceID)
FROM Person.Address
GROUP BY StateProvinceID
HAVING  COUNT(StateProvinceID)>1000

SELECT ProductID, AVG(LineTotal) AS [M�DIA]
FROM Sales.SalesOrderDetail 
GROUP BY ProductID
HAVING AVG(LineTotal)< 1000000

