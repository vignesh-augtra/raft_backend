from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import db_handler

# CORS - Enabling All Domain
middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods =["*"])
]


app = Starlette(debug = False, middleware=middleware)

# Sample Ping API to Check for the latest deployed version 
@app.route("/ping", methods=['GET'])
def ping(request):
    db_handler.rr()
    return JSONResponse({'version': "1.0"})


# API to get All items
@app.route("/api/items/get", methods=['GET'])
async def getItems(request):
   try:
        return JSONResponse({
            'isError' : False,
            'data': db_handler.getItems()
        })
   except Exception as error:
       return JSONResponse({
            'isError' : True,
            'data': str(error)
        })
   

# API to add an item   
@app.route("/api/items/add", methods = ['POST'])
async def addItems(request):
    try:

        # Getting request data
        requestData = await request.json()

        # Executing add to Table logic
        db_handler.addItem(requestData)

        # After Adding, returning the new set of items
        return await getItems(request)
    
    except Exception as error:
       return JSONResponse({
            'isError' : True,
            'data': str(error)
        })
    
@app.route("/api/items/delete/{id}", methods = ['DELETE'])
async def deleteItem(request):
    try:
        # deleting the specified id
        db_handler.deleteItem(request.path_params['id'])

        # returning the new list of items after deletion
        return await getItems(request)
    
    except Exception as error:
       return JSONResponse({
            'isError' : True,
            'data': str(error)
        })
    

# API to update multiple items at once using its ID    
@app.route("/api/items/updateMany", methods = ['PUT'])
async def updateMany(request):
    try:
         # Getting request data
        requestData = await request.json()

        # Executing add to Table logic
        db_handler.updateItems(requestData['data'])

        # After Updating, returning the new set of items
        return await getItems(request)
    
    except Exception as error:
       return JSONResponse({
            'isError' : True,
            'data': str(error)
        })
    
