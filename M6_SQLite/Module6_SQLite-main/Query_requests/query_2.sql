SELECT s.name AS student_name, AVG(g.grade) AS avg_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
WHERE g.subject_id = subject_id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;
