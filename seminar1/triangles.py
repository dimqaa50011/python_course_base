# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def triangle_exist(a: int, b: int, c: int) -> bool:
    if a > b + c or b > a + c or c > a + b:
        return False
    return True


def get_triangle_type(a: int, b: int, c: int) -> str:
    if a == b and b == c and c == a:
        answer = "Равносторонний"
    elif a != b and a != c and b != c:
        answer = "Разносторонний"
    else:
        answer = "Равннобедренный"

    return answer


def start_task1():
    a1 = 5
    b1 = 6
    c1 = 7

    result = f"Треугольник со сторонами (a: {a1}, b: {b1}, c: {c1}) "

    if triangle_exist(a1, b1, c1):
        result += get_triangle_type(a1, b1, c1)
    else:
        result += "не существует"

    print(result)
