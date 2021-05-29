# Lab08 - Dicionários e Conjuntos
# Interpretador de comandos

memory_dictionary = {}  # Dicionário de memória das variáveis com seus respectivos valores
arithmetic_operators = ['+', '-']
boolean_operators = ['==', '!=', '<', '<=', '>', '>=']
boolean_composed_operators = ['AND', 'OR']


def check_variable(value):
    """Função que recebe um valor e verfica se o mesmo é uma variável, um numérico ou uma variável não definida"""
    global erro_variavel
    if value in memory_dictionary.keys():
        return int(memory_dictionary.get(value))
    else:
        if value.isnumeric() == 1:
            return int(value)
        else:
            print("Erro de referencia: a variavel",
                  value, "nao foi definida.")
            return None


def calculate_arithmetic_expression(expression):
    """Calculadora de expressões aritiméticas que recebe uma lista com os operadores, números e variáveis"""
    boolean_atual_operator = '0'
    for i in range(0, len(expression)):
        if i == 0:
            expression_result = check_variable(expression[0])
            if expression_result == None:
                return None, boolean_atual_operator

        if expression[i] in arithmetic_operators:
            next_value = check_variable(expression[i+1])
            if next_value == None:
                return None, boolean_atual_operator
            else:
                if expression[i] == '+':
                    expression_result += next_value
                elif expression[i] == '-':
                    expression_result -= next_value

        if expression[i] in boolean_operators:
            boolean_atual_operator = expression[i]
            return expression_result, boolean_atual_operator

        if expression[i] in boolean_composed_operators:
            boolean_atual_operator = expression[i]
            return expression_result, boolean_atual_operator

    return expression_result, boolean_atual_operator


def calculate_boolean_expression(expression):
    """Calculadora de um expressão booleana simples separando a expressão em antes do sinal booleano e depois"""
    expression_one, boolean_operator = calculate_arithmetic_expression(
        expression)
    if boolean_operator == '0':
        return expression_one

    elif boolean_operator != '0' and boolean_operator != 'AND' and boolean_operator != 'OR':
        del expression[0:expression.index(boolean_operator)+1]
        expression_two, boolean_composed_operator = calculate_arithmetic_expression(
            expression)
        if expression_one == None or expression_two == None:
            return None
        else:
            if boolean_composed_operator != '0':
                del expression[0:expression.index(boolean_composed_operator)+1]
            else:
                del expression[0:2]
            if boolean_operator == '==':
                return int(expression_one == expression_two), boolean_composed_operator
            elif boolean_operator == '!=':
                return int(expression_one != expression_two), boolean_composed_operator
            elif boolean_operator == '<=':
                return int(expression_one <= expression_two), boolean_composed_operator
            elif boolean_operator == '<':
                return int(expression_one < expression_two), boolean_composed_operator
            elif boolean_operator == '>=':
                return int(expression_one >= expression_two), boolean_composed_operator
            elif boolean_operator == '>':
                return int(expression_one > expression_two), boolean_composed_operator


def calculate_composed_boolean_operators(expression):
    """Cálculo das booleanas compostas com os operadores OR e AND"""
    expression = expression.split()  # Divide toda a expressão em uma lista
    logic_expressions = []  # Lista para armazenar o valor binário e os operadores AND e OR
    for i in range(0, (expression.count('AND')+expression.count('OR') + 1)):
        logic_expressions.append(calculate_boolean_expression(expression))
        if logic_expressions[i] == None:  # Verfica se alguma variável não foi nomeada
            logic_expressions = [None]
            break
    if len(logic_expressions) > 1 and (all(isinstance(x, tuple) for x in logic_expressions)) == 1:
        logic_expressions_result = list(sum(logic_expressions, ()))
        logic_expressions_result.pop(-1)
        # Calculadora de OR e AND para os valores 0 e 1
        for i in range(0, len(logic_expressions_result)):
            if i == 0:
                expression_result = logic_expressions_result[0]
            if logic_expressions_result[i] in boolean_composed_operators:
                next_value = logic_expressions_result[i+1]
                if logic_expressions_result[i] == 'AND':
                    expression_result = expression_result and next_value
                elif logic_expressions_result[i] == 'OR':
                    expression_result = expression_result or next_value
        return expression_result
    return logic_expressions[0]


while True:
    try:
        command = input().partition(' = ')
        # Verifica se o comando é do tipo salvar variável ou expressão
        if command[2] != '':
            # Verifica se o valor é permitido para uma variável
            if command[0][0].isdigit() == 1 or command[0].isalnum() == 0:
                print("Erro de sintaxe:",
                      command[0], "nao e um nome permitido para uma variavel.")
            else:
                expression = command[2]
                result = calculate_composed_boolean_operators(expression)
                # Salvar no dicionário as variáveis
                if (type(result) is tuple) == 1:
                    memory_dictionary.update(
                        {command[0]: (result[0])})
                else:
                    memory_dictionary.update(
                        {command[0]: result})
        else:
            final_result = calculate_composed_boolean_operators(command[0])
            if (type(final_result) is tuple) == 1:
                final_result = final_result[0]
            if final_result != None:
                print(final_result)
    except EOFError:
        print("Encerrando... Bye-bye.")
        break
