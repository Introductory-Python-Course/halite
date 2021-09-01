from flask import Flask, jsonify, request, send_from_directory

# Creating a Web App
app = Flask(__name__, static_url_path='', static_folder='frontend/build')

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

port = "5001"
print("running a server on port: " + port)

# Running the app
app.run(host="0.0.0.0", port=port)