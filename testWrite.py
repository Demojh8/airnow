from fileWriter import ExcelWriter
import numpy

def main():

    data = numpy.array([[1,2,3],[2,3,4],[5,6,7],[6,7,8]])

    excelWriter = ExcelWriter()
    excelWriter.write('output.xlsx',data)


if __name__ == '__main__':
    main()
