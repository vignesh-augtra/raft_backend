from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import psycopg2
from starlette.config import Config

config = Config('.env')

conn = psycopg2.connect(
    database=config('DATABASE_NAME'),
    user=config('DATABASE_USER_NAME'),
    password=config('DATABASE_PASSWORD'),
    host=config('DATABASE_HOST'),
    port=config('DATABASE_POST'),
)

app = Starlette(debug = config("DEBUG"))
@app.route("/api/items/get", methods=['GET'])
async def get_items(request):
    curr = conn.cursor()
    # curr.execute(
    #     "create table if not exists items (id serial primary key, title text not null unique, imageUrl text not null, position int not null unique )")

    insertQuery = """insert into items 
    (title, imageUrl, position ) 
    values 
    ('Google', 'https://blog.hubspot.com/hubfs/image8-2.jpg', 1),
    ('Amazon', 'https://1000logos.net/wp-content/uploads/2016/10/Amazon-logo-meaning.jpg', 2),
    ('IBM', 'https://www.ibm.com/brand/experience-guides/developer/8f4e3cc2b5d52354a6d43c8edba1e3c9/02_8-bar-reverse.svg', 3),
    ('ChatGPT', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/2048px-ChatGPT_logo.svg.png', 4),
    ('Microsoft', 'https://png.pngitem.com/pimgs/s/26-260683_microsoft-company-logo-hd-png-download.png', 5)
    """

    fetchQuery = 'select * from items'
    curr.execute(fetchQuery)
    data = curr.fetchall()
    return JSONResponse({'data': data})
