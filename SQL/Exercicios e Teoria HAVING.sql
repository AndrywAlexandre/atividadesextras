--Aula 14 HAVING
/*
O havnig é basicamente muito usado em junção com o group by para filtrar o resultados de um agrupamento.

basicamente ele é um where para dados agrupados

SELECT COLUNA1, FUNCAOAGREGACAO(COLUNA2)
FROM NOME TABELA
GROUP BY COLUNA1
HAVING CONDIÇÃO

Uma grande diferença entre o HAVING E WHERE	é que o Group by é aplicado depois que os dados já foram agrupagos, enquanto o WHERE é aplicado antes dos dados serem agrupados.

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

SELECT ProductID, AVG(LineTotal) AS [MÉDIA]
FROM Sales.SalesOrderDetail 
GROUP BY ProductID
HAVING AVG(LineTotal)< 1000000

