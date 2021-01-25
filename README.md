# Banks-backend

BUILD REST API .

### 1. Autocomplete API to return possible matches based on the branch name **ordered by IFSC code** (ascending order) with limit and offset.
    1. Endpoint: /api/branches/autocomplete?q=<>**
    2. Example: /api/branches/autocomplete?q=**RTGS**&limit=3&offset=0
    3. Sample response:


### 2. Search API to return possible matches across all columns and all rows, **ordered by IFSC code** (ascending order) with limit and offset.

    1. Endpoint: /api/branches?q=<>**
    2. Example: /api/branches?q=**Bangalore**&limit=4&offset=0
    3. Sample response:


https://bankserver.herokuapp.com/api/branches?q=kolkata
## Autocomplete Across branches 
https://bankserver.herokuapp.com/api/branches/autocomplete?q=RTGS


deployed link for testing : - <a href="http://bankserver.herokuapp.com/">Click HERE </a>
