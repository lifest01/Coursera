use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select name from store where is_automated = 1

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
SELECT store_id FROM store WHERE store_id IN (SELECT store_id FROM sale)


-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
SELECT store_id FROM store WHERE store_id not IN (SELECT store_id FROM sale)

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select name, avg(total / quantity)as average from sale natural left join product group by name order by average

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select name from product natural join sale group by product_id having count(distinct store_id) = 1

-- 8. Получить названия всех складов, с которых продавался только один продукт
select name from store natural left join sale group by store_id having count(distinct product_id) = 1 

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale where total = (select max(total) from sale)

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from (select sum(total) as total_sum, date from sale group by date order by total_sum desc limit 1) as final
