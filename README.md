# Kaviar

Simplified event and data formatting and logging.

Kaviar aids developers in need of a convenient way to produce structured
representation of key-value pairs for logging or representation with a 
fixed syntax suit suited for later evaluation or just aesthetic reasons.


## Example

Logging a certain event:

```python
import logging
from kaviar import EventKvLoggerAdapter

logging.basicConfig(level=logging.DEBUG)
logger = EventKvLoggerAdapter.get_logger(__name__)
logger.info('NEW_CLIENT', client_id=42, peer_name='93.184.216.119')
```

Separating the event definition from actual logging:

```python
import logging
from functools import partial
from kaviar import EventKvLoggerAdapter

logging.basicConfig(level=logging.DEBUG)
logger = EventKvLoggerAdapter.get_logger(__name__)

log_event = partial(logger.define_logger_func(logging.INFO,
                                              'server peer_name'),
                    'NEW_CLIENT')

log_event('example.org', '93.184.216.164')
```
