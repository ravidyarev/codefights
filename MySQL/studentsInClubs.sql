CREATE PROCEDURE studentsInClubs()
    SELECT * FROM students
    WHERE EXISTS (select 'X' from clubs 
        where students.club_id = clubs.id
    )
    ORDER BY students.id;
