
def test_header_is_valid(valid_file_against_schema):
    valid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/header.json/#/definitions/Header',
        '../messages/header/header.json'
    )
