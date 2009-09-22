from amara import bindery, xml_print


def weather_for_zip(zip_code, units = 'c'):
    """
    Change zip_code and units
    """
    
    WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s&units=%s'
    NSS = {'WEATHER_NS' : 'http://xml.weather.yahoo.com/ns/rss/1.0'}

    url = WEATHER_URL % (zip_code, units)
    doc = bindery.parse(url)
    
    forecasts = [{
            'date': node.date,
            'low': node.low,
            'high': node.high,
            'condition': node.text
            } for node in doc.xml_select(u'//WEATHER_NS:forecast', prefixes=NSS)]

    ycondition = doc.xml_select(u'//WEATHER_NS:condition', prefixes=NSS)[0]
    return {
        'current_condition': ycondition.text,
        'current_temp': ycondition.temp,
        'forecasts': forecasts,
        'title': unicode(doc.rss.channel.title)
        }

if __name__ == '__main__':
    from pprint import pprint

    # getting my city weather in Celsius
    Zaragoza = "SPXX0086"
    pprint(weather_for_zip(Zaragoza))
