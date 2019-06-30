import shutil
import os
def main():
    print("Thu muc hien hanh :", os.getcwd())
    for x in range(1, 10):
        os.makedirs("phuc"+ str(x))
        a = ("phuc" + str(x) + "/abi.bat")
        shutil.copy('vieth.bat',a)
    print("Done")
if __name__ == '__main__':
    main()
