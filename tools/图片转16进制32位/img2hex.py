import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint as pp


def get_gray(path, seed=0.3, black=0, show=0):
    assert path.split(".")[1] == "png" or path.split(".")[1] == "jpg", \
        "请传入正确图片格式的路径!"
    im = plt.imread(path)

    if path.split(".")[1] == "png":
        _list = []
        gravity = np.array([0.299, 0.587, 0.114])
        im_gravity = np.dot(im[:, :, 0:3], gravity)
        if black == 0:
            im_gravity = (im_gravity > 0) & (im_gravity < seed)
        else:
            im_gravity = im.max(axis=-1)  # 这是直接转换成黑白,使用极值法
        if show != 0:
            plt.imshow(im_gravity, cmap='gray')
            plt.show()
        # for i in im_gravity:
        #     for j in i:
        #         if j == True:
        #             print(1, end="")
        #         else:
        #             print(0, end="")
        #     print("\n")
        return im_gravity

    if path.split(".")[1] == "jpg":
        gravity = np.array([0.299, 0.587, 0.114])
        im_gravity = np.dot(im, gravity)
        if black == 0:
            im_gravity = (im_gravity > 0) & (im_gravity < seed)
        else:
            im_gravity = im.max(axis=-1)  # 这是直接转换成黑白,使用极值法
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


def write_logisim_memory(black_imgs: list, old_path: str, num_flag=0):
    if num_flag == 0:
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
    img_hex_list = []

    colo_path = 'source/img/可乐罐装.png'
    colo_gray_img = get_gray(colo_path, seed=0.45)
    colo_hex = get_hex(colo_gray_img)
    img_hex_list.append(colo_hex)

    hamburger_path = 'source/img/汉堡.png'
    hamburger_gray_img = get_gray(hamburger_path, seed=0.5)
    hamburger_hex = get_hex(hamburger_gray_img)
    img_hex_list.append(hamburger_hex)

    bottled_cola_path = 'source/img/可乐瓶装.png'
    bottled_cola_gray_img = get_gray(bottled_cola_path)
    bottled_cola_hex = get_hex(bottled_cola_gray_img)
    img_hex_list.append(bottled_cola_hex)

    soda_path = 'source/img/汽水.png'
    soda_gray_img = get_gray(soda_path, seed=0.6)
    soda_hex = get_hex(soda_gray_img)
    img_hex_list.append(soda_hex)

    instant_noodles_path = 'source/img/泡面.png'
    instant_noodles_gray_img = get_gray(instant_noodles_path, seed=0.35)
    instant_noodles_hex = get_hex(instant_noodles_gray_img)
    img_hex_list.append(instant_noodles_hex)

    ham_path = 'source/img/火腿肠.png'
    ham_gray_img = get_gray(ham_path, seed=0.5)
    ham_hex = get_hex(ham_gray_img)
    img_hex_list.append(ham_hex)

    mineral_water_path = 'source/img/矿泉水.png'
    mineral_water_gray_img = get_gray(mineral_water_path, seed=0.5)
    mineral_water_hex = get_hex(mineral_water_gray_img)
    img_hex_list.append(mineral_water_hex)

    bread_path = 'source/img/面包.png'
    bread_grey_img = get_gray(bread_path, seed=0.5)
    bread_hex = get_hex(bread_grey_img)
    img_hex_list.append(bread_hex)

    biscuits_path = 'source/img/饼干.png'
    biscuits_gray_img = get_gray(biscuits_path, seed=0.5)
    biscuits_hex = get_hex(biscuits_gray_img)
    img_hex_list.append(biscuits_hex)

    yes_path = 'source/img/空心对勾.png'
    yes_gray_img = get_gray(yes_path, black=1)
    yes_hex = get_hex(yes_gray_img)
    img_hex_list.append(yes_hex)

    no_path = 'source/img/错误空心.png'
    no_gray_img = get_gray(no_path, black=1)
    no_hex = get_hex(no_gray_img)
    img_hex_list.append(no_hex)

    admin_path = 'source/img/管理员.png'
    admin_gray_img = get_gray(admin_path, black=1)
    admin_hex = get_hex(admin_gray_img)
    img_hex_list.append(admin_hex)

    write_logisim_memory(img_hex_list, "", num_flag=1)

if __name__ == "__main__":
    main()