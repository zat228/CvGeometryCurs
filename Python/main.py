import numpy as np
import cv2

shir_real = 16  # Реальная ширина эталонного кирпича
vis_real = 7.5  # Реальная высота эталонного кирпича
shir_pix = 534  # Ширина кирпича на изображении в пикселях
vis_pix = 268  # Высота кирпича на изображении в пикселях
propSH = shir_real / shir_pix  # Полученный коэффициент на основе широты
propVIS = vis_real / vis_pix  # Полученный коэффициент на основе высоты
VisOfLeft = 7  # Необходимая высота кирпича
ShOfLeft = 15  # Необходимая ширина кирпича
Dlinaup = 23  # Необходимая длина кирпича (постель)
ErrOfSize = 3  # Допустимая погрешность (в обе стороны)
prots_sovpadenia = 0.9  # Минимально допустимый процент совпадения (ниже - брак)
del_s = 2  # Максимально допустимая разница в площади


def main(predel_max, tresh, img, template, counutW, counutH):
    imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    templategray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
    # Преобразование изображений в побитовые изображения
    ret, thresh1 = cv2.threshold(imgray, tresh, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(templategray, tresh, 255, cv2.THRESH_BINARY)
    # Создание контуров
    contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Переменные для нахождения максимально большого контура
    max_len = 0
    max = 0
    max_len2 = 0
    max2 = 0
    # Минимально допустимый предел длины контура
    predel_min = 10
    # Цикл для нахождения максимально большого контура с условиями размеров
    for i in contours1:
        if predel_max > len(i) > predel_min and len(i) > max_len:
            max = i
            max_len = len(i)
    for i in contours2:
        if predel_max > len(i) > predel_min and len(i) > max_len2:
            max2 = i
            max_len2 = len(i)
    # Полученные контуры
    cnt1 = max
    cnt2 = max2
    # Отрисовка контуров
    cv2.drawContours(img, [cnt1], -1, (0, 255, 255), 3)
    cv2.drawContours(img, [cnt2], -1, (0, 255, 0), 3)
    # Нахождение площади контуров
    s1 = cv2.contourArea(cnt1)
    s2 = cv2.contourArea(cnt2)
    # Площади и процент разницы между ними
    print(f"{s1} : {s2}")
    print(f"Разница в площади = {round((s1 - s2) / (s1 / 100) if s1 > s2 else (s2 - s1) / (s2 / 100), 2)}%")
    # Сравнение двух контуров и расчёт их процентного совпадения
    ret12 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
    print("Совпадение изображения с эталонным:", (1 - ret12))
    # Прохождение по всем контурам в массиве
    for i in contours1:
        x, y, w, h = cv2.boundingRect(i)  # Взятие координат и размеров контура
        # Отсеивание всех контуров не соответствующие размеру (шумы и мелкие отверстия)
        if counutW > w > 100 and counutH > h > 100:
            rect = cv2.minAreaRect(i)  # Нахождение минимального четырёхугольника для размещения контура
            box = cv2.boxPoints(rect)  # Построение точек четырёхугольника
            box = np.int0(box)  # построение четырёхугольника
            # Проверка на отсчёт с правильного угла четырёх угольника, в противном случае пересобирает массив
            if box[0][1] < y + h / 2:
                box2 = [box[3], box[0], box[1], box[2]]
                box = box2
            # Функция отрисовки линий и получения четырёхугольника
            for z in range(0, len(box)):
                if z + 1 != len(box):
                    cv2.line(img, box[z], box[z + 1], (0, 0, 0), 2, cv2.FILLED)
                else:
                    cv2.line(img, box[z], box[0], (0, 0, 0), 2, cv2.FILLED)
            # Отрисовка мтрелок
            cv2.arrowedLine(img, box[1], box[0], (0, 0, 255), 2, tipLength=0.1)
            cv2.arrowedLine(img, box[1], box[2], (0, 0, 255), 2, tipLength=0.03)
            # Вывод Размеров в консоль
            print(f"{round(propVIS * (box[0][1] - box[1][1]), 2)} cm")
            print(f"{round(propSH * (box[2][0] - box[1][0]), 2)} cm")
            # Ширина и высота
            VisLeft = round(propVIS * (box[0][1] - box[1][1]))
            ShLeft = round(propSH * (box[2][0] - box[1][0]))
            # Вывод значений на изображение
            cv2.putText(img, f"{round(propVIS * (box[0][1] - box[1][1]), 2)} cm",
                        (box[1][0], round((box[0][1] - box[1][1]) / 2 + box[1][1])), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 0), 2)
            cv2.putText(img, f"{round(propSH * (box[2][0] - box[1][0]), 2)} cm",
                        (round((box[2][0] - box[1][0]) / 2 + box[1][0]), box[1][1]), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 0), 2)
            # Проверка условий допустимости ширины, длинны, площади, совпадения фигур
            if 1 - ret12 > prots_sovpadenia and (
            round((s1 - s2) / (s1 / 100) if s1 > s2 else (s2 - s1) / (s2 / 100), 2)) < del_s and ((
                                                                                                          ShOfLeft + ErrOfSize > ShLeft > ShOfLeft - ErrOfSize or Dlinaup + ErrOfSize > ShLeft > Dlinaup - ErrOfSize) and (
                                                                                                          VisOfLeft + ErrOfSize > VisLeft > VisOfLeft - ErrOfSize or ShOfLeft + ErrOfSize > VisLeft > ShOfLeft - ErrOfSize)):
                #print("OK")
                return "OK"
            else:
                #print("NO")
                return "NO"
    # Отрисовка изображений при необходимости
    # cv2.imshow("Result1", img)
    # cv2.imshow("Result2", template)
    # cv2.waitKey(0)


def start():
    ans1 = 0
    ans2 = 0
    ans3 = 0
    # Цикл для последовательной обработки разных изображений и ввода различных настроек для каждого, при необходимости
    for i in range(1, 4):
        counutW = 550   # Отсеивание всех контуров не соответствующие размеру (шумы и мелкие отверстия)
        counutH = 1000  # Отсеивание всех контуров не соответствующие размеру (шумы и мелкие отверстия)
        predel_max = 400  # Минимально допустимый предел длины контура (Полезно при наличии посторонних объектов)
        tresh = 67  # предельное значение яркости пикселя, после которго он будет принят за 0
        # Загрузка изображений: полученное, эталонное
        img = cv2.imread(fr"E:\Games 2\Unity folder\UnityProject\{i}.png")
        template = cv2.imread(f"{i + 3}.png")
        # Изменение настроек для второго изображения (изображения постели кирпича)
        if i == 1:
            ans1 = main(predel_max, tresh, img, template, counutW, counutH)
        if i == 2:
            counutW = 1000
            predel_max = 10000
            tresh = 100
            ans2 = main(predel_max, tresh, img, template, counutW, counutH)
        if i == 3:
            counutW = 1000
            predel_max = 10000
            tresh = 100
            ans3 = main(predel_max, tresh, img, template, counutW, counutH)
            if (ans1 == "OK") and (ans2 == "OK") and (ans3 == "OK"):
                print("OK")
                return "OK"
            else:
                print(ans1, ans2, ans3)
                return "NO"
