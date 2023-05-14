import psycopg2

# connection to PostgreSQL
conn = psycopg2.connect(
    database="raft",
    user="vignesh",
    password="vignesh123",
    host="database-1.cywknhvmc2k3.us-east-2.rds.amazonaws.com", # Postgre RDS instance in AWS
    port=5432,
)

# fetching All items
def getItems():
    try:
        curr = conn.cursor()
        fetchQuery = 'select * from carditems order by position'
        curr.execute(fetchQuery)
        rawListOfItems = curr.fetchall()
        listOfDicts = []

        # Converting the raw data to Dict to easily in front end
        for item in rawListOfItems :
            listOfDicts.append({
                "id":item[0],
                "title":item[1],
                "imageUrl":item[2],
                "position":item[3],
            })
        curr.close()
        return listOfDicts
    except Exception as e:
        curr.execute('rollback')
        conn.commit()
        curr.close()
        raise(e)

# Adding new item
def addItem(item):
    try:
        curr = conn.cursor()

        # Get the max position to add an item to next position
        curr.execute("select max(position) from carditems")
        maxPosition = curr.fetchall()
        maxPosition = (maxPosition[0][0] or 0) + 1 # if No data found, start from 1 or maxPos + 1

        # frame insert query and execute
        insertQuery = f"""insert into carditems 
                        (title, imageUrl, position ) 
                        values 
                        ('{item['title']}', {repr(item['imageUrl'])}, {maxPosition})"""
        curr.execute(insertQuery)
        conn.commit()
        curr.close()
    except Exception as e:
        curr.execute('rollback')
        conn.commit()
        curr.close()
        raise(e)


# Deleting An item
def deleteItem(id):
    try:
        curr = conn.cursor()
        curr.execute("delete from carditems where id = {}".format(id))
        conn.commit()
        curr.close()
    except Exception as e:
        curr.execute('rollback')
        conn.commit()
        curr.close()
        raise(e)

# updating multiple items at once
def updateItems(items):
    try:
        curr = conn.cursor()

        for item in items:
            curr.execute(f"update carditems set title = '{item['title']}', imageUrl = {repr(item['imageUrl'])}, position = {item['position']} where id = {item['id']}")
        conn.commit()
        curr.close()
    except Exception as e:
        curr.execute('rollback')
        conn.commit()
        curr.close()
        raise(e)
    
