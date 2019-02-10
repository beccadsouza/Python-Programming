from urllib import request
url = "https://assets.datacamp.com/production/course_735/datasets/baseball.csv"
def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    lines = str(response.read()).split("\n")
    fx = open(r'data.csv', "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()
download_stock_data(url)
