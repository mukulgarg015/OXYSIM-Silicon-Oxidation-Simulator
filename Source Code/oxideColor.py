class colour:
  thickness=''
  def __init__(self,thickness):
    self.thickness=thickness
  def calcthickness(self):
    D={ '0.05':'Tan','0.07':'Brown','0.10':'Dark violet to red violet','0.12':'Royal blue','0.15':'Light blue to metallic blue','0.17':'Metallic to very light yellow green',
      '0.20':'Light gold or yellow;slightly metallic','0.22':'Gold with slight;yellow orange','0.25':'Orange to melon','0.27':'Red violet','0.30':'Blue to violet blue',
      '0.31':'Blue','0.32':'Blue to blue green','0.34':'Light green','0.35':'Green to yellow green','0.36':'Yellow green','0.37':'Green yellow','0.39':'Yellow',
      '0.41':'Light orange','0.42':'Carnation pink','0.44':'Violet red','0.46':'red Violet','0.47':'Violet','0.48':'Blue Violet','0.49':'Blue','0.50':'Blue Green',
      '0.52':'Green (broad)','0.54':'Yellow green','0.56':'Green Yellow','0.57':'Yellow to "yellowish" (not yellow but is in the position where yellow is to be expected; at times appears to be light creamy gray or metallic)',
      '0.58':'Light orange or yellow to pink','0.60':'Carnation pink','0.63':'Violet red','0.68':'"Bluish"" (not blue but borderline between violet and blue green; appears more like a mixture between violet red and blue green and looks grayish)',
      '0.72':'Blue green to green (quite broad)','0.77':'"Yellowish"','0.80':'Orange (rather broad for orange)','0.82':'Salmon','0.85':'Dull, light red violet',
      '0.86':'Violet','0.87':'Blue Violet','0.89':'Blue','0.92':'Blue Green','0.95':'Dull yellow green','0.97':'Yellow to yellowish','0.99':'orange','1.00':'Carnation pink',
      '1.02':'Violet red','1.05':'Red violet','1.06':'Violet','1.07':'Blue Violet','1.10':'Green','1.11':'Yellow Green','1.12':'Green','1.18':'Violet','1.19':'Red Violet',
      '1.21':'Violet Red','1.24':'Carnation pink to salmon','1.25':'Orange','1.28':'"Yellowish"','1.32':'Sky blue to green blue','1.40':'Orange','1.45':'Violet','1.46':'Blue Violet',
      '1.50':'Blue','1.54':'Dull yellow green'}
   
    if '0.06'>self.thickness>='0.05' :
    	return D['0.05']
    elif '0.08'>=self.thickness>='0.06' :
    	return D['0.07']
    elif '0.11'>=self.thickness>='0.08' :
        return D['0.10']	
    elif '0.135'>=self.thickness>'0.11' :
    	return D['0.12']
    elif '0.16'>=self.thickness>'0.135' :
    	return D['0.15']
    elif '0.185'>=self.thickness>'0.16' :
    	return D['0.17']
    elif '0.21'>=self.thickness>'0.185' :
    	return D['0.20']
    elif '0.235'>=self.thickness>'0.21' :
    	return D['0.22']
    elif '0.26'>=self.thickness>'0.235' :
    	return D['0.25']
    elif '0.285'>=self.thickness>'0.26' :
    	return D['0.27']
    elif '0.305'>=self.thickness>'0.285' :
    	return D['0.30']
    elif '0.315'>=self.thickness>'0.305' :
    	return D['0.31']
    elif '0.33'>=self.thickness>'0.315' :
    	return D['0.32']
    elif '0.345'>=self.thickness>'0.33' :
    	return D['0.34']
    elif '0.355'>=self.thickness>'0.345' :
    	return D['0.35']
    elif '0.365'>=self.thickness>'0.355' :
    	return D['0.36']
    elif '0.38'>=self.thickness>'0.365' :
    	return D['0.37']
    elif '0.40'>=self.thickness>'0.38' :
    	return D['0.39']
    elif '0.415'>=self.thickness>'0.40' :
    	return D['0.41']
    elif '0.43'>=self.thickness>'0.415' :
    	return D['0.42']
    elif '0.45'>=self.thickness>'0.43' :
    	return D['0.44']
    elif '0.465'>=self.thickness>'0.45' :
    	return D['0.46']
    elif '0.475'>=self.thickness>'0.465' :
    	return D['0.47']
    elif '0.485'>=self.thickness>'0.475' :
    	return D['0.48']
    elif '0.495'>=self.thickness>'0.485' :
    	return D['0.49']
    elif '0.51'>=self.thickness>'0.495' :
    	return D['0.50']
    elif '0.53'>=self.thickness>'0.51' :
    	return D['0.52']
    elif '0.55'>=self.thickness>'0.53' :
    	return D['0.54']
    elif '0.565'>=self.thickness>'0.55' :
    	return D['0.56']
    elif '0.575'>=self.thickness>'0.565' :
    	return D['0.57']
    elif '0.59'>=self.thickness>'0.575' :
    	return D['0.58']
    elif '0.615'>=self.thickness>'0.59' :
    	return D['0.60']
    elif '0.655'>=self.thickness>'0.615' :
    	return D['0.63']
    elif '0.70'>=self.thickness>'0.655' :
    	return D['0.68']
    elif '0.745'>=self.thickness>'0.70' :
    	return D['0.72']
    elif '0.785'>=self.thickness>'0.745' :
    	return D['0.77']
    elif '0.81'>=self.thickness>'0.785' :
    	return D['0.80']
    elif '0.835'>=self.thickness>'0.81' :
    	return D['0.82']
    elif '0.855'>=self.thickness>'0.835' :
    	return D['0.85']
    elif '0.865'>=self.thickness>'0.855' :
    	return D['0.86']
    elif '0.88'>=self.thickness>'0.865' :
    	return D['0.87']
    elif '0.905'>=self.thickness>'0.88' :
    	return D['0.89']
    elif '0.935'>=self.thickness>'0.905' :
    	return D['0.92']
    elif '0.96'>=self.thickness>'0.935' :
    	return D['0.95']
    elif '0.98'>=self.thickness>'0.96' :
    	return D['0.97']
    elif '0.995'>=self.thickness>'0.98' :
    	return D['0.99']
    elif '1.01'>=self.thickness>'0.995' :
    	return D['1.00']
    elif '1.035'>=self.thickness>'1.01' :
    	return D['1.02']
    elif '1.055'>=self.thickness>'1.035':
    	return D['1.05']
    elif '1.065'>=self.thickness>'1.055' :
    	return D['1.06']
    elif '1.085'>=self.thickness>'1.065' :
    	return D['1.07']
    elif '1.105'>=self.thickness>'1.085' :
    	return D['1.10']
    elif '1.115'>=self.thickness>'1.105' :
    	return D['1.11']
    elif '1.15'>=self.thickness>'1.115' :
    	return D['1.12']
    elif '1.185'>=self.thickness>'1.15' :
    	return D['1.18']
    elif '1.20'>=self.thickness>'1.185' :
    	return D['1.19']
    elif '1.225'>=self.thickness>'1.20' :
    	return D['1.21']
    elif '1.245'>=self.thickness>'1.225' :
    	return D['1.24']
    elif '1.265'>=self.thickness>'1.245' :
    	return D['1.25']
    elif '1.30'>=self.thickness>'1.265' :
    	return D['1.28']
    elif '1.36'>=self.thickness>'1.30' :
    	return D['1.32']
    elif '1.425'>=self.thickness>'1.36' :
    	return D['1.40']
    elif '1.455'>=self.thickness>'1.425' :
    	return D['1.45']
    elif '1.48'>=self.thickness>'1.455' :
    	return D['1.46']
    elif '1.52'>=self.thickness>'1.48' :
    	return D['1.50']
    elif '1.54'>=self.thickness>'1.52' :
    	return D['1.54']
    elif self.thickness not in D.keys():
        return "Thickness Not Found"
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
   







