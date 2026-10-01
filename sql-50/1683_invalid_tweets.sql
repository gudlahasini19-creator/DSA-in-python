-- LeetCode 1683: Invalid Tweets
-- A tweet is invalid if the number of characters in content is strictly greater than 15.

SELECT tweet_id 
FROM Tweets 
WHERE LENGTH(content) > 15;
