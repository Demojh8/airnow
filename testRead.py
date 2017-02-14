from fileReader import ExcelReader

def main():

    excelReader = ExcelReader()
    excelReader.loadData('input.xlsx',2,1,3000)

    for i in range(1, len(excelReader.data)):
        print(excelReader.data[i])   


if __name__ == '__main__':
    main()
