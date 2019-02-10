from tabula import read_pdf

df = read_pdf('C:\\Users\\Dell\\PycharmProjects\\Pypractice\\SUDOCODE\\exam.pdf',output_format='json')
print(df)
