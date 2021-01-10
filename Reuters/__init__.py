from requests_html import HTMLSession
import json

class Reuters:
    
    def __init__(self, symbol):
        self.symbol = symbol
        self.res = self.get('https://www.reuters.com/companies/api/getFetchCompanyProfile/'+self.symbol)
    
    def get(self, url):
        session = HTMLSession()
        res = session.get(url)
        result = json.loads(res.text)
        return result
    
    def getPrice(self):
        try:
            price = self.res['market_data']['last']
            if price.find("--") == -1:
                return "{0:.3f}".format(float(price))
            else:
                return "N/A"
        except Exception:
            return "N/A"
    
    def getName(self):
        try:
            name = self.res['market_data']['company_name']
            if name.find("--") == -1:
                return name
            else:
                return "N/A"
        except Exception:
            return "N/A"
    
    def getMarketCap(self):
        try:
            cap = self.res['market_data']['market_cap']
            if cap.find("--") == -1:
                return "{0:.2f}(M)".format(float(cap))
            else:
                return "N/A"
        except Exception:
            return "N/A"
    
    def getPE(self):
        try:
            PE = self.res['market_data']['forward_PE']
            if PE.find("--") == -1:
                return PE
            else:
                return "N/A"
        except Exception:
            return "N/A"
        
    def getRecommendation(self):
        try:
            recommendation = self.res['market_data']['recommendation']['mean']/5
            return "{0:.2f}%".format(float(recommendation))
        except Exception:
            return "N/A"
            
        
    def getROI(self):
        try:
            ROI = self.res['market_data']['roi_ttm']
            return ROI
        except Exception:
            return "N/A"
    
    def getROE(self):
        try:
            ROE = self.res['market_data']['roe_ttm']
            return ROE
        except Exception:
            return "N/A"
        
    def getSector(self):
        try:
            sector = self.res['market_data']['sector']
            return sector
        except Exception:
            return "N/A"
        
    def getIndustry(self):
        try:
            industry = self.res['market_data']['industry']
            return industry
        except Exception:
            return "N/A"
