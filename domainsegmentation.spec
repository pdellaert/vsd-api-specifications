{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Associated domain identifier ",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "domainID",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Domain ID"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The VLAN Number (1-4095).",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 4095,
            "min_length": null,
            "min_value": 1,
            "name": "segmentationID",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Segmentation ID"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "VLAN"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": false,
            "default_value": "VLAN",
            "deprecated": false,
            "description": "The type of segmentation that is used.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "segmentationType",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Segmentation Type"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "This represents domain segment identifier which is unique for domain per NSGateway.",
        "entity_name": "DomainSegmentation",
        "extends": [],
        "get": true,
        "package": "vnf",
        "resource_name": "domainsegmentations",
        "rest_name": "domainsegmentation",
        "root": null,
        "update": false
    }
}