--Explicação dos Aula MAX MIN SUM AVG
/*
MIN-Mínimo dos dados
MAX-Máximo dos dados
SUM-Somatoria dos dados
AVG-Média dos dados
*/
--Explicação dos Aula 13 GROUP BY
--O GROUP BY  basicamente divide o resultado da sua pesquisa em grupos 
/*
--Para cada grupo cocê pode aplicar uma função de agregação , por exemplo
	-calcular a soma de itens
	-contar o número de itens naquele grupo
--Sintax
	SELECT COLUNA1,FUNÇÃODEAGREGAÇÃO(COLUNA 2)
	FROM NOMETABELA
	GROUP BY COLUNA1
*/
--EXEMPLO
--SELECT SpecialOfferID,SUM(UNITPRICE) FROM Sales.SalesOrderDetail GROUP BY SpecialOfferID

SELECT MiddleName,COUNT(MiddleName) AS [QUANTIDADE] FROM Person.Person GROUP BY MiddleName
