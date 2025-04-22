# screen lens
Crowd sourced timestamps for on screen actor information.

Sorted by tmdb id.

Proposed json formatting for easy editing of on screen information:
```json
    {
        "actors": [
            {
                "id": <tmdb_id>,
                "roles": <object>[
                    {
                        "role": <string>,
                        "hidden": <boolean>, // *
                        "timeframes": <object>[
                            {
                                "start": <second>,
                                "end": <second>
                            },
                        ]
                    },
                ]
            },
        ]
    }
```
\* true: will hide the role name until user selection to prevent spoilers


Proposed json structure for easy access of actor information:
```json
    {
        <timestamp>: [
            {
                "id": <tmdb_id>,
                "roles": <object>[
                    {
                        "role": <string>,
                        "hidden": <boolean>,
                    },
                ]
            },
        ],
    }
```