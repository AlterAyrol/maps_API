from requests import Response
import json


"""Методы для проверки ответов на запросы"""
class Checking:

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if status_code == response.status_code:
            print("Успешно! Статус код = " + str(response.status_code))
        else:
            print("Провал!!! Статус код = " + str(response.status_code))


    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_key(response: Response, expected_value):
        key = json.loads(response.text)
        assert list(key) == expected_value
        print('Все обязательные поля присутствуют.')


    """Метод для проверки значения обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print("Значение поля " + field_name + " верно.")


    """Метод для проверки значения обязательных полей в ответе запроса на наличие заданного слова"""
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово " + search_word + " присутствует.")
        else:
            print("Внимание! Слово " + search_word + " отсутствует.")
