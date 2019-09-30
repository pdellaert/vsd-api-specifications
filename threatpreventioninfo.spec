{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": [
                "CONNECTED",
                "DISCONNECTED"
            ],
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Connection status between Threat Prevention Server and NSG",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "connectionStatus",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Connection Status"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": false,
        "description": "Represents information about Threat Prevention service/instance on NSG",
        "entity_name": "ThreatPreventionInfo",
        "extends": [],
        "get": true,
        "package": "threatprevent",
        "resource_name": "threatpreventioninfos",
        "rest_name": "threatpreventioninfo",
        "root": null,
        "template": null,
        "update": false,
        "userlabel": "Threat Prevention Info"
    }
}