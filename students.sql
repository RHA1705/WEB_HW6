-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student VARCHAR(255) UNIQUE NOT NULL
);

-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: lecturers
DROP TABLE IF EXISTS lecturers;
CREATE TABLE lecturers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lecturer VARCHAR(255) UNIQUE NOT NULL
);

-- Table: lectures
DROP TABLE IF EXISTS lectures;
CREATE TABLE lectures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lecture VARCHAR(255) UNIQUE NOT NULL,
    lecturer_id INTEGER,
    FOREIGN KEY (lecturer_id) REFERENCES lecturers (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    grade INTEGER,
    date_of DATE NOT NULL,
    lecture_id INTEGER,
    student_id INTEGER,
    FOREIGN KEY (lecture_id) REFERENCES lectures (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
