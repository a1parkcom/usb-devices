fields_id_name = {  # id: name
    0: 'Сумма операции, выраженная в минимальных единицах валюты',
    1: 'Дополнительная сумма операции, выраженная в минимальных единицах валюты',
    4: 'Код валюты операции',
    6: 'Оригинальная дата и время совершения операции YYYYMMDDHHMMSS на Хосте',
    8: 'Способ ввода карты',
    10: 'Номер карты',
    13: 'Код авторизации',
    14: 'Номер ссылки (RRN или Transaction ID)',
    15: 'Код ответа от хоста',
    19: 'Дополнительные данные ответа',
    21: 'Оригинальная дата и время совершения операции YYYYMMDDHHMMSS на терминале',
    23: 'Идентификатор транзакции в коммуникационном сервере',
    25: 'Код операции',
    26: 'Уникальный номер транзакции на стороне ККМ',
    27: 'Идентификатор внешнего устройства (TerminalID)',
    28: 'Идентификатор продавца (MerchantID)',
    39: 'Статус проведения транзакции',
    51: 'Статус завершения операции на кассе',
    52: 'Номер слипа (Номер чека завершенной операции на терминале)',
    64: 'Режим выполнения пользовательской команды 1',
    65: 'Режим выполнения пользовательской команды 2',
    67: 'Статус (результат) выполнения пользовательской команды',
    70: 'Данные (криптограмма)',
    86: 'Дополнительные данные транзакции',
    89: 'Наименование модели ВУ',
    90: 'Данные для печати на чеке',
}

fields_id = tuple(fields_id_name.keys())

errors_id_name = {
    0: 'DC не смог передать ответ от терминала. Возможная причина, внутренняя ошибка DC',
    1: 'Истекло время исполнения операции. Устанавливает полем «timeout» в запросе',
    3: 'Общая ошибка, ошибка параметров DC, не поддерживаемый метод HTTP, неизвестная ошибка, ошибка во время работы DC',
    4: 'Ошибка поля или ошибка запроса, как между кассой и DC, так и между DC и терминалом',
    13: 'Ошибка обмена данными между DC и терминалом. Возможная причина в отсутствии устройства или ответ не по протоколу SA',
    15: 'Обмен данными прерван, например, выключение DC, мониторинг подключения устройства или отменен другим обменом',
    16: 'Устройство занято, например, занято другим обменом'
}

errors_id = tuple(errors_id_name.keys())

transaction_status_name_id = {
    0: 'Неопределенный статус. Транзакция не выполнена.',
    1: 'Одобрено. Положительное завершение транзакции.',
    2: 'Операция «Оплата» одобрена не на полную сумму. Операция «Возврат ЭС» завершена частично (не одобрен возврат '
       'за счет собственных средств клиента). При использовании СБП операция «Сверка итогов» успешна только на хосте '
       'банка.',
    16: 'Отказано. Транзакция проведена, но ее одобрение не получено.',
    34: 'Нет соединения.',
    53: 'Операция прервана.',
}


class CurrencyCode:
    RUB = 643


class OperationsCodes:
    test_connect = 26

    sale = 1
    cancel_sale = 4
    emergency_cancel_sale = 53

    reconciliation_of_results = 59
