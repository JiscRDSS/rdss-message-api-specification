from ..test_helpers import valid_file_against_schema


def test_metadata_delete_request_is_valid():
    valid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/delete_request.json/#/definitions/MetadataDeleteRequest',
        '../messages/body/metadata/delete/research_object_delete_request.json'
    )
