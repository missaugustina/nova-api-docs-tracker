Verify method list for flavors.inc

Source Code: ../tests/test_files/flavors.inc

1. Do all methods for the resource currently exist?

Methods currently documented:
DELETE /v2.1/{tenant_id}/flavors/{flavor_id} (Delete Flavor)
GET /v2.1/{tenant_id}/flavors (List Flavors)
GET /v2.1/{tenant_id}/flavors/{flavor_id} (Show Flavor Details)
POST /v2.1/{tenant_id}/flavors (Create Flavor)
GET /v2.1/{tenant_id}/flavors/detail (List Flavors With Details)


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
