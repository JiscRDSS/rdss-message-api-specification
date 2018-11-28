
def test_metadata_create_header_is_valid(valid_file_against_schema):
    valid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/header.json/#/definitions/Header',
        '../messages/header/metadata_create_header.json'
    )

def test_metadata_create_error_header_is_valid(valid_file_against_schema):
    valid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/header.json/#/definitions/Header',
        '../messages/header/metadata_create_error_header.json'
    )

def test_preservation_event_header_is_valid(valid_file_against_schema):
    valid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/header.json/#/definitions/Header',
        '../messages/header/preservation_event_header.json'
    )
