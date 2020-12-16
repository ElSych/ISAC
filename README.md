### 						ОТЧЕТ по лабораторной работе 

##### 			По дисциплине: «Информационные системы аэрокосмических комплексов»

Выполнили: 
студенты гр. М3О-312Б-18
Журавлев А.А
Григорьев Н.С

Проверил: 
Шаталов И.К

​	Цель: программным способом вырезать со снимка спутница Landsat-7 изображение заданного города (Копенгаген)
​	Реализация:
​	Координаты города заданы в виде 4 точек (points), образующих прямоугольник, каждая точка задается широтой и долготой на земном шаре. Для того, чтобы сопоставить координаты точек с координатами на изображении – индексами пикселя необходимо знать координаты краевых точек на изображении: левой верхней, правой верхней, левой нижней и правой верхней точек. Данная информация содержится в файле «MTL».  
​	Поэтому первым шагом достанем необходимые координаты из файла
Далее найдем дельта-х – как разницу между средним значением широты левой верхней и левой нижней точек снимка и средним значением широты правой верхней и правой нижней точек снимка и дельта-у – как разницу между средним значением долготы левой верхней и правой верхней точек и средним значением долготы правой нижней и правой верхней точек снимка. 		

​	Среднее значение берется для того, чтобы повысить точность. Для того, чтобы сопоставить координаты точек в долготе и широте с координатами точек на снимке введем коэффициенты пропорциональности:
C(x) = дельта-х/w

C(y) = дельта-y/hImage
Где w и h – ширина и высота снимка соответственно
	Координаты точек будем вычислять относительно левого верхнего угла – начала координат по формулам:
xp = (x-x0)/C(x)

yp = (y-y0)/C(y)

(x0;y0) - координаты левой верхней точки в градусах, (x;y)– координаты точки в градусах, (xp;yp)- новые координаты точки на снимке.
Далее зададим отрезки прямоугольника, который будет образован полученными точками и с помощью библиотеки Open CV выделим полученный прямоугольник на снимке.
Так как снимок является матрицей, то для того, чтобы вырезать город на снимке, необходимо найти dxp и dxy как ширину и высоту прямоугольника в пикселях и взять элементы из диапазона от xp0 до xp0 + dxp  и от yp0 до yp0 + dyp 

Результат: ![](https://sun9-21.userapi.com/impg/KuGMAM0YgiplworYDnsI-Y8vZ_WZezMxkQ0zwg/6oK7nKIWKzs.jpg?size=624x359&quality=96&proxy=1&sign=8f319a46eebffb62007ca0b764f1864a)

##### 			Задание №2
​	Цель: программным способом используя снимки со спутника Landsat-7 рассчитать и вывести на снимок **NDVI**  — нормализованный относительный индекс растительности 

​	Реализация: Для реализации потребуются снимки диапазонов: 3 (Red)  — видимый красный спектр и 4 (NIR)  — ближний инфракрасный спектр.
​	Поэтому первым шагом откроем файлы со снимками в 3 и 4 диапазонах соответственно как массивы с ячейками float64. Далее производим преобразования, создаём новую матрицу ndvi, ячейки которой будут подчинены правилу: если (nir+red) = 0, то ячейка = 0, иначе ячейка рассчитывается по формуле NDVI (nir-red)/(nir+red). Затем создаётся файл ndviImage.tiff в котором градиент ndvi задаётся в виде (-1) - чёрный цвет. 1 - белый.

Результат работы программы: ![img](https://sun9-12.userapi.com/iIFLeTC9PGxL45GksF6xWb9HTcdl9LW7EwoZhQ/Pj5B5oPeWBk.jpg?type=album)

При желании с помощью утилиты QGIS можно задать другие параметры градиента, например так:![img](https://sun1-23.userapi.com/p-wbjhU4HVnQNC0OJbLSSIWFjMdGHZBx2JYLxA/YteXKiodd98.jpg?type=album)

​	Итог: б*о*льшая часть снимка лежит в диапазоне от -0.2 (красный) до 0.25(жёлтый), некоторые области с NDVI = 0,475 (светло-зелёный) это обусловлено тем, что:

1. Большую площадь занимает вода, а у неё NDVI отрицательный
2. Снимок взят за 29 сентября 2000 года, температура воздуха составляла около 10 градусов Цельсия, для такой погоды NDVI = 0,25 может говорить о том, что растения готовятся к зимовке
