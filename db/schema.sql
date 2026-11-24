CREATE TABLE equipment (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    equipment_id INT REFERENCES equipment(id),
    student_name VARCHAR(100) NOT NULL,
    slot_date DATE NOT NULL,
    slot_time VARCHAR(20) NOT NULL,
    UNIQUE (equipment_id, slot_date, slot_time)
);

INSERT INTO equipment (name) VALUES
 ('Oscilloscope'), ('3D Printer'), ('Lab Bench 1'), ('Lab Bench 2');
