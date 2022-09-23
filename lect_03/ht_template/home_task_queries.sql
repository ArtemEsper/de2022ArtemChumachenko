/*
 Завдання на SQL до лекції 02.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
SELECT
    film_category.category_id,
    category.name,
    COUNT(film_category.film_id) AS film_total
FROM film_category
JOIN category ON film_category.category_id = category.category_id
GROUP BY
    film_category.category_id,
    category.name
ORDER BY 3 DESC;



/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
SELECT
    film_actor.actor_id,
    COUNT(inventory.inventory_id) AS rented_total
FROM inventory
JOIN film_actor ON inventory.film_id = film_actor.film_id
GROUP BY film_actor.actor_id
ORDER BY 2 DESC
LIMIT 10;



/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/
SELECT
    cs.category_id,
    c."name",
    cs.su
FROM category c
JOIN
    (SELECT
         fc.category_id,
         SUM(sfp.amount) su
     FROM film_category fc
         JOIN (SELECT
                   film_id,
                   p.amount
               FROM inventory i
                   JOIN rental r ON r.inventory_id = i.inventory_id
                   JOIN payment p ON p.rental_id = r.rental_id
               ) sfp
             ON sfp.film_id = fc.film_id
     GROUP BY fc.category_id
     ORDER BY 2 DESC
     LIMIT 1
     ) cs
        ON cs.category_id = c.category_id;



/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
SELECT
    f.film_id,
    f.title
FROM film f
    LEFT JOIN inventory i ON i.film_id = f.film_id
WHERE i.film_id IS NULL;


/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
SELECT DISTINCT
    fa.actor_id,
    COUNT(fa.actor_id)
FROM film_actor fa
    JOIN film_category fc ON fc.film_id = fa.film_id
WHERE fc.category_id = 3
GROUP BY fa.actor_id
ORDER BY 2 DESC
LIMIT 6;


/*
6.
Вивести міста з кількістю активних та неактивних клієнтів
(в активних customer.active = 1).
Результат відсортувати за кількістю неактивних клієнтів за спаданням.
*/

