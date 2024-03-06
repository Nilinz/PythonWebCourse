SELECT t.name AS teacher_name, s.name AS student_name, AVG(g.grade) AS avg_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
JOIN teachers AS t ON sub.teacher_id = t.id
WHERE t.id = teacher_id
GROUP BY t.name, s.name