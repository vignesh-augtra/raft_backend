# raft_backend

Postgre SQL from AWS RDS

Deployment using AWS App Runner

Backend Domain : https://qqeaur9dda.us-east-2.awsapprunner.com/

1. Add Items 

  EndPoint : /api/items/add (POST)
  
  Sample Request JSON : 
  {
      "title":"B",
      "imageUrl":"https://blog.hubspot.com/hubfs/image8-2.jpg" // or base64 string
  }

2. Get items

  EndPoint : /api/items/get (GET)

3. Delete item

  EndPoint : /api/items/delete/{id} (DELETE) 
  
4. UpdatePosition

  EndPoint : /api/items/updateMany (UPDATE)
  
  Sample Request JSON :
    {
    "data": [
        {
            "id": 17,
            "title": "Google",
            "imageUrl": "https://blog.hubspot.com/hubfs/image8-2.jpg",
            "position": 1
        },
        {
            "id": 18,
            "title": "ChatGPT",
            "imageUrl": "https://blog.hubspot.com/hubfs/image8-2.jpg",
            "position": 2
        }
    ]
}


