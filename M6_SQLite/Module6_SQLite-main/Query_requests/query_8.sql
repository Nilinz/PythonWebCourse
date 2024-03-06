SELECT t.name AS teacher_name, sub.name AS subject_name, AVG(g.grade) AS avg_grade
FROM subjects AS sub
JOIN teachers AS t ON sub.teacher_id = t.id
JOIN grades AS g ON sub.id = g.subject_id
WHERE t.id = teacher_id
GROUP BY t.name, sub.name;
