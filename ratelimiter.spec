{
    "apis": {
        "children": {}, 
        "parents": {
            "/enterprises/{id}/ratelimiters": {
                "RESTName": "enterprise", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }, 
                    {
                        "availability": null, 
                        "method": "POST"
                    }
                ], 
                "resourceName": "enterprises"
            }, 
            "/ratelimiters": {
                "RESTName": "ratelimiter", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }, 
                    {
                        "availability": null, 
                        "method": "POST"
                    }
                ], 
                "resourceName": "ratelimiters"
            }
        }, 
        "self": {
            "/ratelimiters/{id}": {
                "RESTName": "ratelimiter", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "PUT"
                    }, 
                    {
                        "availability": null, 
                        "method": "DELETE"
                    }, 
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "ratelimiters"
            }
        }
    }, 
    "model": {
        "RESTName": "ratelimiter", 
        "attributes": {
            "committedInformationRate": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Committed Information Rate :  Committed bandwidth that is allowed in Mb/s; only whole values supported.", 
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
            "description": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "A description of the Rate Limiter object", 
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
            "entityScope": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Specify if scope of entity is Data center or Enterprise level", 
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
                "type": "EntityScope", 
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
                "description": "A unique name of the Rate Limiter object", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": true, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "peakBurstSize": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bits; only whole values are supported.", 
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
            "peakInformationRate": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Peak Information Rate :  Peak bandwidth allowed in Mb/s; only whole values supported.", 
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
            }
        }, 
        "description": "Rate Limiter object that contains peak, burst and cir. Can be associated with Egress QOS policy objects.", 
        "entityName": "RateLimiter", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "package": "/policy/qos", 
        "resourceName": "ratelimiters"
    }
}