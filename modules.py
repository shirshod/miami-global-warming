#!/usr/bin/env python
# coding: utf-8

# The code creates a library of predefined modules to compute relative humidity and heat indices — what the temperature feels like, since the same methods need to be called multiple ties in more than one Notebook. 

# ### Relative humidity

# In[1]:


def relHumidity(temp, dew):
    
    ### converts to celsius
    temp_c = 5.0/9.0*(temp - 32.0)
    dew_c = 5.0/9.0*(dew - 32.0)

    ### calculates saturation and actual vapor pressures in millibars
    es = 6.11*10.0**(7.5*temp_c/(237.7 + temp_c))
    e = 6.11*10.0**(7.5*dew_c/(237.7 + dew_c))

    ### calculates relative humidity as percent
    rh = (e/es)*100
    
    ### returns value
    return rh


# ### Steadman's apparent temperature and Rothfusz Regression

# NOTE: The formulae defined in the method is the same as that used by the National Weather Service to calculate heat index — an estimate of the apparent temperature or what the temperature "feels like". The initial formula tallies with the findings of Roger Steadman in 1984. If the calculated index is more than 80 degrees Fahrenheit, then the second formula — defining a Rothfusz regression and its adjustments are computed. The Rothfusz regression is not appropriate when temperature and humidity gives a heat index value below 80 degrees Fahrenheit.

# In[2]:


def heatIndex(temp, rh):
    
    ### calculates heat index (what the temperature "feels like") in fahrenheit
    hi = 0.5*(temp+61.0+((temp-68.0)*1.2)+(rh*0.094))
    hi = (hi + temp)/2

    ### calculates adjusted heat index if index is above 80 (Rothfusz Regression)
    if hi > 80:
        hi = -42.379+2.04901523*temp+10.14333127*rh -0.22475541*temp*rh-0.00683783*temp*temp-0.05481717*rh*rh+0.00122874*temp*temp*rh+0.00085282*temp*rh*rh-0.00000199*temp*temp*rh*rh

        if rh < 13 and temp > 80 and temp < 112:
            factor = abs(temp-95.)
            adjustment = ((13-rh)/4)*(((17-factor)/17)**0.5)
            hi = hi-adjustment

        elif rh > 85 and temp > 80 and temp < 87: 
            adjustment = ((rh-85)/10)*((87-temp)/5)
            hi = hi+adjustment

    ### rounds off heat index to one decimal point      
    hi = round(hi, 1)
    
    ### returns value
    return hi

