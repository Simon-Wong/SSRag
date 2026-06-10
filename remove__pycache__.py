
def remove_pycache():
    # 删除当前目录及子目录下的__pycache__目录
    import os
    import shutil
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            if dir == '__pycache__':
                shutil.rmtree(os.path.join(root, dir))

if __name__ == '__main__':
    remove_pycache()
