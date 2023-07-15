def bills_count(value):
    bills = {
        'one': 0,
        'five': 0,
        'ten': 0,
        'fifty': 0,
        'hundred': 0
    }

    try:
        if value <= 0:
            return False
        else:
            while value >= 100:
                value = value - 100
                bills['hundred'] = bills['hundred'] + 1
            else:
                while value >= 50:
                    value = value - 50
                    bills['fifty'] = bills['fifty'] + 1
                else:
                    while value >= 10:
                        value = value - 10
                        bills['ten'] = bills['ten'] + 1
                    else:
                        while value >= 5:
                            value = value - 5
                            bills['five'] = bills['five'] + 1
                        else:
                            while value >= 1:
                                value = value - 1
                                bills['one'] = bills['one']+1
                            else:
                                new_bills = bills
                                return new_bills
    except Exception as error:
        return error


def messages(new_bills_amount):
    message = "Notas de 100: "+str(new_bills_amount['hundred'])+"\nNotas de 50: "+str(new_bills_amount['fifty'])+"\n" \
                "Notas de 10: "+str(new_bills_amount['ten'])+"\nNotas de 5: "+str(new_bills_amount['five'])+"\n" \
                "Notas de 1: "+str(new_bills_amount['one'])

    return message


new_value = input("insira um valor a ser sacado: ")
try:
    bills_amount = bills_count(int(new_value))
    if bills_amount is False:
        print("Erro: Valor Invalido!")
    else:
        if not (type(bills_amount) is dict):
            print(bills_amount)
        else:
            print(messages(bills_amount))
except Exception as Error:
   print(Error)
