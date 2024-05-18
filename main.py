from src.hh_parser import HHParser
from src.vacancy_model import Vacancy
from src.data_manager import DataManager
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies

hh_parser = HHParser()


def user_interaction():
    """
    Interacts with the user to perform operations on job vacancies fetched from HeadHunter.

    Prompts the user for a search query, saves the fetched vacancies, deletes vacancies by keywords,
    and filters and displays the top vacancies based on user-defined criteria.
    """
    search_query = input("Введите ваш запрос (например Python): ")
    hh_vacancies = hh_parser.fetch_vacancies(search_query)

    vacancies_list = [Vacancy.from_json(vacancy) for vacancy in hh_vacancies]

    print(f"Получено {len(vacancies_list)} вакансий с сайта HeadHunter")

    data_manager = DataManager()
    data_manager.save_vacancies(vacancies_list)

    del_keywords = input("Введите ключевые слова, чтобы удалить вакансии (например Python Developer): ")
    data_manager.delete_vacancies_by_keyword(del_keywords)

    top_n = int(input("Сколько вакансий вывести в топ: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите зарплату (Пример: 50000 - 350000): ")

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    for i, vacancy in enumerate(top_vacancies, start=1):
        try:
            print(vacancy)
        except UnicodeEncodeError:
            print(f"{i}. Название вакансии: {vacancy.name}")


if __name__ == "__main__":
    user_interaction()