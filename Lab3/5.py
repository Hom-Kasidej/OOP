record_collection = {
    2548: {
        "albumTitle": 'Slippery When Wet',
        "artist": 'Bon Jovi',
        "tracks": ['Let It Rock', 'You Give Love a Bad Name']
    },
    2468: {
        "albumTitle": '1999',
        "artist": 'Prince',
        "tracks": ['1999', 'Little Red Corvette']
    },
    1245: {
        "artist": 'Robert Palmer',
        "tracks": []
    },
    5439: {
        "albumTitle": 'ABBA Gold'
    }
}

def update_records(dict_record, id, property,value):
    if property != "tracks" and value != "":
        dict_record[id][property] = value
    elif property == "tracks" and property not in dict_record[id]:
        newList = [value]
        dict_record[id][property] = newList
    elif property == "tracks" and value != "":
        dict_record[id][property].append(value)
    elif value == "" and id in dict_record and property in dict_record[id]:
        dict_record[id].pop(property)
    return dict_record

print(record_collection)

record_collection = update_records(record_collection, 5439, "artist", "")

print(record_collection)
