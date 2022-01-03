import os


def main():
    # s = input("请输入要播放的视频文件文件名:")
    s = "NGGYu.mp4"
    if not os.path.exists(s):
        print("文件不存在")
    else:
        # mag = input("请输入亮部阈值（该值越低，所显示的视频中白色占比越多）范围0~255:")
        mag = "100"
        os.system("python Translate.py " + s + " " + mag)
        print("视频已转码成功，转码结果位于 Word.txt 中")
        os.system("python Circ.py")
        print("电路已生成成功，电路文件名为 LED.circ")
        print("正在打开电路文件")
        os.system("logisim.exe LED.circ")


if __name__ == "__main__":
    main()
