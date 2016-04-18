Verify method list for servers.inc

Source Code: ../tests/test_files/servers.inc

1. Do all methods for the resource currently exist?

Methods currently documented:
POST /v2.1/{tenant_id}/servers (Create Server)
GET /v2.1/{tenant_id}/servers/{server_id} (Show Server Details)
GET /v2.1/{tenant_id}/servers (List Servers)
PUT /v2.1/{tenant_id}/servers/{server_id} (Update Server)
DELETE /v2.1/{tenant_id}/servers/{server_id} (Delete Server)


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
