import PyPDF2
import re

# pdfFileObj = open('C:\\Users\\Dell\\PycharmProjects\\Pypractice\\SUDOCODE\\sudo.pdf', 'rb')
pdfFileObj = open('C:\\Users\\Dell\\PycharmProjects\\Pypractice\\SUDOCODE\\exam.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
for num in range(int(pdfReader.numPages)):
    pageObj = pdfReader.getPage(num)

    # index = []
    # days = ['Saturday','Monday','Tuesday','Wednesday','Thursday','Friday']
    # text = str(pageObj.extractText())
    # for x in days:
    #     try :
    #         index.append(text.index(x))
    #     except : print('\n')
    #
    # index.append(len(text))
    # for i,j in zip(index,index[1:]):
    #     print(text[i:j])

    delimiters = ['Saturday','Monday','Tuesday','Wednesday','Thursday','Friday']
    text = str(pageObj.extractText())
    regexPattern = '|'.join(map(re.escape, delimiters))
    print("\n".join(re.split(regexPattern, text)[1:]))


"""
, 2nd June 201802.00 P.M. - 05.00 P.M.Applied Mathematics l*
,4th June 201802.00 P.M. - 05.00 P.M.Analog Electronics - I
, 7th June 201802.00 P.M. - 05.00 P.M.Circuit Theory*
, 8th June 201802.00 P.M. - 05.00 P.M.Digital Circuits*PRINCIPAL
"""

