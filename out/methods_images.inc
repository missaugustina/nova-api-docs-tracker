Verify method list for images.inc

Source Code: ../tests/test_files/images.inc

1. Do all methods for the resource currently exist?

Methods currently documented:
GET //v2.1/{tenant_id}/images/{image_id} (Show Image Details)
PUT //v2.1/{tenant_id}/images/{image_id}/metadata/{key} (Create Or Update Image Metadata Item)
DELETE //v2.1/{tenant_id}/images/{image_id}/metadata/{key} (Delete Image Metadata Item)
GET //v2.1/{tenant_id}/images/{image_id}/metadata/{key} (Show Image Metadata Item Details)
DELETE //v2.1/{tenant_id}/images/{image_id} (Delete Image)


2. Rearrange methods in the following order (sorted by url):
GET
POST
PUT
DELETE

For example, servers.inc would be:
GET /servers
POST /servers
GET /servers/details
GET /servers/{id}
PUT /servers/{id}
DELETE /servers/{id}
