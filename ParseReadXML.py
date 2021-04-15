#!/usr/bin/env python3
'''
**********************************************************
* ReadParseXML
# version: 20210415b
* By: Nicola Ferralis <feranick@hotmail.com>
***********************************************************
'''
import urllib.request, sys
from datetime import datetime
import xml.etree.ElementTree as ET
import pandas as pd

def main():
    df = getNWSdata()
    print("\n National Weather Service Data for: KBOS")
    print(" Location: {0} ({1}, {2})".format(df['location'][0],df['longitude'][0],df['latitude'][0]))
    print(" Weather:",df['weather'][0])
    print(" Temperature:",float(df['temp_c'][0]),"C, ",float(df['temp_f'][0]),"F")
    print(" Relative Humidity:",float(df['relative_humidity'][0]),"%")
    print(" Dew point:",float(df['dewpoint_c'][0]),"C, ",float(df['dewpoint_f'][0]),"F")
    print(" Sea level pressure:",float(df['pressure_mb'][0]),"hPa")
    print(" Wind:",df['wind_string'][0])
    print(" Windchill:",float(df['windchill_c'][0]),"C, ",float(df['windchill_f'][0]),"F")
    print(" Visibility: {0:0.1f} km, {1:0.1f} mi".format(float(df['visibility_mi'][0])*1.608, float(df['visibility_mi'][0])))
    print(" Weather:",df['weather'][0])
    
    # Save to CSV
    file = "Weather-data_KBOS_"+str(datetime.now().strftime('%Y%m%d-%H%M%S'))+".csv"
    df.to_csv(file, mode="a", header=True)
    print("\n Weather data for KBOS saved in:",file,"\n")
    
#************************************
# Get NWS data
#************************************
def getNWSdata():
    # This is when parsing from saved file
    #xml_data = open('KBOS.xml', 'r').read()  # Read file

    # This when parsing from URL
    url = 'https://w1.weather.gov/xml/current_obs/KBOS.xml'
    xml_data = urllib.request.urlopen(url).read()
    root = ET.XML(xml_data)  # Parse XML
    data = []
    cols = []
    for i, child in enumerate(root):
        #print(i, child.tag, child.text)
        data.append([child.text])
        cols.append(child.tag)
    df = pd.DataFrame(data).T  # Write in DF and transpose it
    df.columns = cols  # Update column names
    return df
    
#************************************
# Main initialization routine
#************************************
if __name__ == "__main__":
    sys.exit(main())
