# Metadata Delete

Message Type: `MetadataDelete`.
Message Class: `Command`.

Describes a JSON payload of metadata of a [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj), [Article](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Article-content-model.mdj), [Dataset](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Dataset-content-model.mdj) or [Thesis](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Thesis-content-model.mdj) that is generated during a `CREATE` operation.

## Scenarios

- Sent to subscribers to notify that metadata for a [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj), [Article](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Article-content-model.mdj), [Dataset](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Dataset-content-model.mdj) or [Thesis](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Thesis-content-model.mdj) has been deleted.

## Request

- Research Object example: [`research_object_delete_request.json`](research_object_create_request.json)
- Schema: [`schemas/message/metadata/delete_request.json`](../../../../schemas/message/metadata/delete_request.json)

(n.b. As the payload for these messages consists of the `objectUUID` of the object being deleted, an example is provided only for `ResearchObject`.)

## Response

N/A.
