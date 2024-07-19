class Queries:
    CREATE_REVIEW_TABLE = """
    CREATE TABLE IF NOT EXISTS review_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    instagram_username TEXT,
    visit_date INTEGER,
    food_rating INTEGER,
    cleanliness_rating INTEGER,
    extra_comments TEXT
    )
    """

    DROP_CATEGORY_OF_DISHES_TABLE = "DROP TABLE IF EXISTS category_dishes"

    CREATE_CATEGORY_OF_DISHES_TABLE = """
    CREATE TABLE IF NOT EXISTS category_dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    UNIQUE(name))"""

    CREATE_DISHES_TABLE = """
    CREATE TABLE IF NOT EXISTS dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    price INTEGER,
    photo TEXT,
    category_of_dishes_id INTEGER,
    UNIQUE(title),
    FOREIGN KEY (category_of_dishes_id) REFERENCES category_dishes(id))"""

    INSERT_INTO_CAT = """
    INSERT OR IGNORE INTO category_dishes (name) VALUES ('drinks'), ('first'), ('second')"""

    INSERT_INTO_DISHES = """
    INSERT OR IGNORE INTO dishes (title, price, photo, category_of_dishes_id) VALUES 
    ('Плов', 320, 'AllHomework/images_2/plov.jpg', 2), 
    ('Пельмени', 220, 'AllHomework/images_2/pelmeni.jpg', 3),
    ('Мохито', 180, 'AllHomework/images_2/mohito.jpg', 1), 
    ('Манты', 350, 'AllHomework/images_2/manty.jpg', 2)  
    """




