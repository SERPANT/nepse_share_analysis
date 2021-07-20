class DuplicatePipeLine: 
    
    def __init__(self):
        self.time_seen = set()
    
    def process_item(self, item, spider):
        new_time_list = []

        for timeVal in item['time_list']:

            minute_value = int(timeVal['time'].strftime("%M"))
            nearest_multiple_of_five = (5 * round(minute_value/5)) % 60

            t_value = timeVal['time'].replace(minute=nearest_multiple_of_five)
            date_text= t_value.strftime("%m/%d/%Y, %H:%M:%S")

            if date_text in self.time_seen:
                continue
            else:
                self.time_seen.add(date_text)
                new_time_list.append({"time": t_value, "value": timeVal["value"]})

        item['time_list'] = new_time_list

        self.time_seen.clear()
        return item
        