import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList


class AlchemyEncoder(json.JSONEncoder): 

    @staticmethod
    def convert_model_list_to_dic(listObj):
        new_list = []

        for obj in listObj:
            new_list.append(AlchemyEncoder.convert_model_obj_to_dict(obj))

        return new_list

    @staticmethod
    def convert_model_obj_to_dict(obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)

                if type(data) == InstrumentedList and  len(data) == 0:
                    fields[field] = []
                    continue

                new_data = None

                if type(data) == InstrumentedList:
                    instrument_list = []
                    for item in data:
                        instrument_list.append(AlchemyEncoder.convert_model_obj_to_dict(item))
                    
                    new_data = instrument_list
                else:
                    new_data = data

                try:
                    json.dumps(new_data) # this will fail on non-encodable values, like other classes
                    fields[field] = new_data
                except TypeError:
                    continue
            # a json-encodable dict
            return fields

    @staticmethod
    def parse_model_obj_to_json(obj):
        dic_obj = AlchemyEncoder.convert_model_obj_to_dict(obj)

        return json.dumps(dic_obj)

    @staticmethod
    def parse_model_list_to_json(listObj):
        new_list = AlchemyEncoder.convert_model_list_to_dic(listObj)

        return json.dumps(new_list)
    
    @staticmethod
    def parse_model_to_json(obj):
        # starting function
        if(type(obj) == list):
            return AlchemyEncoder.parse_model_list_to_json(obj)
        
        return AlchemyEncoder.parse_model_obj_to_json(obj)
