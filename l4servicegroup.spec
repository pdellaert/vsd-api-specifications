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
            "description": "Describes the Service Group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 256,
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
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Name of the Service group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 256,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "name",
            "orderable": false,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": true,
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
            "rest_name": "l4service",
            "update": true
        }
    ],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": true,
        "description": "Service Group is a set of Services that can be used in ACLs.",
        "entity_name": "L4ServiceGroup",
        "extends": [
            "@audited",
            "@base"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "l4servicegroups",
        "rest_name": "l4servicegroup",
        "root": null,
        "template": false,
        "update": true,
        "userlabel": "Service Group"
    }
}