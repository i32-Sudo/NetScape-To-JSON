import tkinter as tk
from tkinter import filedialog
import ctypes, os

def getFile():
    root = tk.Tk(); root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

lines=[]
path = os.environ['APPDATA']

class c:
    def c():
        file_path=getFile()
        while file_path == '':
            result = ctypes.windll.user32.MessageBoxW(0, "Select a File", "", 0x30 | 0x04)
            file_path=getFile()
        with open(f'{file_path}', 'r') as f:
            lineData = f.readlines()
            for line in lineData:
                lines.append(line)
        if os.path.exists(f'{path}\\output.c'):
            os.remove(f'{path}\\output.c')
        with open(f'{path}\\output.c', 'w') as f:
            f.write('[\n')
            for i, line in enumerate(lines):
                s = line.split()
                if len(s) != 7:
                    result = ctypes.windll.user32.MessageBoxW(0, "Incorrect File Format\nCheck the file and try again.", "", 0x30 | 0x04)
                    return
                f.write(f'  {{\n'
                        f'    "name": "{s[5]}",\n'
                        f'    "value": "{s[6]}",\n'
                        f'    "domain": "{s[0]}",\n'
                        f'    "path": "{s[2]}",\n'
                        f'    "expirationDate": {s[4]},\n'
                        f'    "secure": {str(s[1]).lower()}\n'
                        f'  }}' + (',' if i < len(lines) - 1 else '') + '\n')
            f.write(']')
        with open(f"{path}\\output.c", "r") as file:
            output_contents = file.read()
        window = tk.Tk()
        window.title(f'NetScape->JSON | DONE:OK')
        window.resizable(0,0)
        text_box = tk.Text(window)
        text_box.pack()
        text_box.insert(tk.END, output_contents)
        print(path)
        window.mainloop()
            
if __name__=="__main__":
    while True:
        try:
            c.c()
        except Exception as e:
            print(e)
            result = ctypes.windll.user32.MessageBoxW(0, "An Unkown Error Has Occured.", "", 0x30 | 0x04)
            c.c()
