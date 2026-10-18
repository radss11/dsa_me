SELECT p.product_id,
       COALESCE(
           ROUND(SUM(p.price * e.units) / SUM(e.units), 2),
           0
       ) AS average_price
FROM Prices p
LEFT JOIN UnitsSold e
    ON p.product_id = e.product_id
   AND e.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;