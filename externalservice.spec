{
    "attributes": {
        "description": {
            "description": "Description of the External Service.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "direction": {
            "allowed_choices": [
                "INGRESS"
            ],
            "description": "Direction -  INGRESS Possible values are INGRESS, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "unique name of the External Service. ",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "serviceType": {
            "allowed_choices": [
                "L2",
                "L3"
            ],
            "description": "Type of the SERVICE -  L3,L2 Possible values are L3, L2, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "stage": {
            "allowed_choices": [
                "START"
            ],
            "description": "Stage -  START,END Possible values are START, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "children": {
        "endpoint": {
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "metadatatag": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Representation of External Service",
        "entity_name": "ExternalService",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "externalservices",
        "rest_name": "externalservice",
        "update": true
    }
}