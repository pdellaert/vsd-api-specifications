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
            "description": "Identification of the Performance Monitoring Probe that is associated with this instance of a UBR Group.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedPerformanceMonitorID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Performance Monitor"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Description of the UBR Group.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "description",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Description"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Unique Identifier for DUC Group, autogenerated by VSD.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 5120,
            "min_length": null,
            "min_value": 4096,
            "name": "ducMeshGroupID",
            "orderable": true,
            "read_only": true,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": true,
            "uniqueScope": null,
            "userlabel": "Duc Mesh Group ID"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "GATEWAY",
                "HUB",
                "UBR"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "UBR",
            "deprecated": false,
            "description": "The function of the group",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "function",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Function Type"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Name given to the UBR Group.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Name"
        }
    ],
    "children": [
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "member",
            "rest_name": "nsgateway",
            "update": true
        }
    ],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": true,
        "description": "A logical group of 1 or more NSGs of personality NSG-UBR, that are used to provide connectivity between NSGs in disjoint underlays.",
        "entity_name": "DUCGroup",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": null,
        "resource_name": "ducgroups",
        "rest_name": "ducgroup",
        "root": null,
        "template": false,
        "update": true,
        "userlabel": "UBR Group"
    }
}