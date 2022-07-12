import psycopg2


# task 1
connection = psycopg2.connect(
    user = 'postgres',
    password = '',
    host = 'localhost',
    port = '5432',
    database = 'jobs_db'
)

cursor = connection.cursor()
query = """
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    gain INT NOT NULL,
    expiry_date DATE,
    language_skills BOOLEAN DEFAULT true,
    city VARCHAR(50) NOT NULL
);
"""
# cursor.execute(query)
# connection.commit()


# Task2 
query2 = """
    ALTER TABLE jobs DROP COLUMN city,
    ALTER TABLE jobs RENAME COLUMN gain TO salary,
    ALTER TABLE jobs ADD COLUMN company VARCHAR(50) NOT NULL DEFAULT 'ABC'
"""
# cursor.execute(query)
# connection.commit()




# task 3 

info_list = [
    # basliq, sirket, maas, bitme tarixi, xarici dil telebi
    ('iOS developer', 'A2Z Technologies', 3500, '2022-07-18', True),
    ('Tender üzrə mütəxəssis', 'A2Z Technologies', 1500, '2022-06-11', False),
    ('Məlumat bazası üzrə inzibatçı', 'ABB ASC', 1500, '2022-07-12', True),
    ('Database Administrator', 'A2Z Technologies', 2500, '2022-07-14', True),
    ('Front-End Developer', 'AzəriMed QSC', 1500, '2022-07-23', False),
    ('Proqram təminatının testləşdirilməsi üzrə mühəndis',
     'ABB ASC', 1500, '2022-08-10', False),
    ('Back-end üzrə proqramçı', 'ABB ASC', 4100, '2022-07-11', True),
    ('Biznes analitika üzrə Baş mütəxəssis ', 'ABB ASC', 2200, '2022-07-03', True),
    ('Android proqramçı', 'ABB ASC', 1300, '2022-07-22', True),
    ('Front-end üzrə proqramçı', 'ABB ASC', 3200, '2022-07-06', True),
    ('Full stack PHP proqramçı', 'AzəriMed QSC', 2400, '2022-07-17', False),
    ('Avtomatlaşdırılmış əməliyyat sistemi üzrə proqramçı',
     'ABB ASC', 2700, '2022-07-15', True),
    ('Proqram təminatı üzrə mühəndis', 'Kontakt Home', 2700, '2022-07-13', False),
    ('Hüquqşünas', 'Kontakt Home', 1500, '2022-07-03', False),
    ('Çatdırılma xidmətləri üzrə fəhlə', 'Kontakt Home', 500, '2022-07-15', True),
    ('PHP developer', 'ARIS', 1500, '2022-07-11', True),
    ('Məhsul üzrə menecer', 'Kontakt Home', 2800, '2022-07-05', True),
    ('Proqram təminatı üzrə aparıcı mühəndis',
     'Kontakt Home', 2500, '2022-07-02', False),
    ('İT sənədləşməsi üzrə mütəxəssis', 'Azericard', 1500, '2022-07-25', True),
    ('Information Security Specialist', 'DEFSCOPE LLC', 2500, '2022-07-03', False),
    ('IT Helpdesk', 'Azericard', 1500, '2022-07-30', True),
    ('Cybersecurity Business Development Internship',
     'DEFSCOPE LLC', 2900, '2022-07-19', False),
    ('Vue.js developer', 'ARIS', 1500, '2022-07-29', True),
]

query3 = """
    INSERT INTO jobs (title, company, salary, expiry_date, language_skills) VALUES(%s, %s, %s, %s, %s)
"""
for info in info_list:
    cursor.execute(query3, info_list)

# task 4 
query4 = """
SELECT * FROM jobs WHERE company='ABB ASC';
SELECT * FROM jobs WHERE company='ABB ASC' AND salary<2000;
SELECT * FROM jobs WHERE company='Kontakt Home' AND expiry_date<today;
SELECT * FROM jobs WHERE language_skills=FALSE AND salary>2500;
SELECT * FROM jobs WHERE title LIKE '.*proqramçı$';
SELECT * FROM jobs WHERE title not LIKE '.?end.?';
SELECT * FROM jobs WHERE title LIKE '^I|İT.*';
SELECT * FROM jobs WHERE language_skills=TRUE ORDER BY salary DESC;
SELECT MAX(salary) FROM jobs;
SELECT * FROM jobs WHERE expiry_date>'2022-07-12' ORDER BY DESC LIMIT 3 OFFSET 1;
SELECT * FROM jobs WHERE language_skills=FALSE AND (title LIKE '.*developer.*' OR '.*proqramçı.*');
SELECT * FROM jobs WHERE company IN ('Kontakt Home', 'AzəriMed QSC', 'A2Z Technologies') AND salary BETWEEN 2500 AND 3000;
SELECT COUNT(*) AS expired FROM jobs WHERE expiry_date<'2022-07-12';
SELECT MAX(salary) FROM jobs WHERE language_skills=FALSE;
SELECT MAX(salary) FROM jobs WHERE language_skills=FALSE;
SELECT MIN(salary) FROM jobs WHERE language_skills=TRUE;
SELECT AVG(salary) FROM jobs WHERE title LIKE '.*developer.*' OR '.*proqramçı.*';
SELECT AVG(salary) FROM jobs WHERE company IN ('Kontakt Home', 'AzəriMed QSC', 'A2Z Technologies');
"""