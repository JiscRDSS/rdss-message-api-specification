
def test_header_is_valid(valid_against_schema):
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/header.json/#/definitions/header',
        '../messages/header/header.json'
    )
