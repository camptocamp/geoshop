# Extract-Geoshop interaction

1. Extract loads connectors
1. ...
1. 11
1. `CommandImportJobRunner#run` instantiates a new RequestWriter
1. `CommandImportJobRunner#run` instantiates a new ConnectorImportReader
   1. `CommandImportJobRunner#getReader` creates a new ConnectorImportReader instance that immediately invokes ConnectorImportReader#fetchCommands
   1. `ConnectorImportReader#fetchCommands` creates a new instance of a GeoshopSitn connector with parameters
   1. `GeoshopSitn` connector sends import request (GeoshopSitn.java#sendImportResult)
   1. Connector sends `POST` request to "http://geoshop/token" with username and password and gets a token in response:
   ```json
   → {"username": "...", "password": "..."}
   ← {"refresh": "...", "access": "..."}
   ```
   2. Connector sends `GET` request to "http://geoshop/extract/order" to get pending orders:
   ```http
   GET /extract/order
   ...
   Authorization: Bearer *access_token*
   ```
   3. Happens Stuff in "api/views.py#ExtractOrderView"
   4. Extract parses the result and puts it into queue
1. `CommandImportJobRunner#run` fetches a product from the queue prepared by the ConnectorImportReader and sends it to the requestWriter
   ...
1. RequestTaskRunner#run
1. RequestTaskRunner#executeTask
1. RequestTaskRunner#processTaskResult
1. RequestTaskRunner#processTaskSuccess
1. RequestTaskRunner#updateRequestWithResult attaches result to request
1. RequestTaskRunner#notifyCompletionListeners
   ...
1. GeoshopSitn#exportResult
1. GeoshopSitn#sendExportRequest
   1. OrderItems sent one by one by doing `PUT` request to http://geoshop:8000/extract/orderitem/ITEM_ID and the with some of the following parameters: file, rejected, comment, etc.
