# VSD API Specifications

## Introduction

This repository contains formalized specifications for VSD APIs.


## Structure

A specification file contains the following information


### APIs

This section of the specification describes how to interact with the object through ReST calls. It is a dictionary where the key the API path. It also contains additional informations:

 - `RESTName`: the ReST name of the api object. It can be the parent, the child or itself (see below)
 - `resourceName`: the resource name of the API object. It is usually the plural version of the `RESTName`
 - `operations`: an array of available ReST operations (`method`), and to what role it is available (`availability`)

#### Self
Describes how to directly access the specified object.

#### Parents
Describes how to access the specified object from its parents

#### Children
Describes how to access the children of the specified object


### Model

The model is a dictionary that describes the specified object itself. It contains the following keys:

#### General information
 - `RESTName`: the ReST name of the specified object
 - `resourceName`: the resource name of the specified object. It is usually the plural version of the `RESTName`
 - `description`: the description of the specified object
 - `package`: the package of the objects (this is mostly used for API documentation ordering)
 - `entityName`: the name of the entity. This is usually used to create `vsdk` class with correct capitalization
 - `attributes`: The list and description of all attributes of the specified object. (see below)

#### Attributes
This is an dictionary of all available attributes of the specified object where the key is the attribute, and the content is a dictionary containing characteristics of this attributes. The characteristics must all be set. Usually, when a characteristic is not applicable, its value must be set to null.


 - `allowedChars`: regexp defining what chars can be set for the property (only available when type is `string`, otherwise `null`)
 - `allowedChoices`: array containing all the possible values of the attribute (only avalailble when type is `enum`, otherwise `null`)
 - `autogenerated`: boolean telling if this field is autogenerated by the server
 - `availability`: array defining what roles can see this attribute. (`null` means all)
 - `creationOnly`: boolean telling if the attribute can only be set during creation (semi-readonly)
 - `defaultOrder`: boolean telling if this attribute is the default order key
 - `defaultValue`: default value set by the server if the attribute is sent as `null`
 - `description`: description of the attribute (used for API documentation)
 - `filterable`: boolean telling if this property can be filtered using `X-NuageFilter`
 - `format`: format of the attribute (see below)
 - `maxLength`: maximum length of the attribute (only available when type is `string`, otherwise `null`)
 - `maxValue`: minimum length of the attribute (only available when type is `string`, otherwise `null`)
 - `minLength`: maximum value of the attribute (only available when type is `int` or `float`, otherwise `null`)
 - `minValue`: minimum value of the attribute (only available when type is `int` or `float`, otherwise `null`)
 - `orderable`: boolean telling if client can order results based this attribute
 - `readOnly`: boolean telling if this attribute is not modifiable
 - `required`: boolean telling if this attribute is required
 - `type`: type of the attribute (see below)
 - `unique`: boolean telling if the value of this attribute has to be unique in its context


#### Types

The `type` characteristic of an attribute can be one on the following:

- `string`
- `int`
- `float`
- `enum`
- `list`
- `object`
- `boolean`


#### Formats

The `format` characteristic of an attribute can be one on the following:

- `null`
- `email`
- `phone`
- `ip`
- `cidr`
- `range`
- `mac`
- `rtrd`