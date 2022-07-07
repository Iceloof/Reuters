import requests
from bs4 import BeautifulSoup as Soup

class Reuters:
    
    def __init__(self, symbol):
        self.symbol = symbol
        self.res = self.get('https://www.reuters.com/markets/companies/'+self.symbol)
    
    def getVersion(self):
        return '1.2.0'

    def get(self, url):
        res = requests.get(url, headers={'Connection': 'keep-alive',
'Pragma': 'no-cache', 'Cache-Control': 'no-cache','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36','Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'})
        result = Soup(res.text, "html.parser")
        return result
    
    def getPrice(self):
        try:
            price = self.res.select("span[class*=markets-header__amount]")[0].text
            if price.find("--") == -1:
                return "{0:.3f}".format(float(price))
            else:
                return "N/A"
        except Exception:
            return "N/A"
    
    def getName(self):
        try:
            name = self.res.select("h1[class*=markets-header__company-name]")[0].text
            if name.find("--") == -1:
                return name
            else:
                return "N/A"
        except Exception:
            return "N/A"
    
    def getMarketCap(self):
        try:
            cap = self.res.select("div[class*=company-profile-maximizer__stats-field]")[5].select("dd")[0].text.replace(',','')
            if cap.find("--") == -1:
                return "{0:.2f}(M)".format(float(cap))
            else:
                return "N/A"
        except Exception:
            return "N/A"
    
    def getPE(self):
        try:
            PE = self.res.select("div[class*=company-profile-maximizer__stats-field]")[6].select("dd")[0].text.replace(',','')
            if PE.find("--") == -1:
                return PE
            else:
                return "N/A"
        except Exception:
            return "N/A"
        
    def getRecommendation(self):
        try:
            recommendation = 1-float(self.res.select("div[class*=range-line__marker]")[2]['style'].split(':')[1].replace('%','').replace(',',''))/100
            return "{0:.2f}%".format(float(recommendation))
        except Exception:
            return "N/A"
            
        
    def getROI(self):
        try:
            ROI = self.res.select("div[class*=company-profile-maximizer__row]")[6].select("dd")[0].text.replace(',','')
            return ROI
        except Exception:
            return "N/A"
    
    def getROE(self):
        try:
            ROE = self.res.select("div[class*=company-profile-maximizer__row]")[7].select("dd")[0].text.replace(',','')
            return ROE
        except Exception:
            return "N/A"
        
    def getSector(self):
        return "N/A"
        
    def getIndustry(self):
        try:
            industry = self.res.select("div[class*=about-company-card__industry]")[0].select("p")[0].text
            return industry
        except Exception:
            return "N/A"
