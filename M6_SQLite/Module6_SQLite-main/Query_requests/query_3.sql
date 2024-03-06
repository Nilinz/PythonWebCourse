SELECT s.group_id, sub.name AS subject_name, AVG(g.grade) AS avg_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
GROUP BY s.group_id, sub.name;
