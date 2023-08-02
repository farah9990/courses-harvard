-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 ;

SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";

SELECT bakery_security_logs.activity , bakery_security_logs.license_plate , people.name FROM bakery_security_logs , people
WHERE bakery_security_logs.license_plate = people.license_plate AND bakery_security_logs.year = 2021 AND
bakery_security_logs.month = 7 AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute >=15 AND
bakery_security_logs.minute <= 25 ;

SELECT people.name , atm_transactions.transaction_type FROM people , atm_transactions , bank_accounts WHERE bank_accounts.person_id = people.id
AND atm_transactions.account_number = bank_accounts.account_number AND atm_transactions.year = 2021 AND atm_transactions.month = 7
AND atm_transactions.day = 28 AND atm_transactions.atm_location = "Leggett Street" AND atm_transactions.transaction_type = "withdraw";
-- Bruce , Diane , Imen ,Luca

--ALTER TABLE phone_calls ADD caller_name text ;
--ALTER TABLE phone_calls ADD receiver_name text ;

UPDATE  phone_calls SET caller_name = people.name from people WHERE phone_calls.caller = people.phone_number ;
UPDATE  phone_calls SET receiver_name = people.name from people WHERE phone_calls.receiver = people.phone_number ;

SELECT caller , caller_name , receiver_name FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 ;
-- Bruce , Diane

UPDATE flights SET origin_airport_id = airports.city FROM airports WHERE flights. origin_airport_id = airports.id;
UPDATE flights SET destination_airport_id = airports.city FROM airports WHERE flights. destination_airport_id = airports.id;

SELECT id , hour , minute , origin_airport_id , destination_airport_id FROM flights WHERE year = 2021 AND month = 7 AND day = 29
ORDER BY HOUR LIMIT 1 ;
-- New York Ctiy

SELECT flights.destination_airport_id , people.name , people.phone_number ,people.license_plate FROM flights , people , passengers
WHERE people.passport_number = passengers.passport_number AND flights.id = passengers.flight_id
AND flights.id = 36 ORDER BY flights.hour ASC ;

SELECT name FROM people , flights , passengers WHERE people.passport_number = passengers.passport_number AND
flights.id = passengers.flight_id AND flights.year = 2021 AND flights.month = 7 AND flights.day = 29 AND flights.id = 36
AND name IN (SELECT phone_calls.caller_name FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60)
AND name IN (SELECT people.name FROM people , atm_transactions , bank_accounts WHERE bank_accounts.person_id = people.id
AND atm_transactions.account_number = bank_accounts.account_number AND atm_transactions.year = 2021 AND atm_transactions.month = 7
AND atm_transactions.day = 28 AND atm_transactions.atm_location = "Leggett Street" AND atm_transactions.transaction_type = "withdraw")
AND name IN (SELECT people.name FROM bakery_security_logs , people
WHERE bakery_security_logs.license_plate = people.license_plate AND bakery_security_logs.year = 2021 AND
bakery_security_logs.month = 7 AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute >=15 AND
bakery_security_logs.minute <= 25 ) ;
-- Bruce ==> Robin