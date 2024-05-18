from abc import ABC, abstractmethod
import json
from src.vacancy_model import Vacancy


class FileManager(ABC):
    """
    An abstract base class defining the interface for file managers.
    """

    @abstractmethod
    def save_vacancies(self, vacancies):
        """
        Saves a list of vacancies to a JSON file.
        """
        pass

    @abstractmethod
    def load_vacancies(self):
        """
        Loads vacancies from a JSON file.
        """
        pass

    @abstractmethod
    def delete_vacancies_by_keyword(self, keyword):
        """
        Deletes vacancies from the JSON file that match a given keyword.
        """
        pass


class DataManager(FileManager):
    """
    Implements file-based management of job vacancies data.

    Provides methods to save, load, and delete vacancies from a JSON file.
    """

    def save_vacancies(self, vacancies):
        vacancies_data = [vacancy.to_dict() for vacancy in vacancies]
        with open('data/hh_vacancies.json', "w", encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False, indent=4)

    def load_vacancies(self):
        with open('data/hh_vacancies.json', 'r', encoding='utf-8', errors='replace') as file:
            return [Vacancy.from_dict(item) for item in json.load(file)]

    def delete_vacancies_by_keyword(self, keyword):
        vacancies = self.load_vacancies()
        vacancies = [vac for vac in vacancies if keyword.lower() not in vac.name.lower()]
        self.save_vacancies(vacancies)