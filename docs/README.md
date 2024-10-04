#  Geometric figures
## Описание
Этот проект предоставляет функции для вычисления площади и периметра различных геометрических фигур: квадрата, прямоугольника, треугольника и круга.

## Функции
1. ``area_square(a)``
Описание: Вычисляет площадь квадрата по длине стороны.
Параметры: ``a``: длина стороны квадрата (число).
Возвращаемое значение: Площадь квадрата (число).

**Пример вызова**
```python
side = 5
square_area = area_square(side)
print(f"Площадь квадрата со стороной {side} равна {square_area}")
```

2. ``perimeter_square(a)``
+ Описание: Вычисляет периметр квадрата по длине стороны.
+ Параметры: ``a``: длина стороны квадрата (число).
+ Возвращаемое значение: Периметр квадрата (число).

**Пример вызова**
```python
side = 5
square_perimeter = perimeter_square(side)
print(f"Периметр квадрата со стороной {side} равен {square_perimeter}")
```

3. ``area_triangle(a, h)``
+ Описание: Вычисляет площадь треугольника по длине основания и высоте.
Параметры: 
    + ``a``: длина основания треугольника (число).
    + ``h``: высота треугольника (число).
+ Возвращаемое значение: Площадь треугольника (число).

**Пример вызова**
```python
base = 5
height = 4
triangle_area = area_triangle(base, height)
print(f"Площадь треугольника с основанием {base} и высотой {height} равна {triangle_area}")
```
4. ``perimeter_triangle(a, b, c)``

+ Описание: Вычисляет периметр треугольника по длинам его сторон.
+ Параметры:
    + ``a``: длина первой стороны треугольника (число).
    + ``b``: длина второй стороны треугольника (число).
    + ``c``: длина третьей стороны треугольника (число).
+ Возвращаемое значение: Периметр треугольника (число).

**Пример вызова**
```python
side1 = 5
side2 = 4
side3 = 3
triangle_perimeter = perimeter_triangle(side1, side2, side3)
print(f"Периметр треугольника со сторонами {side1}, {side2}, {side3} равен {triangle_perimeter}")
```
5. ``area_rectangle(a, b)``

+ Описание: Вычисляет площадь прямоугольника по длине и ширине.
+ Параметры:
    + ``a``: длина прямоугольника (число).
    + ``b``: ширина прямоугольника (число).
+ Возвращаемое значение: Площадь прямоугольника (число).

**Пример вызова**
```python
length = 5
width = 4
rectangle_area = area_rectangle(length, width)
print(f"Площадь прямоугольника с длиной {length} и шириной {width} равна {rectangle_area}")
```

6. ``perimeter_rectangle(a, b)``

+ Описание: Вычисляет периметр прямоугольника по длине и ширине.
+ Параметры:
    + ``a``: длина прямоугольника (число).
    + ``b``: ширина прямоугольника (число).
+ Возвращаемое значение: Периметр прямоугольника (число).

**Пример вызова**
```python
length = 5
width = 4
rectangle_perimeter = perimeter_rectangle(length, width)
print(f"Периметр прямоугольника с длиной {length} и шириной {width} равен {rectangle_perimeter}")
```

7. ``area_circle(r)``

+ Описание: Вычисляет площадь круга по радиусу.
+ Параметры: ``r``: радиус круга (число).
+ Возвращаемое значение: Площадь круга (число).

**Пример вызова**
```
radius = 5
circle_area = area_circle(radius)
print(f"Площадь круга с радиусом {radius} равна {circle_area}")
```

8. ``perimeter_circle(r)``
+ Описание: Вычисляет периметр круга по радиусу.
Параметры: ``r``: радиус круга (число).
+ Возвращаемое значение: Периметр круга (число).

**Пример вызова**
```python
radius = 5
circle_perimeter = perimeter_circle(radius)
print(f"Периметр круга с радиусом {radius} равен {circle_perimeter}")
```
**Пример использования**
```python
import math

# Импортируем функции из модуля
from geometric_figures import area_square, perimeter_square, area_triangle, perimeter_triangle, area_rectangle, perimeter_rectangle, area_circle, perimeter_circle

# Вычисляем площадь и периметр различных фигур
square_side = 5
square_area = area_square(square_side)
square_perimeter = perimeter_square(square_side)

triangle_base = 5
triangle_height = 4
triangle_area = area_triangle(triangle_base, triangle_height)
triangle_side1 = 5
triangle_side2 = 4
triangle_side3 = 3
triangle_perimeter = perimeter_triangle(triangle_side1, triangle_side2, triangle_side3)

rectangle_length = 5
rectangle_width = 4
rectangle_area = area_rectangle(rectangle_length, rectangle_width)
rectangle_perimeter = perimeter_rectangle(rectangle_length, rectangle_width)

circle_radius = 5
circle_area = area_circle(circle_radius)
circle_perimeter = perimeter_circle(circle_radius)

# Выводим результаты
print(f"Площадь квадрата со стороной {square_side} равна {square_area}")
print(f"Периметр квадрата со стороной {square_side} равен {square_perimeter}")

print(f"Площадь треугольника с основанием {triangle_base} и высотой {triangle_height} равна {triangle_area}")
print(f"Периметр треугольника со сторонами {triangle_side1}, {triangle_side2}, {triangle_side3} равен {triangle_perimeter}")

print(f"Площадь прямоугольника с длиной {rectangle_length} и шириной {rectangle_width} равна {rectangle_area}")
print(f"Периметр прямоугольника с длиной {rectangle_length} и шириной {rectangle_width} равен {rectangle_perimeter}")

print(f"Площадь круга с радиусом {circle_radius} равна {circle_area}")
print(f"Периметр круга с радиусом {circle_radius} равен {circle_perimeter}")
```

**Дополнительная информация**:

Модуль ``math`` содержит константу ``pi``, которая используется в функциях для вычисления площади и периметра круга.

Для использования проекта необходимо импортировать модуль ``geometric_figures`` и использовать его функции.

**Автор**: hideomiamoto

**Дата**: 04/10/2024

**Лицензия**: MIT
```