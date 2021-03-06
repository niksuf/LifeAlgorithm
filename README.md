# Алгоритм "Жизнь"
Простой клеточный автомат, придуманный Д. Конвеем в 1970 году.

## Описание алгоритма
Данный алгоритм представляет собой простой клеточный автомат, придуманный Д. Конвеем в 1970 году и заключается в последовательном рекуррентном расчете
матрицы на основе ее предыдущего состояния. Алгоритм состоит из следующих правил:
- Место действия алгоритма — двухмерное поле, состоящее из ячеек — клеток.
- Каждая клетка на поле может находиться в одном из двух состояний: в живом или в мертвом. В силу конечных размеров поля, крайние клетки поля всегда
находятся в «мертвом» состоянии. Каждая клетка, кроме крайних, имеет 8 соседей.
- Распределение живых клеток (начальное состояние поля) называется первым поколением. Каждое следующее поколение рассчитывается из предыдущего следующим образом:
  - Если мертвая клетка содержит ровно три живых соседа, то на следующем ходу она становится живой.
  - Если живая клетка содержит менее 2 или более 3 соседей, то на следующем ходу она умирает.
  - Все остальные клетки сохраняют свое состояние с предыдущего хода.

Пользователь задает начальную конфигурацию ячеек (первое поколение) и дальше просто наблюдает за работой алгоритма. Функционирование продолжается
до тех пор, пока пользователь не прервет работу программы. Ввод данных в программу осуществляется при помощи текстового файла. Вывод данных производится в консоль.

Игра «Жизнь» содержит множество различных примечательных фигур. Самой известной из них является «планер». Эта фигура изменяет свою конфигурацию таким образом, 
что через 4 хода приходит в начальное состояние, но оказывается сдвинутой на 1 клетку. Последовательные стадии планера приведены на рисунке ниже.

![planner_life](https://github.com/niksuf/LifeAlgorithm/blob/master/planner_life.png)

В рамках данного алгоритма начальная конфигурация будет задаваться в виде текстового файла, состоящего из символов «-», означающих пустую клетку, 
и символов «*», означающих живую клетку. Символы будут записаны в файл в виде прямоугольной матрицы. При этом граничные элементы матрицы должны соответствовать 
мертвым клеткам:
```
------
------
--***-
------
------
------
```

## Инструкция по запуску
1. Скачать репозиторий к себе на компьютер при помощи команды:
```
git clone https://github.com/niksuf/LifeAlgorithm
```
2. Запустить приложение командой:
```
python LifeAlgorithm.py
```
3. Для того, чтобы изменить исходную матрицу, нужно поменять ее в файле `life.txt`. Например:
```
-----
--*--
---*-
-***-
-----
```
4. Если вы ввели матрицу, для которой алгоритм является бесконечным, то можно просто остановить программу путем нажатия, например, сочетания `Ctrl + C`.
