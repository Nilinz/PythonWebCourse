SELECT s.name AS student_name, sub.name AS subject_name, g.grade, g.date_received
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE s.group_id = group_id AND g.subject_id = subject_id;
ORDER BY g.date_received DESC
LIMIT 1;