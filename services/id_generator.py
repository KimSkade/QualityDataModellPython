import sqlite3

def create_table():
    conn = sqlite3.connect("id_database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS id_counter (counter INTEGER)")
    conn.commit()
    conn.close()

def get_counter_value():
    conn = sqlite3.connect("id_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT counter FROM id_counter")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0

def set_counter_value(value):
    conn = sqlite3.connect("id_database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE id_counter SET counter = ?", (value,))
    conn.commit()
    conn.close()

def generate_unique_id():
    create_table()
    counter_value = get_counter_value()
    counter_value += 1
    set_counter_value(counter_value)
    return counter_value