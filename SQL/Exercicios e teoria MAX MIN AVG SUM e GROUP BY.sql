--Explica��o dos Aula MAX MIN SUM AVG
/*
MIN-M�nimo dos dados
MAX-M�ximo dos dados
SUM-Somatoria dos dados
AVG-M�dia dos dados
*/
--Explica��o dos Aula 13 GROUP BY
--O GROUP BY  basicamente divide o resultado da sua pesquisa em grupos 
/*
--Para cada grupo coc� pode aplicar uma fun��o de agrega��o , por exemplo
	-calcular a soma de itens
	-contar o n�mero de itens naquele grupo
--Sintax
	SELECT COLUNA1,FUN��ODEAGREGA��O(COLUNA 2)
	FROM NOMETABELA
	GROUP BY COLUNA1
*/
--EXEMPLO
--SELECT SpecialOfferID,SUM(UNITPRICE) FROM Sales.SalesOrderDetail GROUP BY SpecialOfferID

SELECT MiddleName,COUNT(MiddleName) AS [QUANTIDADE] FROM Person.Person GROUP BY MiddleName
