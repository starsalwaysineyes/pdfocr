from gradio_client import Client # type: ignore
import os
OUTPUT_DIR="./output"
client = Client("https://aistudio.baidu.com/serving/app/7658/",output_dir=OUTPUT_DIR)



def ocr(pngpath="./test.png"):
    result = client.predict(
                    pngpath,
                    fn_index=1,
    )
    with open(result[1],'r') as f:
        s=f.read()
        dic=eval(s)
        print(dic["text"])
    filepath=OUTPUT_DIR
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)