from requests_html import HTMLSession

class Reuters:
    
    def __init__(self, symbol):
        self.symbol = symbol
        self.res = self.get('https://uk.mobile.reuters.com/business/stocks/overview/'+self.symbol)
    
    def get(self, url):
        session = HTMLSession()
        res = session.get(url)
        return res
    
    def getPrice(self):
        try:
            price = self.res.html.find('.section-quote-detail .price', first=True)
            if price.text.find("--") == -1:
                return price.text
            else:
                return "N/A"
        except Exception:
            return "N/A"
    
    def getName(self):
        try:
            name = self.res.html.find('.company-name', first=True)
            if name.text.find("--") == -1:
                return name.text
            else:
                return "N/A"
        except Exception:
            return "N/A"
    
    def getMarketCap(self):
        try:
            cap = self.res.html.find('.section-quote-detail .detail-value')[9]
            if cap.text.find("--") == -1:
                return cap.text+"(M)"
            else:
                return "N/A"
        except Exception:
            return "N/A"
    
    def getPE(self):
        try:
            PE = self.res.html.find('.section-quote-detail .detail-value')[10]
            if PE.text.find("--") == -1:
                return PE.text
            else:
                return "N/A"
        except Exception:
            return "N/A"
        
    def getRecommendation(self):
        try:
            recommendation = self.res.html.find('.recommendation-marker', first=True)
            return "{0:.2f}%".format(float(recommendation.attrs['style'][6:-2]))
        except Exception:
            return "N/A"
            
        
    def getROI(self):
        try:
            ROI = self.res.html.find('.ratio-graph')[6].find('.graph-bar-value', first=True)
            return ROI.text
        except Exception:
            return "N/A"
    
    def getROE(self):
        try:
            ROE = self.res.html.find('.ratio-graph')[7].find('.graph-bar-value', first=True)
            return ROE.text
        except Exception:
            return "N/A"
        
    def getSector(self):
        try:
            sector = self.res.html.find('.company-profile', first=True).find('.company-info-value')[0]
            return sector.text
        except Exception:
            return "N/A"
        
    def getIndustry(self):
        try:
            industry = self.res.html.find('.company-profile', first=True).find('.company-info-value')[1]
            return industry.text
        except Exception:
            return "N/A"
    
