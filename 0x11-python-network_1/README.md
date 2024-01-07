### This is the readme of this repository.
##0x11. Python - Network #1
##Intoduction
This is project consist of the use of library such as urllib and request which is quite essential for making all kind of request of a site

Title: Python urllib and requests Module Documentation Summary

## urllib Module

### Overview:
The `urllib` module in Python provides a set of modules that offer a high-level interface for working with URLs. It is divided into several submodules, each handling specific aspects of URL manipulation.

### Key Submodules:

1. **urllib.request:**
   - Provides a way to open and read URLs.
   - Supports various protocols, including HTTP, HTTPS, FTP, and more.
   - Allows sending HTTP requests with different methods (GET, POST, etc.).

2. **urllib.error:**
   - Contains exception classes raised by urllib.

3. **urllib.parse:**
   - Helps in parsing URLs, constructing query strings, and handling URL encoding and decoding.

4. **urllib.robotparser:**
   - Implements a parser for the robots.txt file to check if a particular user agent can access a given URL.

### Example Usage:
```python
from urllib.request import urlopen

with urlopen('https://www.example.com') as response:
    html = response.read()
    print(html)
```

## requests Module

### Overview:
The `requests` module is a third-party library that simplifies making HTTP requests in Python. It abstracts the complexities of handling HTTP sessions, cookies, and headers.

### Key Features:

1. **Simplified API:**
   - Provides a simple and intuitive API for making HTTP requests.

2. **Session Management:**
   - Supports persistent sessions with automatic handling of cookies.

3. **HTTP Verbs and Parameters:**
   - Allows sending requests using various HTTP methods (GET, POST, PUT, DELETE, etc.).
   - Supports query parameters, request headers, and request bodies.

4. **File Uploads:**
   - Facilitates easy file uploads with multipart encoding.

### Example Usage:
```python
import requests

response = requests.get('https://www.example.com')
print(response.text)
```

### Installation:
```bash
pip install requests
```

## Conclusion:
Both `urllib` and `requests` modules are powerful tools for handling HTTP requests in Python. While `urllib` is part of the standard library and provides a comprehensive set of functionalities, `requests` is a popular third-party library that offers a more user-friendly interface with additional features. The choice between them depends on the specific requirements and preferences of the developer..
