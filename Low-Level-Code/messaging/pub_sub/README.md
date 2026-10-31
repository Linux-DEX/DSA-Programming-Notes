# In-memory pub-sub

`subscribe(topic, handler)` registers a callback.
`publish(topic, message)` calls the handlers for that topic inline,
in the order they subscribed. `unsubscribe` removes one handler.

Handlers run on the publisher's thread. A handler can unsubscribe
itself during publish.

## Run

```bash
python main.py
```
