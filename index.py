index_view = """
<!DOCTYPE html>
<html>
   <head>
      <title>GCP App Engine + MongoDB Atlas Demo App</title>
   </head>
   <body style="background-color:white;">
        <h1 style="color: #000000; margin: 15px;">GCP App Engine + MongoDB Atlas Example App</h1>
        <div style="background-color: #589636; margin: 15px; border-radius: 5px; padding: 15px; width: 400px">
        <form action="/insert-doc" method="post">
            <p><input type=text name=email placeholder="Insert document ... Example: {x:1}">
            <p><input type=submit value="Upload document to MongoDB">   
        </form>
        <form action="/list-docs" method="get">
            <p><input type=submit value="List documents in MongoDB">   
        </form>
        </div>
    </body>
</html>
"""