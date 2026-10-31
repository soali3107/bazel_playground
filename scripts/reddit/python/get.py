from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

req = Request('https://python.org/')


try:
    response = urlopen(req)
    print(f"Success [{response.code}] with: {req}")
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
except Exception as e:
    print(f"e: {e}")
