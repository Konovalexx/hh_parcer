from src.hh_parser import HHParser
from src.vacancy_model import Vacancy
from src.data_manager import DataManager
from src.utils import get_vacancies_by_salary, sort_vacancies, get_top_vacancies

hh_parser = HHParser()

def user_interaction():
    """
    Interacts with the user to perform operations on job vacancies fetched from HeadHunter.

    Prompts the user for a search query, saves the fetched vacancies, and displays the top vacancies based on user-defined criteria.
    """
    search_query = input("Введите ваш запрос (например Python): ")
    hh_vacancies = hh_parser.fetch_vacancies(search_query)

    vacancies_list = [Vacancy.from_json(vacancy) for vacancy in hh_vacancies]

    print(f"Получено {len(vacancies_list)} вакансий с сайта HeadHunter")

    data_manager = DataManager()
    data_manager.save_vacancies(vacancies_list)

    salary_range = input("Введите зарплату (Пример: 50000 - 350000): ")

    ranged_vacancies = get_vacancies_by_salary(vacancies_list, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_n = len(sorted_vacancies)  # Показываем все найденные вакансии, соответствующие критериям
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    for i, vacancy in enumerate(top_vacancies, start=1):
        try:
            print(vacancy)
        except UnicodeEncodeError:
            print(f"{i}. Название вакансии: {vacancy.name}")

if __name__ == "__main__":
    user_interaction()