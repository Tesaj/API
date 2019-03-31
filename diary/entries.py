from flask import Flask

from flask_restful import Resource ,Api

app = Flask(__name_)

api =Api(app)

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

class Entries(Resource):
    def get(self,name):
        return{'Entries':name}
api.add_resource(Entries,'/Entries/<string:name>')#https://127.0.0.1:5000/entries/some_name

#POST   
def post(self,name):
    entry ={'name':name,'entryid':1,'event':event}
    entry.append(entry)
    return entry,201 
api.add_resource(Entries,'/entry/<string:name>')


#GET /entry
def get(self,name):
    for entry in entries:
        if entry['name']==name:
            return entry
            return{'entry':None},404
api.add_resource(Entries,'/entry/<string:name>')


app.run(port=5000, debug=True)

 
