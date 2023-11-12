# Eindproject-API

**Gemaakt door:** Mehmet Demirtas  
**Studentnummer:** r0939369

## Over het thema

Dit is mijn API project over snacks en soda. Ik sla al de gegevens ook op in mijn database met sqlite.

#### POST requests

- **Post-request snack**: Hier kan je de naam en extra informatie van de snack geven (automatisch ID toegevoegd).
- **Post-request soda**: Hier kan je de naam en de smaak van de soda geven (automatisch ID toegevoegd).

#### GET requests

- **Get-request snack**: hier kan je de id van de snack geven en krijg je de informatie van dat snack binnen.
- **Get-request all snack**: Hier kan je de van/tot id ingeven dat je wil zien over de snack's.
- **Get-request soda**: hier kan je de id van de soda geven en krijg je de informatie van dat soda binnen.
- **Get-request team/soda**: Hier kan je de van/tot id ingeven dat je wil zien over de soda's.

#### DELETE requests

- **Delete-request snack/soda**: Hier kan je de snack/soda verwijderen door de ID te geven.

### Overview API

- [API-documentatie](img/docs.png)

### Postman Screenshots

- Post-request: add snack ![addsnack](img/post_snack.png)
- Post-request: add sodas ![addsodas](img/post_sodas.png)
- Get-request: all snack ![allsnack](img/get_snack.png)
- Get-request: all soda ![allsodas](img/get_sodas.png)
- Get-request: id snack ![idsnack](img/get_snack_id.png)
- Get-request: id soda ![idsoda](img/get_sodas_id.png)
- Delete-request: remove snack id ![removesnackid](img/delete_snack_id.png)
- Delete-request: remove soda id ![removesodaid](img/delete_sodas_id.png)

### OPENAPI Screenshots

- Post-request: add snack ![addsnack](img/api_post_snack.png)
- Post-request: add sodas ![addsodas](img/api_post_sodas.png)
- Get-request: all snack ![allsnack](img/api_get_snacks.png)
- Get-request: all soda ![allsodas](img/api_get_sodas.png)
- Get-request: id snack ![idsnack](img/api_get_snacks_id.png)
- Get-request: id soda ![idsoda](img/api_get_sodas_id.png)
- Delete-request: remove snack id (it shows error but it gets removed from the database) ![removesnackid](img/api_delete_snack_id.png)
- Delete-request: remove soda id (it shows error but it gets removed from the database) ![removesodaid](img/api_delete_soda_id.png)

---