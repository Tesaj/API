from flask import Flask,jsonify,request
app = Flask(__name__)


Entries =[  
    {
'name'='meetings', 
[
{'entryid'=1
 'event' = 'Meeting with managers'

}
]
 'name'='appreciation',
 [
{'entryid'=2
 'event' = 'Staff appreication week'
}
]
'name'='party',
[
{'entryid'=3
 'event'='end of year staff party'
}
]

]

#GET /entries
@app.route('/https://127.0.0.1:5000/api/v1/entries',method['GET'])
def get_entries():
    return jsonify({'entries':entries})

#POST /entries/entry_name
@app.route('/entries/<'string:name'>,method=['POST'])
def create_entry():
    request_data = request.get_json()
    new_entry =
    {
        'name' :request_data['name']
        'entryid':[]
        'event':[]
       
    }
    entry.append(new_entry)
    return jsonify(new_entry)


#GET /entries/<'string:name'>
@app.route('/entry'<'string:name'>,method['GET'])
def get_entryname():
    for entryname in entries:
        if entryname['name']==name:
            return jsonify(entryname)
            return jsonify({'message':'entryname is not found'})


#GET /entries/entryid
@app.route('/entryid',method['GET'])
def get_entryid(name):
    for entry in entries:
        if entry['name']==name:
            return({'entryid':entry['entryid']})
            return({'message':'entryid is not found'})

#POST /entries/event
@app.route('/event',method=['POST'])
def get_an_event_in_entry(name):
    request_data = request.get_json()
    for entry in entries:
        if entry['name']==name:
            new_event=
            {
                'name':request_data['name'],
                'event':[]
            }
            entry['event'].append(new_event)
            return jsonify(new_event)

app.run(port=5000)






 