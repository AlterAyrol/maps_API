import json
from requests import Response
from utils.api import Google_maps_api
from utils.checking import Checking


#python -m pytest -s -v


"""Создание, изменение и удаление новой локации"""

class Test_create_place():

    def test_create_new_place(self):

        print("\nМетод POST")
        result_post = Google_maps_api.create_new_place()
        # result_post: Response = Google_maps_api.create_new_place()      #Устаревший вариант
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        # json_key = json.loads(result_post.text)         #для вывода, в форме списка, всех ключей
        # print(list(json_key))                           #в названиях полученных ответов
        Checking.check_json_key(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')


        print("\nМетод GET проверющий POST")
        result_get = Google_maps_api.get_new_place(place_id)
        # result_get: Response = Google_maps_api.get_new_place(place_id)      #Устаревший вариант
        Checking.check_status_code(result_get, 200)
        # json_key = json.loads(result_get.text)
        # print(list(json_key))
        Checking.check_json_key(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')


        print("\nМетод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_key(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')


        print("\nМетод GET проверющий PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_key(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')


        print("\nМетод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_key(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')


        print("\nМетод GET проверющий DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_key(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'Get operation failed')
        # Get operation failed, looks like place_id doesn't exists


        print("\nТестовый сценарий test_create_new_place завершён.")


