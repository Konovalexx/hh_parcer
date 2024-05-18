def filter_vacancies(vacancies_data: list, filter_words: list):
    """
    Filters a list of vacancies based on a list of filter words.

    :param vacancies_data: List of Vacancy objects to filter.
    :param filter_words: List of words to filter vacancies by.

    :return: Filtered list of Vacancy objects.
    """
    filtered_vacancies = []
    for vacancy in vacancies_data:
        for word in filter_words:
            if word.lower() in vacancy.name.lower():
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies


def get_vacancies_by_salary(vacancies_data: list, salary_range: str):
    """
    Filters vacancies within a specified salary range.

    :param vacancies_data: List of Vacancy objects to filter.
    :param salary_range: String specifying the minimum and maximum salary values.

    :return: Filtered list of Vacancy objects within the salary range.
    """
    min_salary, max_salary = map(int, salary_range.split('-'))
    ranged_vacancies = []
    for vacancy in vacancies_data:
        if vacancy.salary_from is not None and vacancy.salary_to is not None:
            if vacancy.salary_from >= min_salary and vacancy.salary_to <= max_salary:
                ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(vacancies_data: list):
    """
    Sorts a list of vacancies by their starting salary in descending order.

    :param vacancies_data: List of Vacancy objects to sort.

    :return: Sorted list of Vacancy objects.
    """
    return sorted(vacancies_data, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(vacancies_data: list, top_n):
    """
    Returns the top N vacancies from a sorted list.

    :param vacancies_data: Sorted list of Vacancy objects.
    :param top_n: Number of top vacancies to return.

    :return: Top N Vacancy objects.
    """
    return vacancies_data[:top_n]