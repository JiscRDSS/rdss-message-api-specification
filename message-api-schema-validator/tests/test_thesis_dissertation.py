
def test_thesis_dissertation_is_valid(valid_against_schema): 
    valid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation",
            "../messages/body/metadata/create/thesis_dissertation_create_request.json"
            )


def test_article_is_not_a_valid_thesis_dissertation(invalid_against_schema):
    invalid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation",
            "../messages/body/metadata/create/article_create_request.json"
            )

def test_research_object_is_not_a_valid_thesis_dissertation(invalid_against_schema):
    invalid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation",
            "../messages/body/metadata/create/research_object_create_request.json"
            )

def test_dataset_is_not_a_valid_thesis_dissertation(invalid_against_schema):
    invalid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation",
            "../messages/body/metadata/create/dataset_create_request.json"
            )

