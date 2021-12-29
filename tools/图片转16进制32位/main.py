import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint as pp


def get_gray(path, seed=0.3):
    assert path.split(".")[1] == "png" or path.split(".")[1] == "jpg", \
        "请传入正确图片格式的路径!"
    im = plt.imread(path)

    if path.split(".")[1] == "png":
        _list = []
        gravity = np.array([0.299, 0.587, 0.114])
        im_gravity = np.dot(im[:, :, 0:3], gravity)
        im_gravity = (im_gravity > 0) & (im_gravity < seed)
        # im_max = im.max(axis=-1) #这是直接转换成黑白
        plt.imshow(im_gravity, cmap='gray')
        # for i in im_gravity:
        #     for j in i:
        #         if j == True:
        #             print(1, end="")
        #         else:
        #             print(0, end="")
        #     print("\n")
        plt.show()
        return im_gravity

    if path.split(".")[1] == "jpg":
        gravity = np.array([0.299, 0.587, 0.114])
        im_gravity = np.dot(im, gravity)
        # im_max = im.max(axis=-1)#这是直接转换成黑白
        plt.imshow(im_gravity, cmap='gray')
        plt.show()
        return im_gravity


def get_hex(array_im):
    test_array = array_im.T.copy()  # 矩阵转置
    pixel_list = []
    for _list in test_array:
        sum = 0
        i = 0
        # 计算这一列的和
        for element in _list[::-1]:
            sum += (2 ** i) * int(element)
            i += 1
        pixel_list.append(hex(sum))
    return pixel_list


def write_logisim_memory(black_imgs: list, old_path: str, num_flag=1):
    if num_flag == 1:
        new_path = "./output/" + old_path.split(".")[0] + ".txt"
        with open(new_path, 'w', encoding='utf-8') as file_object:
            file_object.write(str("v2.0 raw\n"))
            for i in range(32):
                file_object.write("00000000" + "\n")
            for hex_info in black_imgs:
                # 格式化为8位16进制
                info = str(hex_info).replace('0x', '')
                for i in range(8):
                    if len(info) < 8:
                        info = "0" + info
                    else:
                        file_object.write(info + "\n")
                        break
        file_object.close()
    else:
        w_path = "./output/all.txt"
        with open(w_path, 'w', encoding='utf-8') as file_object:
            file_object.write(str("v2.0 raw\n"))
            for i in range(32):
                file_object.write("00000000" + "\n")
            for black_img in black_imgs:
                for hex_info in black_img:
                    # 格式化为8位16进制
                    info = str(hex_info).replace('0x', '')
                    for i in range(8):
                        if len(info) < 8:
                            info = "0" + info
                        else:
                            file_object.write(info + "\n")
                            break
        file_object.close()


def main():
    # colo_path = 'source/img/可乐罐装.png'
    # colo_gray_img = get_gray(colo_path, seed=0.45)

    # hamburger_path = 'source/img/汉堡.png'
    # hamburger_gray_img = get_gray(hamburger_path, seed=0.5)

    # bottled_cola_path = 'source/img/可乐瓶装.png'
    # bottled_cola_gray_img = get_gray(bottled_cola_path)

    soda_path = 'source/img/汽水.png'
    soda_gray_img = get_gray(soda_path, seed=0.7)


if __name__ == "__main__":
    main()
