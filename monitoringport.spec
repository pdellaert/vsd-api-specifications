{
    "apis": {
        "children": {}, 
        "parents": {
            "/hscs/{id}/monitoringports": {
                "RESTName": "hsc", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "hscs"
            }, 
            "/vrss/{id}/monitoringports": {
                "RESTName": "vrs", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vrss"
            }, 
            "/vscs/{id}/monitoringports": {
                "RESTName": "vsc", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vscs"
            }
        }, 
        "self": {}
    }, 
    "model": {
        "RESTName": "monitoringport", 
        "attributes": {
            "access": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Flag to indicate that it is a access port or network port.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "boolean", 
                "unique": false
            }, 
            "description": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Optional port description.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "lastStateChange": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Last port state change timestamp.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "long", 
                "unique": false
            }, 
            "name": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Name for the port.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "resiliencyState": {
                "allowedChars": null, 
                "allowedChoices": [], 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "enum", 
                "unique": false
            }, 
            "resilient": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Flag to indicate if an ACCESS port is resilient or not.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "boolean", 
                "unique": false
            }, 
            "state": {
                "allowedChars": null, 
                "allowedChoices": [
                    "DOWN", 
                    "UP", 
                    "ADMIN_DOWN"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The current state of the port. Possible values are UP, DOWN, ADMIN_DOWN, .", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "enum", 
                "unique": false
            }, 
            "uplink": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Flag to indicate that is an uplink or downlink port.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "boolean", 
                "unique": false
            }
        }, 
        "description": "Encapsulates the port information for system monitor entity.", 
        "entityName": "MonitoringPort", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "package": "/sysmon", 
        "resourceName": "monitoringports"
    }
}