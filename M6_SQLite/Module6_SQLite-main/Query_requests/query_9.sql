SELECT s.name AS student_name, sub.name AS subject_name
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE g.student_id = student_id;
