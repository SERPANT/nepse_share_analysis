import json
import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList
from decimal import Decimal
import simplejson


class AlchemyEncoder(json.JSONEncoder): 

    @staticmethod
    def convert_model_list_to_dic(listObj, ingore_field_list):
        new_list = []

        for obj in listObj:
            new_list.append(AlchemyEncoder.convert_model_obj_to_dict(obj, ingore_field_list))

        return new_list

    @staticmethod
    def convert_model_obj_to_dict(obj, ingore_field_list):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:


                if field in ingore_field_list:
                    continue

                data = obj.__getattribute__(field)

                if type(data) == InstrumentedList and  len(data) == 0:
                    fields[field] = []
                    continue

                new_data = None

                if type(data) == InstrumentedList:
                    instrument_list = []
                    for item in data:
                        instrument_list.append(AlchemyEncoder.convert_model_obj_to_dict(item, ingore_field_list))
                    
                    new_data = instrument_list
                else:
                    new_data = data

                if isinstance(new_data, datetime.date):
                    fields[field] = new_data.strftime("%Y-%m-%d %H:%M:%S")
                    continue

                if isinstance(new_data, Decimal):
                    fields[field] = simplejson.dumps(new_data, use_decimal=True)
                    continue

                try:
                    json.dumps(new_data) # this will fail on non-encodable values, like other classes
                    fields[field] = new_data
                except TypeError:
                    continue
            # a json-encodable dict
            return fields

    @staticmethod
    def parse_model_obj_to_json(obj, ingore_field_list):
        dic_obj = AlchemyEncoder.convert_model_obj_to_dict(obj, ingore_field_list)

        return json.dumps(dic_obj)

    @staticmethod
    def parse_model_list_to_json(listObj, ingore_field_list):
        new_list = AlchemyEncoder.convert_model_list_to_dic(listObj, ingore_field_list)

        return json.dumps(new_list)
    
    @staticmethod
    def parse_model_to_json(obj, ingore_field_list = []):
        # starting function
        if(type(obj) == list):
            return AlchemyEncoder.parse_model_list_to_json(obj, ingore_field_list)
        
        return AlchemyEncoder.parse_model_obj_to_json(obj, ingore_field_list)
