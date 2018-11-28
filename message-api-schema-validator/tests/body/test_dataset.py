from ..test_helpers import valid_file_against_schema, invalid_file_against_schema


def test_dataset_is_valid():
    valid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/dataset.json/#/definitions/Dataset',
        '../messages/body/metadata/create/dataset_create_request.json'
    )


def test_article_is_not_a_valid_dataset():
    invalid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/dataset.json/#/definitions/Dataset',
        '../messages/body/metadata/create/article_create_request.json'
    )


def test_thesis_dissertation_is_not_a_valid_dataset():
    invalid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/dataset.json/#/definitions/Dataset',
        '../messages/body/metadata/create/thesis_dissertation_create_request.json'
    )


def test_research_object_is_not_a_valid_dataset():
    invalid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/dataset.json/#/definitions/Dataset',
        '../messages/body/metadata/create/research_object_create_request.json'
    )


def test_information_package_object_is_not_a_valid_dataset():
    invalid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/dataset.json/#/definitions/Dataset',
        '../messages/body/preservation/preservation_event_request.json'
    )
