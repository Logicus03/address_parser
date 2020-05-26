from postal.parser import parse_address
from postal.expand import expand_address

def parse_json(address):
    return {k: v for (v, k) in address}

def address_parser(address):

    # parsed = parse_address( expand_address( address )[0] )
    parsed = parse_json(parse_address( expand_address( address )[0] ))
    
    return  parsed