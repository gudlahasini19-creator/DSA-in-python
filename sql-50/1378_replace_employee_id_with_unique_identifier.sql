-- LeetCode 1378: Replace Employee ID With The Unique Identifier
-- Show unique_id and name for each user; if no unique ID, show null (LEFT JOIN).

SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;
