-- 코드를 입력하세요
SELECT A.category AS CATEGORY, SUM(B.sales) AS TOTAL_SALES
FROM BOOK A
LEFT JOIN
BOOK_SALES B
ON A.BOOK_ID = B.BOOK_ID
WHERE  DATE_FORMAT(B.sales_date, '%Y-%m') LIKE '2022-01'
GROUP BY A.category
ORDER BY A.category