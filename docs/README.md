# Geometric Lib — документация

## Общее описание
Библиотека для работы с геометрическими фигурами: квадратом и кругом
Служит для вычисления площади и периметра данных фигур

### square
- `area(a: float) -> float` — площадь квадрата 
  ```python
  from square import area
  print(area(3.0))  # 9.0
  ```
- `perimeter(a: float) -> float` — периметр квадрата  
  ```python
  from square import perimeter
  print(perimeter(3.0))  # 12.0
  ```

### circle
- `area(r: float) -> float` — площадь круга 
  ```python
  from circle import area
  print(round(area(3.0), 3))  # 28.274
  ```
- `perimeter(r: float) -> float` — длина окружности 
  ```python
  from circle import perimeter
  print(round(perimeter(3.0), 3))  # 18.850
  ```

## История изменений
d078c8d9ee6155f3cb0e577d28d337b791de28e2
8ba9aeb3cea847b63a91ac378a2a6db758682460