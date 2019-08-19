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
            "description": "Symbolic name of the IDP Rule",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 15,
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
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": true,
        "description": "IDP Profile/Rules are used to detect intrusion attempts and/or inspect network traffic and take appropriate action.",
        "entity_name": "Idpprofile",
        "extends": [],
        "get": true,
        "package": "idsips",
        "resource_name": "idpprofiles",
        "rest_name": "idpprofile",
        "root": null,
        "template": null,
        "update": true,
        "userlabel": "IDP Profile"
    }
}