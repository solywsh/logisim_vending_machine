def write_logisim_memory(text_lists: list, w_path="./output/text.txt", zeros=1):
    with open(w_path, 'w', encoding='utf-8') as file_object:
        file_object.write(str("v2.0 raw\n"))
        for i in range(zeros):
            file_object.write("00000000" + "\n")
        for text in text_lists:
            # 格式化为8位16进制
            info = str(hex(text).replace("0x", ""))
            for i in range(8):
                if len(info) < 8:
                    info = "0" + info
                else:
                    print(info)
                    file_object.write(info + "\n")
                    break
        file_object.close()


def main():
    # 商品价格,商品数量
    price_list = [3, 4, 4, 3, 3, 1, 2, 2, 1]
    num_list = [10, 6, 8, 10, 5, 4, 11, 3, 8]
    money_list = [20, 30, 20]
    write_logisim_memory(price_list, "./output/price.txt")
    write_logisim_memory(num_list, "./output/num.txt")
    write_logisim_memory(money_list, "./output/money.txt", zeros=0)


if __name__ == "__main__":
    main()
