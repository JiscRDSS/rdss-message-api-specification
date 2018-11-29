# Metadata Read

Message Type: `MetadataRead`.
Message Class: `Command`.

Describes a JSON payload of metadata of a [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj), [Article](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Article-content-model.mdj), [Dataset](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Dataset-content-model.mdj) or [Thesis](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Thesis-content-model.mdj) that is generated during a `READ` operation.

## Scenarios

- Sent by subscribers when the metadata for an existing [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj), [Article](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Article-content-model.mdj), [Dataset](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Dataset-content-model.mdj) or [Thesis](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Thesis-content-model.mdj) is required.

## Request

- Research Object example: [`research_object_read_request.json`](research_object_read_request.json)
- Schema: [`schemas/message/metadata/read_request.json`](../../../../schemas/message/metadata/read_request.json)

(n.b. As the payload for these messages consists of the `objectUUID` of the object being requested, an example is provided only for `ResearchObject`.)

## Response

- Research Object example: [`research_object_read_response.json`](research_object_read_response.json)
- Schema: [`schemas/message/metadata/read_response.json`](../../../../schemas/message/metadata/read_response.json)

(n.b. Payloads for these messages are identical in form to those for `MetadataCreate` messages, so only a `ResearchObject` payload is provided as an example.)
