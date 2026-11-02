import itertools
import re

def evaluate(expression, assignment):
    expression = expression.replace("<=>", "==")
    expression = expression.replace("=>", "<=")
    expression = expression.replace("^", " and ")
    expression = expression.replace("v", " or ")
    expression = expression.replace("~", " not ")

    for symbol, value in assignment.items():
        expression = re.sub(r'\b' + symbol + r'\b', str(value), expression)

    return bool(eval(expression))


def get_symbols(kb, query):
    expressions = kb + " " + query
    symbols = set(re.findall(r'\b[A-Z]\b', expressions))
    return sorted(symbols)


def tt_check_all(kb, query, symbols, assignment, results):
    if not symbols:
        kb_value = evaluate(kb, assignment)
        query_value = evaluate(query, assignment)

        results.append((assignment.copy(), kb_value, query_value))

        if kb_value:
            return query_value
        return True

    symbol = symbols[0]
    rest = symbols[1:]

    assignment[symbol] = True
    result1 = tt_check_all(kb, query, rest, assignment, results)

    assignment[symbol] = False
    result2 = tt_check_all(kb, query, rest, assignment, results)

    del assignment[symbol]

    return result1 and result2


def tt_entails(kb, query):
    symbols = get_symbols(kb, query)
    results = []

    print("\n" + "=" * 65)
    print("             TRUTH TABLE ENTAILMENT")
    print("=" * 65)

    print("\nKnowledge Base:", kb)
    print("Query         :", query)
    print("Symbols       :", ", ".join(symbols))

    entailment = tt_check_all(kb, query, symbols, {}, results)

    print("\n" + "-" * 65)
    print("TRUTH TABLE")
    print("-" * 65)

    for symbol in symbols:
        print(f"{symbol:^8}", end="")

    print(f"{'KB':^10}{'QUERY':^10}")
    print("-" * 65)

    for assignment, kb_value, query_value in results:
        for symbol in symbols:
            print(f"{str(assignment[symbol]):^8}", end="")

        print(f"{str(kb_value):^10}{str(query_value):^10}")

    print("-" * 65)

    print("\nRESULT:")
    if entailment:
        print("KB ENTAILS QUERY")
        print("KB |= QUERY")
    else:
        print("KB DOES NOT ENTAIL QUERY")
        print("KB |/= QUERY")

    print("\n" + "=" * 65)
    print("Name : Dhanush")
    print("USN  : 1WN24CS0091")
    print("=" * 65)


kb = input("Enter Knowledge Base: ")
query = input("Enter Query: ")

tt_entails(kb, query)