SELECT DISTINCT sub.name AS subject_name, t.name AS teacher_name
FROM subjects AS sub
JOIN teachers AS t ON sub.teacher_id = t.id;
