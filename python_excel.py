import pandas as pd
def read_excel(file_path, sheet_name=None,usercols=None,skiprows=None,nrows=None):
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path,sheet_name=sheet_name,usecols=usercols,skiprows=skiprows,nrows=nrows)
        # 打印数据
        print(df)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_excel("excel_pv.xlsx","数据","A:C",1,5)