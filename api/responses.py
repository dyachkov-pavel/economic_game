from drf_yasg import openapi

STOCKS_RESPONSE_SCHEMA = {
    '200': openapi.Response(
        description='200 OK - Ссылка на картинку',
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'data': openapi.Schema(type=openapi.TYPE_STRING,),
            },
            required=['data', ]
        ),
        examples={
            'application/json': {
                'data': 'https://i.postimg.cc/wMgwvk9d/16.png',
            }
        }
    ),
    '204': openapi.Response(
        description='204 No Content - Если акций еще нет',
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'data': openapi.Schema(type=openapi.TYPE_STRING,),
            },
            required=['data', ]
        ),
        examples={
            'application/json': {
                'data': 'No stocks now',
            }
        }
    ),
    '404': openapi.Response(
        description='404 Not Found - Неверный id',
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'data': openapi.Schema(type=openapi.TYPE_STRING,),
            },
            required=['data', ]
        ),
        examples={
            'application/json': {
                'data': 'Wrong company id (number)',
            }
        }
    ),
}

USER_RESPONSE_SCHEMA = {
    '200': openapi.Response(
        description='200 OK - Пользователь существует или нет',
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'exists': openapi.Schema(type=openapi.TYPE_BOOLEAN,),
            },
            required=['exists', ]
        ),
        examples={
            'application/json': {
                'exists': True,
            }
        }
    ),
    '400': openapi.Response(
        description='400 Bad Request',
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'account': openapi.Schema(type=openapi.TYPE_ARRAY,
                                          items=openapi.Items(type=openapi.TYPE_STRING)),
                'password': openapi.Schema(type=openapi.TYPE_ARRAY,
                                           items=openapi.Items(type=openapi.TYPE_STRING))
            },
        ),
        examples={
            'application/json': {
                'account': [
                    'This field is required.'
                ],
                'password': [
                    'This field is required.'
                ]
            }
        }
    ),
}
