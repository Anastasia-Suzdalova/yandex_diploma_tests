# Яндекс.Самокат работа с БД и автоматизация API
## Автоматизация API
Шаги автотеста:
* Выполнить запрос на создание заказа.
* Сохранить номер трека заказа.
* Выполнить запрос на получения заказа по треку заказа.
* Проверить, что код ответа равен 200.
## Работа с БД
1. SELECT c.login, COUNT(o.id) FROM "Couriers" AS c INNER JOIN "Orders" AS o ON c.id = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;
2. SELECT track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END as status FROM "Orders";
