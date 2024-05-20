from abc import ABC, abstractmethod
import requests

class AbstractAPIClient(ABC):
    """
    An abstract base class defining the interface for API clients.
    """

    @abstractmethod
    def prepare_request_params(self, keyword: str):
        """
        Prepares the parameters for fetching vacancies from the HeadHunter API.

        :param keyword: Search query to use for fetching vacancies.

        :return: Dictionary of request parameters.
        """
        pass

    @abstractmethod
    def fetch_vacancies(self, query):
        """
        Fetches job vacancies from the HeadHunter API based on a search query.

        :param query: Search query string.

        :return: List of dictionaries representing fetched vacancies.
        """
        pass

class HHParser(AbstractAPIClient):
    """
    Parses job vacancies from the HeadHunter API.

    Prepares request parameters and fetches vacancies based on a search query.
    """

    def __init__(self):
        self.base_url = 'https://api.hh.ru/vacancies'

    def prepare_request_params(self, keyword: str):
        params = {'per_page': 100, 'page': 1, 'text': keyword}
        return params

    def fetch_vacancies(self, query):
        params = self.prepare_request_params(query)
        response = requests.get(url=self.base_url, params=params)
        return response.json().get("items", [])