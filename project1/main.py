import argparse
import redactor


if __name__ == "__main__":
    

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--input",type = str, required = True, help = "Input files path", nargs = "*", action = "append" )
    arg_parser.add_argument("--names", required = False, help = "Redacts names", action = "store_true")
    arg_parser.add_argument("--dates", required = False, help = "Redacts dates", action = "store_true")
    arg_parser.add_argument("--phones", required = False, help = "Redacts phone numbers", action = "store_true")
    arg_parser.add_argument("--genders", required = False, help = "Redacts genders", action = "store_true")
    arg_parser.add_argument("--address", required= False,  help = "Redacts address ", action="store_true")
    arg_parser.add_argument("--concept", type = str, required = False, help = "Redacts concept words", action = "append")
    arg_parser.add_argument("--stats", type = str, required = False, help = "Redacted File  statistics")
    arg_parser.add_argument("--output", type = str, required = True, help = "output folder")

    args = arg_parser.parse_args()
    input_data,files = redactor.input_files(args.input)

    
    if args.names:
        input_data= redactor.names(input_data)
    
    if args.dates:
        input_data = redactor.dates(input_data)
    
    if args.phones:
        input_data = redactor.phones(input_data)
        

    if args.genders:
        input_data = redactor.gender(input_data)
    
    if args.address:
        input_data= redactor.address(input_data)

    if args.concept:
        input_data,list_data = redactor.concept(input_data, args.concept)
        
    if args.output:
        redactor.output( files,input_data, args.output)

    if args.stats:
        
        redactor.stats(list_data,files,args.stats)




