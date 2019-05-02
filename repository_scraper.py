from bs4 import BeautifulSoup
import certifi
import urllib3


def url_response(url):
    """
    Returns a response for a given URL

    Args:
        url (str): Target URL
    Returns:
        HTTPResponse: If the URL response status is 200/Ok
        None: Otherwise
    """
    try:
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        response = http.request('GET', url)
    except (urllib3.exceptions.MaxRetryError, ValueError) as error:
        print(error)
        response = None
    return response


class Repository:
    """
    Repository object parses the target repository for the required information. For example:

    Example: In `Open Access Theses`_ repository the article listings are formatted according to the format follows,::

    .. literalinclude:: docs_assets/examples/repository_example_1.html

    The following input will parse the HTML for all the paragraph tags contained in the 'div' tag with id
    'series-home'::

        url = 'https://docs.lib.purdue.edu/ecetr/'
        find = ('div', {'id': 'series-home'})
        findall = 'p'

    Args:
        url (str): URL of the form https://docs.lib.purdue.edu/<repository>/
        find (str): HTML tag pointing to the container which contains the required data
        findall (str): HTML tag to look for in the container

    ..  _Open Access Theses:
        https://docs.lib.purdue.edu/open_access_theses/
    """
    def __init__(self, url, find, findall=None):
        self.url = url
        self.soup_data = self.soup()
        self.data = None
        self.store = None
        if self.soup_data:
            self.data = self.soup_find(find, findall)

    def soup(self):
        """
        Soup method returns a beautifulsoup object of the HTML page contained in the URL

        Returns:
            BeautifulSoup: If the URL response status is 200/Ok
            None: If the URL response status is not 200/ok
        """
        response = url_response(self.url)
        if response != 0:
            if response.status == 200:
                return BeautifulSoup(response.data, "html.parser")
            else:
                return None
        else:
            return None

    def soup_find(self, find, findall=None):
        """
         soup_find method looks through all the tags contained in parsed HTML and retrieves all those which match the
         given arguments.

         Args:
             find (str): HTML tag pointing to the container which contains the required data
             find_all (str, optional): HTML tag to look for in the container

         Returns:
             list: if match is found
             None: otherwise
        """
        if type(find) is tuple:
            target = self.soup_data.find(*find)
        else:
            target = self.soup_data.find(find)
        if findall:
            if type(findall) is tuple:
                target = target.find_all(*findall)
            else:
                target = target.find_all(findall)
        return target


