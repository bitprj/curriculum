# name

Practicing with JSON

# cards_folder

Computational-Social-Science-Twitter-Topic/activities/Activity2_Stream Twitter API/cards

# checkpoint_type

Multiple Choice

# instruction

In Python, given this JSON data/Python dictionary, how would I access the "id"?

```json
file = {
  "kind": "youtube#searchListResponse",
  "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/PaiEDiVxOyCWelLPuuwa9LKz3Gk\"",
  "nextPageToken": "CAUQAA",
  "regionCode": "KE",
  "pageInfo": {
    "totalResults": 4249,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/QpOIr3QKlV5EUlzfFcVvDiJT0hw\"",
      "id": {
        "kind": "youtube#channel",
        "channelId": "UCJowOS1R0FnhipXVqEnYU1A"
      }
    }
  ]
}
```

# mc_choices

## choice_1

```
file["id"]
```

## choice_2

```
file[items][id]
```

## choice_3

```
file["items"]["id"]
```

## choice_4

```
["items"]["id"]
```

# correct_choice

```
file["items"]["id"]
```

