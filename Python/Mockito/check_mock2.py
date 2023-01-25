from mockito import when, mock, verifyStubbedInvocationsAreUsed, unstub
from mock2 import *

def test_fetch():
    url = 'https://www.google.com'
    response = mock({'text':'OK'},spec=requests.Response)
    session = mock(requests.Session)
    when(session).get(url).thenReturn(response)
    when(requests).Session().thenReturn(session)
    r=fetch(url)
    assert r.text == 'OK'
    verifyStubbedInvocationsAreUsed()
    unstub()

if __name__ == '__main__':
    test_fetch()
    