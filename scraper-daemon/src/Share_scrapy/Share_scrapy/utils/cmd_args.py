from getopt import getopt

def parse_named_command_line_args(args, options):
    argument_list = getopt(args, options)

    argument_dic = {}

    for argument_tuple in argument_list[0]:
        arg_value = argument_tuple[1]
        [key, value] = arg_value.split("=")
        argument_dic[key] = value
    
    return argument_dic
        
