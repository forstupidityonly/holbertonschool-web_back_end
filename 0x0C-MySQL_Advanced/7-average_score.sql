-- make a procedure that calculates adv score per usr

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT SUM(score) / COUNT(*)
    FROM corrections AS val
    WHERE val.user_id = user_id)
    WHERE id = User_id;
END;

DELIMITER
