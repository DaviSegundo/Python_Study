import sqlite3


con = sqlite3.connect('code_organization/dealing_with_errors/application.db')
cur = con.cursor()

# Create Table
cur.execute('''CREATE TABLE blogs (id text not null primary key, date text, title text, content text, public integer)''')

# Insert few rows of data
cur.execute('INSERT INTO blogs VALUES ("first_blog", "2022-03-07", "My first blog", "Some content", 1)')
cur.execute('INSERT INTO blogs VALUES ("private_blog", "2022-05-10", "Secret blog", "This is a secret", 0)')

# Save the changes
con.commit()

# Close the connection
con.close()