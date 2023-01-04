#!/usr/bin/env python3

import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Check Python version
py_ver = sys.version_info
if py_ver.major != 3 or py_ver.minor <= 8:
    logger.error(f'Python version {py_ver} is not supported. '
                 'Please use Python 3.9+')
    sys.exit(1)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
