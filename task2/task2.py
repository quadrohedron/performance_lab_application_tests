import sys

def fetch_input(paths):
    with open(paths[0]) as f:
        text = f.read()
    vertices = list(map(lambda x: tuple(map(float, x.split(' '))), text.strip().split('\n')))
    #
    with open(paths[1]) as f:
        text = f.read()
    points = tuple(map(lambda x: tuple(map(float, x.split(' '))), text.strip().split('\n')))
    #
    return vertices, points

def chk_points_brt(vertices, points):
    N_poly = len(vertices)
    vertices.append(vertices[0])
    #
    for p in points:
        if p in vertices:                # Проверка того, что точка является одной из вершин
            print(0)
        else:
            px, py = p
            for i in range(N_poly):
                flag = True              # Флаг вхождения точки в тело многоугольника
                #
                ax, ay = vertices[i]
                vpx, vpy = px-ax, py-ay  # Вектор от нынешней вершины до проверяемой точки
                bx, by = vertices[i+1]
                vqx, vqy = bx-ax, by-ay  # Вектор от нынешней вершины до следующей
                prod = vqy*vpx-vqx*vpy   # Их векторное произведение
                #
                if prod < 0:             # Отрицательное произведение (точка "слева" от стороны) означает, что точка снаружи многоугольника
                    print(3)
                    flag = False
                    break
                elif prod == 0:          # Нулевое произведение означает, что точка на линии стороны
                    if (vqx and 0 <= vpx/vqx <= 1) or (0 <= vpy/vqy <= 1): # Если точка лежит между двумя вершинами, она принадлежит стороне
                        print(1)
                        flag = False
                        break
            if flag:                     # Если точка "справа" от КАЖДОЙ стороны многоугольника, она в его теле
                print(2)
    #
    return None

if __name__ == '__main__':
    chk_points_brt(*fetch_input(sys.argv[1:3]))

