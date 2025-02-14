from flask import Flask,jsonify, render_template
import json

app = Flask(__name__)

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load the data once at the start and store it in a global variable
data = load_json_data('data/data.json')
  
# Set parent key to "" if it's None
for node in data:
    if node["parent"] is None:
        node["parent"] = ""  
      
# Flask app
def get_children_count(parent_id):
    return len([node for node in data if node["parent"] == parent_id])
  
# fetch children of a parent node
@app.route('/api/get-children/<int:parent_id>', methods=['GET'])
def get_children(parent_id):
    children = [node for node in data if node["parent"] == parent_id]
 
    # Add childCount to parent node
    for child in children:
        child["childCount"] = get_children_count(child["key"])
        
    return jsonify(children)
        
# fetch top-level nodes
@app.route('/api/get-top-level', methods=['GET'])
def get_top_level():
    top_level_nodes = [node for node in data if node["parent"] == ""]
    
    # Add childCount to top-level nodes
    for node in top_level_nodes:
        node["childCount"] = get_children_count(node["key"])

    return jsonify(top_level_nodes)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
