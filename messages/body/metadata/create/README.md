# Metadata Create

Message Type: `MetadataCreate`.
Message Class: `Command`.

Describes a JSON payload of metadata of a [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj), [Article](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Article-content-model.mdj), [Dataset](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Dataset-content-model.mdj) or [Thesis](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Thesis-content-model.mdj) that is generated during a `CREATE` operation.

## Scenarios

- Sent to subscribers to notify that metadata for a [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj), [Article](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Article-content-model.mdj), [Dataset](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Dataset-content-model.mdj) or [Thesis](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Thesis-content-model.mdj) has been created.

## Request

- Research Object example: [`research_object_create_request.json`](research_object_create_request.json)
- Article example: [`article_create_request.json`](article_create_request.json)
- Dataset example: [`dataset_create_request.json`](dataset_create_request.json)
- Thesis example: [`thesis_dissertation_create_request.json`](thesis_dissertation_create_request.json)
- Schema: [`schemas/message/metadata/create_request.json`](../../../../schemas/message/metadata/create_request.json)

## Response

N/A.
