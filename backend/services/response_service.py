def incident_to_json(row):

    return {

        "id": row[0],

        "incident_type": row[1],

        "category": row[2],

        "description": row[3],

        "location": {

            "latitude": row[4],

            "longitude": row[5]

        },

        "severity": row[6],

        "reported_by": row[7],

        "status": row[8],

        "timestamp": row[9]

    }



def incidents_to_json(rows):

    return [

        incident_to_json(row)

        for row in rows

    ]