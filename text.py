

##########################################################################################################

def get_text():
    
    text = {}
    text['analysis'] = {}
    text['plot_titles'] = {}
    text['hue_titles'] = {}

    #########################################################################
    # Analytic Comments
    #########################################################################

    text['analysis']['Barplot'] = {}
    text['analysis']['Barplot']['tipo_vehiculo'] = """
    **Insights:**
    - The **most frequent** vehicle type `(tipo_vehiculo)` involved in Madrid traffic accidents are **passenger cars** `(turismo)`, which are present in the **70%** of the Madrid accidents.
    - The **second** one are the **motorbikes** `(moto)`, with a relative frequency of **13%**.
    - The **third** one are the **vans** `(furgoneta)`, which are involved in the **6.5%** of traffic accidents in Madrid.
    - The remaining options has a non significant weight in Madrid traffic accidents, according to the available data.
    """
    text['analysis']['Barplot']['tipo_persona'] = """
    **Insights:**
    - The **most frequent** type of person `(tipo_persona)` involved in Madrid traffic accidents are the **drivers** `(conductor)`, with a percentage of **81%**.
    - The **second** one are the **passengers** `(pasajeros)`, with a relative frequency of **16%**.
    - The **third** one is the remaining category, the **pedestrians** `(peatón)`, which are only part of the **3.5%** of Madrid traffic accidents.
    """
    text['analysis']['Barplot']['rango_edad'] ="""
    **Insights:**
    - The **dominant** age group `(rango_edad)` involved in Madrid traffic accidents are people with an **age between 25 and 54 years**, being involved in the **66.3%** of the accidents. 
    - The **second** age group are those immediately below or above the dominant group, i.e. people with an **age in [18,24] or [55,64]**. The **23.50%** of people involved in the accidents belong to this group.
    - The **third** one are the oldest people, whose **age is >= 65**, and are involved in the **6.4%** of the accidents.
    - The **fourth** group are the youngest people, whose **age is < 18**, and are involved only in the **3.8%** of the accidents.
    """
    text['analysis']['Barplot']['sexo'] = """
    **Insights:**
    - The **most frequent**  sex `(sexo)` involved in Madrid traffic accidents are the **men** `(hombre)`, which are present in the **68%** of the accidents.
    - The **women** are involved in the remaining **32%** of the accidents.
    """
    text['analysis']['Barplot']['lesividad'] = """
    **Insights:**
    - The **most part of people (55%)** of the people involved in Madrid traffic accidents **didn't need medical assistance** `(Sin asist. sanitaria)` after the accident.
    - The **22%** of the people **received medical assistance in the spot** `(Asist. solo insitu)`.
    - The **7.2%** were **hospitalized for 24 hours or less** `(Ingreso <= 24h)`.
    - The **6.75%** needed to **go to a medical centre**, either immediately after the accident or a few days later `(Asist.inmediata CS)` or `(Asist.posterior CS)`.
    - The **5.2%** went to **urgency** but **without** need of **hospitalization** `(Urg. sin ingreso)`.
    - The **2.1%** of people were **hospitalized more than 24 hours** `(Ingresa > 24h)`.
    - Only a **0.12%** of people involved in the accidents **die within the first 24 hours after the accident** `(Fallecido)`.
    """
    text['analysis']['Barplot']['positiva_alcohol'] = """
    **Insights:**
    - Almost all the people involved in Madrid traffic accidents **(97%) didn't test positive for alcohol** `(positiva_alcohol)`. 
    - Only a **3%** of people involved in Madrid accidents **tested positive for alcohol**.
    """
    text['analysis']['Barplot']['positiva_droga'] = """
    **Insights:**
    - Almost all the people involved in Madrid traffic accidents **(99.7%) didn't test positive for drugs** `(positiva_droga)`. 
    - Only a **0.3%** of people involved in Madrid accidents **tested positive for drugs**.
    """
    text['analysis']['Barplot']['some_death_involved'] = """
    **Insights:**
    - In almost all traffic accidents in Madrid (99.85%) there were no fatalities involved in the first 24 hours.     
    - In only a 0.15% of Madrid traffic accidents there were deaths in the 24 hours after the accident.   
    """
    text['analysis']['Barplot']['distrito'] = """
    **Insights:**
    - The Madrid **district** `(distrito)` with **more affluence of accidents** is **Salamanca (7.46%)**, followed by **Puente de Vallecas (7.36%)** and **Chamartin (6.86%)**.
    - The districts with **lower affluence of accidents** are **Vicalvaro (1.73%)**, **Barajas (1.97)%** and **Moratalaz (2.73%)**.
    """
    text['analysis']['Barplot']['tipo_accidente'] = """
    **Insights:**
    - The **most frequent  accident type** `(tipo_accidente)` in Madrid are **frontal side collisions (22.85%)** `(colisión fronto-lateral)`.
    - The **second** one are the **rear-end collision (20.83%)** `(alcance)`.
    - The **third** one are the **fixed obstacle collision (15.41%)** `(choque obstaculo fijo)`.
    - Another remarkable types are: **fall (9.89%)** `(Caida)`, **hit and run (6.82%)** `(Atropello a persona)`, **multiple collision (3.85%)** `(colision multiple)`, and **frontal collision (2.24%)** `colison frontal`.
    - There are few non significan options: `despeñamiento` **(0.01%)**, `Atropello animal` **(0.37%)**, `Vuelco` **(0.47%)** and `Salida via` **(0.65%)**.
    """
    text['analysis']['Barplot']['estado_meteorológico'] = """
    **Insights:**
    - The vast majority **(84.21%)** of the Madrid traffic accidents happened in **clear weather** `(despejado)`.
    - The most part of the remaining accidents occured in **light rain (7.29%)** `(lluvia debil)` or **cloudy (6.69%)** `(Nublado)`. 
    - The least frequent weather condition in the Madrid traffic accidents are **heavy rain (1.66%)** `(Lluvia intensa)`, **snowing (0.12%)** `(Nevando)`, and **hailing (0.02)** `(Granizando)`.
    - The remaining options has a non significant weight in Madrid accidents, according to the available data.
    """
    text['analysis']['Barplot']['weekday'] = """
    **Insights:**
    - The **most usual** week-day for having a traffic accident in Madrid is **Friday (16.69%)**.
    - The **second** and the **third** are **Thursday (15.34%)** and **Wednesday (15.04%)**.
    - The **least usual** days are **Sunday (11.34%)**, **Saturday (12.89%)**, **Monday (13.79%)** and **Tuesday (14.91%)** .
    """
    text['analysis']['Barplot']['phy_severity'] = """
    **Insights:**
    - The **63%** of people involved in Madrid traffic accident suffered **low severity physical consequences** `(phy_severity)`. 
    - The **26%** of them suffered **high severity physical consequences**.
    - While **12%** suffered **medium severity physical consequences**. 
    """
    text['analysis']['Barplot']['severe_accident'] = """
    **Insights:**
    - *At least* the **2.68%**  of Madrid traffic accidents were **severe**.
    - *At most* a **97.32%* of them were indeed **not severe**.
        >⚠️ This is an **lower-bound estimatimation** of the first statistic and a **upper-bound estimation** of the second one, because of the presence of missing values in `lesividad`. 
         All the people involved in an accident with unknown lesivity (missing values) are directly considered as non-severe lesivity. 
         Therefore, if in an accident two people were involved, one with low physical severity, and other with unknown, this acciden is considered as non-severe, evem thouth the lesiviry of the second person could actually be severe. 
    """
    text['analysis']['Barplot']['some_positive_involved'] = """
    **Insights:**
    - *At least* the **7.01%** of Madrid traffic accidents there was some **positive** test for drugs or alcohol among the people involved. 
    - *At most* the **92.99%** of them ther was non positibe among the people involved.
        >⚠️ This is a **lower-bound estimatimation** of the first statistic and a **upper-bound estimation** of the second one, because of the presence of missing values in `positiva_alcohol`. 
         Drivers with unknown data regarding the alcohol test are directly considered as non-alcohol-positive drivers, even though they could actually be positive for alcohol.
    """
    text['analysis']['Barplot']['age_category'] = """
    **Insights:**
    - The **most part (81.1%)** of people involved in Madrid traffic accidents are **adults**. 
    - The **14.87%** are **young** people.
    - And the remaining **4.04%** are **old**.
    """
    text['analysis']['Barplot']['male_driver_involved'] = """
    **Insights:**
    - *At least* in the **83.9%** of Madrid traffic accidents **male drivers were involved**.  
    - *At most* in the **16.1%** of the accidents **male drivers were not involved**. 
        >⚠️ This is an **lower-bound estimatimation** of the first statistic and a **upper-bound estimation** of the second one, because of the presence of missing values in `sex`. 
         If in an accident two drivers were involved, one was female an the sex of other is unknown (missing value), 
         it is considered as non-male-driver-involved accident, even though the missing sex could be actually male.
    """
    text['analysis']['Barplot']['only_male_driver_involved'] = """
    **Insights:**
    - *At least* in the **50.57%** of Madrid traffic accidents **only men drivers were involved** `(only_male_driver_involved)`. 
    - *At most* in the **49.43%** of the accidents both **men and women drivers were involved**.
        >⚠️ This is an **lower-bound estimatimation** of the first statistic and a **upper-bound estimation** of the second one, because of the presence of missing values in `sex`. 
         If in an accident two drivers were involved, one was male an the sex of other is unknown (missing value), 
         it is considered as non-only-male-driver-involved accident, even though the missing sex could be actually male.
    """
    text['analysis']['Barplot']['female_driver_involved'] = """
    **Insights:**
    - *At least* in the **36.5%** of traffic accidents in Madrid **female drivers were involved** `(female_driver_involved)`. 
    - *At most* in the **63.5%** of the accidents female drivers were not involved.
        >⚠️ This is an **lower-bound estimatimation** of the first statistic and a **upper-bound estimation** of the second one, because of the presence of missing values in `sex`. 
         If in an accident two drivers were involved, one was male an the sex of other is unknown (missing value), 
         it is considered as non-female-driver-involved accident, even though the missing sex could be actually female.    """
    text['analysis']['Barplot']['only_female_driver_involved'] = """
    **Insights:**
    - *At least* in the **9.17%** of traffic accidents in Madrid there were only female drivers involved. 
    - *At most* in the **90.83%** of the accidents not only female drivers were involved.
        >⚠️ This is an **lower-bound estimatimation** of the first statistic and a **upper-bound estimation** of the second one, because of the presence of missing values in `sex`. 
         If in an accident two drivers were involved, one was female an the sex of other is unknown (missing value), 
         it is considered as non-only-female-driver-involved accident, even though the missing sex could be actually female.    
         """
    text['analysis']['Barplot']['young_driver_involved'] = """
    **Insights:**
    - *At least* in **4.25%** of the Madrid traffic accidents young drivers (age in [18,24]) were involved. 
    - *At most* in **95.75%** of the accidents there were non young driver involved.
        >⚠️ This is an **lower-bound estimatimation** of the first statistic and a **upper-bound estimation** of the second one, because of the presence of missing values in `rango_edad`. 
         Drivers with unknown age are directly considered as non-young drivers, even though they could actually be young ([18,24]). 
         """ 
    text['analysis']['Barplot']['old_driver_involved'] = """
    **Insights:**
    - *At least* in the **5.74%** of Madrid traffic accidents old drivers (>= 65) were involved. 
    - *At most* in the **94.26%** of Madrid traffic accidents, non-old drivers were involved.
        >⚠️ This is an **lower-bound estimatimation** of the first statistic and a **upper-bound estimation** of the second one, because of the presence of missing values in `rango_edad`. 
         Drivers with unknown age are directly considered as non-old drivers, even though they could actually be old (>= 65).
    """    
    text['analysis']['Barplot']['positive_driver_involved'] = """
    **Insights:**
    - *At least* the **7.21%** of Madrid traffic accidents positive in drugs or alcohol drivers `(positive_driver_involved)` were involved. 
    - *At most* the **92.79%** of the accidents were non positive drivers involved.
        >⚠️ This is an **lower-bound estimatimation** of the first statistic and a **upper-bound estimation** of the second one, because of the presence of missing values in `positiva_alcohol`. 
         Drivers with unknown data regarding the alcohol test are directly considered as non-alcohol-positive drivers, even though they could actually be positive for alcohol.
    """   

    #########################################################################

    text['analysis']['Histogram'] = {}
    text['analysis']['Histogram']['num_people_involved'] = """
    **Insights:**
    - In the **most part (72.3%)** of Madrid traffic accidents **2 or 3 people were involved** `(num_people_involved)`. 
    - In the **16.11%** of the cases only **one person was involved** in the accident.
    - Int the **9.42%** of the cased **4 or 5 people were involved**.
    - Only in the **7.55%** of the accidents **more than 5 people were involved**.
    """
    text['analysis']['Histogram']['year'] =  """
    **Insights:**
    - The year with **more affluence of traffic accidents** in Madrid was **2019 (21.95%)**, followed by **2023 (20.69%)**, and **2022 (20.23%)**.
    - The years with the **lowest traffic accidents** are **2021 (17.96%)** and especially **2020 (14.18%)**. This was probably due to the influence of the pandemic situation and the restrictions imposed on the population, which led to a decrease in traffic, especially noticeable during the lockdown and the following months.
    - Although 2024 (4.99%) is actually the year with the lowest number of traffic accidents in Madrid, this should be taken with caution, as data was only available for the first three months of this year, so its results are not comparable with the others.
    """
    text['analysis']['Histogram']['quarter'] =  """
    **Insights:**
    - The **quarters** with the **highest number of traffic accidents** in Madrid are the **first (28.28%)** and **last (27.56%)** quarters, i.e. the period from November to March.    
    - And the **quarters** with the **lowest number of traffic accidents** are the **second (22.96%)** and **third (21.20%)** quarters, that is, the period from April to September.    
    """
    text['analysis']['Histogram']['month'] = """
    **Insights:**
    - The **months** with the **highest number of traffic accidents** in Madrid are in the period from **September to March**, covering the **63.9%** of the  accidents.   
    - The **remaing months** cover the remaining **36.1%** of the accidents. 
    - The mont with the **lowest affluence** of accidents is **August (5.35%)**   
    """
    text['analysis']['Histogram']['week'] = """
    ❗*We recommned you to set a large enough number of bins to extrtact better insights form this visualization.*

    **Insights:**
    - The **weeks** with **highest number of traffic accidents** in Madrid are from **35 to 13**, corresponding to the first and last quarter.      
    - The ones with the **lowest affluence** are from **14 to 34**, corrsponding to second and third quarters.
    """
    text['analysis']['Histogram']['day'] = """
    ❗*We recommned you to set a large enough number of bins to extrtact better insights form this visualization.*
    
    **Insights:**
    - The **distribution of traffic accidents in Madrid over the days** is fairly **uniform**, which means that there is no special day with a higher or lower number of accidents.
    - The only day that breaks this pattern is the 31st, which shows a lower number of accidents than the rest, but this is due to the fact that not all months have 31 days.
    """

    #########################################################################

    text['analysis']['Lineplot'] = {}
    text['analysis']['Lineplot']['year'] =  """
    **Insights:**
    - The year with **more affluence of traffic accidents** in Madrid was **2019 (22k)**, followed by **2023 (21k)**, and **2022 (20k)**.
    - The years with the **lowest traffic accidents** are **2021 (18k)** and especially **2020 (14k)**. This was probably due to the influence of the pandemic situation and the restrictions imposed on the population, which led to a decrease in traffic, especially noticeable during the lockdown and the following months.
    - Although 2024 (5k) is actually the year with the lowest number of traffic accidents in Madrid, this should be taken with caution, as data was only available for the first three months of this year, so its results are not comparable with the others.
    """
    text['analysis']['Lineplot']['quarter'] =  """
    **Insights:**
    - The **quarters** with the **highest number of traffic accidents** in Madrid are the **first (28k)** and **last (27.5k)** quarters, i.e. the period from November to March.    
    - And the **quarters** with the **lowest number of traffic accidents** are the **second (23k)** and **third (21k)** quarters, that is, the period from April to September.    
    """
    text['analysis']['Lineplot']['month'] = """
    **Insights:**
    - The **months** with the **highest number of traffic accidents** in Madrid are in the period from **September to March**, were **55k** accidents happend, what means the **63.9%** of them.
    - The **remaing months** cover the remaining **36.1%** of the accidents, which are **36k**. 
    - The months with the **lowest affluence** are the **summer months**, probably due to the fact that Madrid citizens usually go out of the city during that period, and there is less traffic withing the city.   
    """
    text['analysis']['Lineplot']['week'] = """
    **Insights:**
    - The **weeks** with **highest number of traffic accidents** in Madrid are from **35 to 13**, corresponding to the first and last quarter.      
    - The ones with the **lowest affluence** are from **14 to 34**, corrsponding to second and third quarters.
    - It is worth highlighting the decrease experienced in the last and first weeks of the year, as well as in the weeks between July and August, that is to say, in the middle of summer, when Madrid is less busy with its citizens, who are away on holiday, and therefore there is less traffic within the city.    """
    text['analysis']['Lineplot']['day'] = """
    **Insights:**
    - The **distribution of traffic accidents in Madrid over the days** is fairly **uniform**, which means that there is no special day with a higher or lower number of accidents.
    - The only day that breaks this pattern is the 31st, which shows a lower number of accidents than the rest, but this is due to the fact that not all months have 31 days.
    """
    text['analysis']['Lineplot']['hour'] = """
    **Insights:**
    - With a simple glance, it can be concluded that the highest number of accidents occurs in the afternoon, when most people leave work and, therefore, when most people take the car. 
    - During the night there is a much lower number of accidents since the vast majority of people are sleeping and therefore the number of cars on the road is very low, so the possibility of an accident is also very low.
    - There is also a small spike in the hours around 9 am, which corresponds to the entrance of people to their jobs so many people take the car to get to their offices and therefore there are more opportunities for accidents.
    """
    text['analysis']['Lineplot']['weekday'] =  """
    **Insights:**
    - The **most usual** week-day for having a traffic accident in Madrid is **Friday (17k, 16.69%)**.
    - The **second** and the **third** are **Thursday (15.3k, 15.34%)** and **Wednesday (15k, 15.04%)**.
    - The **least usual** days are **Sunday (11k, 11.34%)**, **Saturday (13k, 12.89%)**, **Monday (14k, 13.79%)** and **Tuesday (15k, 14.91%)** .
    """
    text['analysis']['Lineplot']['year-quarter'] = """
    **Insights:**
    - In this plot the effect of the pandemic is quite clear, as in the quarters affected by the lock-down (Q1 and especially Q2) the traffic accidents in Madrid suffered a huge drop.
      This is distorting the aggregate statistic for Q2, as it is also noticeable that the pattern in the rest of the years is that Q2 and Q4 are the quarters with the highest number of accidents, while in Q1 and Q3 it is lower. 
      But this pattern does not hold true in 2020 due to the Pandemic situation, with Q2 being the quarter with  the lowest number of accidents by far. This affects the overall average, making this quarter lower than Q1, even though this is a pattern that is not observed within the rest of the available years. 
    - However, a pattern that holds every year and is quite obvious is that Q3 is the quarter with the lowest number of accidents in Madrid, and the possible reason behind this is that in the summer period most Madrilenians go out, and inland traffic is severely reduced.
    - Another clear fact is that Q4 is the quarter with the highest number of accidents within each year. This fact is not well captured by the aggregated version of this graph as the only quarter available for 2024 is Q1, and this is distorting the overall results, artificially giving more weight to Q1, making it with more accidents than Q4, even though this pattern is not reflected at all within each year.
    """
    text['analysis']['Lineplot']['year-month'] = """
    **Insights:**
    - In this plot the effect of pandemic situation is again absolutely clear. The months of 2020 afffected by the lock-down experienced a huge decrement in the number of traffic accidents, due to obvious reasons, since the traffic stopped almost completely.
    - There is a clear seasonal patter within each year (excluding 2020, the most affected by pandemic).
      Madrid traffic accidents start decreasing smoothly from May to July, and sharply in August, and after that increase exponentially up to Octuber, and then start decreasing again up to January or Febrary, and then start growing again up to May. And the pattern is generally repeted along the years.
    """
    text['analysis']['Lineplot']['year-month-day'] = """
    **Insights:**
    - The patterns seen in other visualization, like the year-month one are clearly seen here as well.
    - To highlight again the masive influence of the pandemic in the Madrid traffic accidens series.
    - As another interesting result, the day with the lowest number of accidents was not framed in the pandemic year (2020) but in 2021: Jan 10, 2021, with only one accident.
     But leaving this day out of consideration, the top 30 days with the lowest affluence of traffic accients in Madrid are located in the 2020 lockdown, between the second week of March and the second of May, as was expectectable.
    - And the day with more accidents in MAdrid was April 5, 2019, with 150 accidents.
    """

    #text['analysis']['Select All'] = {}
    #for x in text['analysis']['Barplot'].keys():
    #    text['analysis']['Select All'][x] = text['analysis']['Barplot'][x]
    #for x in text['analysis']['Histogram'].keys():
    #    text['analysis']['Select All'][x] = text['analysis']['Histogram'][x]

    text['analysis']['acc_districts'] = """
    **Insights:**
    - The districts with **more affluence of accidents** are: **Salamanca (7.46%)**, **Puente de Vallecas (7.36%)** and **Chamartín (6.86%)**.
    - The districts with **less affluence of accidents** are: **Vicalvaro (1.73%)**, **Barajas (1.97%)** and **Villa de Vallecas (2.75%)**.
    - The districts with **more affluence of severe accidents** are: **Salamanca (8.64%)**, **Chamartín (7.93%)** and **Puente de Vallecas  (7.11%)**.
    - The districts with **less affluence of severe accidents** are: **Barajas (1.12%)**, **Vicalvaro (1.65%)** and **Moratalaz (2.13%)**.
    - The districts with **more accidents per 1000 inhabitants** are: **Salamanca (51)**, **Chamartín (47.15)** and **Moncloa-Aravaca (45.45%)**.
    - The districts with **less accidents per 1000 inhabitants** are: **Latina (19.85)**, **Villaverde (20.14)**, and **Hortaleza (20.72)**.
    - The districts with **more severe accidents per 1000 inhabitants** are: **Salamanca (1.58)**, **Chamartín (1.46)** and **Retiro (1.21)**.
    - The districts with **less severe accidents per 1000 inhabitants** are: **Carabanchel (0.49)**, **Vicalcaro (0.53)**, and **Fuencarral-El Pardo (0.53)**.

    - There is a concentration of accidents in more central areas, especially in accidents by number of inhabitants.
    - **Salamanca** is the **worst** district in average in terms of affluence of traffic accidents. It is dark purple in the four cases.
    - **Vicalvaro** is the **best** district in average in terms of affluence of traffic accidents. It is white in the four cases.
    - Districts such as Puente de Vallecas, Latina, Carabanchel, Hortaleza and Fuencarral-El Pardo despite having a significant percentage of accidents, due to their large population, are not as relevant in accidents per number of inhabitants.
    - In districts such as Barajas and Moncloa-Aravaca, the opposite occurs, since take a greater importance in accidents per number of inhabitants, possibly due to a smaller population, and in the case of Barajas due to the extra traffic that this district recieved because Madrid airport is located there.
    
    """

    text['analysis']['sev_acc~positive'] = """
    **Insights:**
    - Given that you suffered a traffic accident in Madrid, the probability of being a severe accident is:
       - **4.82%** if there is a positive for grugs or alcohol driver involved.
       - **2.51%** if there is non positive driver involved.           
    - The probability of a severe accident is almost the double when a driver involved tests positive. This seems a significative difference,
       -  Drugs and alcohol have a negative impact on traffic accidents, since they have the effect of making severe accidents more probable. 
    - The average probability of having a severe accident in Madrid, given that an accident occurs, is 2.68%. Compared to this, the probability is higher both if there is a positive driver (almost double) and if there is not (slightly lower).
     >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
    """ 

    text['analysis']['sev_acc~weather'] = """
    **Insights:**
    - In **adverse weather conditions**, the probability of having a severe accident varies, but is **generally lower** than in non-adverse conditions. The lowest probability is with snow **(0.93%)** and hail **(0%)**, while light rain has about **1.75%** and heavy rain **2.5%**.
    - In **non-adverse weather conditions**, the probability of having a severe accident is **higher than average**. For clear conditions, the probability is **3.06%**, and in cloudy conditions, it is almost 4%.
    - These findings indicate that, counterintuitively, clear and cloudy conditions have a higher probability of severe crashes compared to adverse weather conditions such as snow, hail and rain. This could be because drivers are more cautious in adverse conditions, reducing the severity of crashes, whereas in clear or cloudy conditions, confidence may lead to higher speeds and less careful decisions.
     >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
    """

    text['analysis']['sev_acc~age'] = {}
    text['analysis']['sev_acc~age']['old_driver_involved'] = """
    **Insights:**
    - The presence of an older person as a driver not only doesn't increases the probability of havind a severe accident but decreases it.
    - If there is an old driver involved, the probability of the accident of being severe is lower (2.2%) than if there is no one (2.7%), and lower than the average probability of having a severe accident in Madrid (2.68%).
         >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
    """
    text['analysis']['sev_acc~age']['only_old_driver_involved'] = """
    **Insights:**
    - In this case the results are significative and clear. 
    - When **all the drivers involved in the accident are old**, the probability of being a severe accident is **significantly higher (7%) than when not (2.66%)**.
    - A possible explaination of this fact could be that old people is easier to be injured severely, that is, to have high severity physical consequences, and this affect directly to the concept of 'severe accident' taking into account the way in which it was defined.
    - Other possible explanation could be based on the fact that old people have lower reflects that younger, in general. Therefore, when there is a non old driver involved in the acciden, in addition to an old one, the first is able to manege better the sitiation, avoiding this more sevre consequences, but when both drivers are old, the aussence of good reflect in none of the drives causes more fatal results.
     >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
    """
    text['analysis']['sev_acc~age']['young_driver_involved'] = """
    **Insights:**
    - The probability of having a sevre accident is almost the same both if there is a young driver involved (2.5%) or if there is none (2.7%). Moreover, when a young driver is involved, the probability is a bit lower.
     >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
     """
    text['analysis']['sev_acc~age']['only_young_driver_involved'] = """
    **Insights:**
    - In this case, it seems that the fact that all drivers involved are young makes an influence in the possibility of having a severe accident. 
    - Specifically, when all drivers are young, the probability of having a sevre accident is **3.47%**, while when there is none it is **2.64%**.
    - Comparing with the case of only old drivers, we can affirm that when there are only old drivers involved in an accident there is the double of chances of having a severe one than when all them are young.
    >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
     """

    text['analysis']['sev_acc~sex'] = {}
    text['analysis']['sev_acc~sex']['male_driver_involved'] = """
    **Insights:**
    - When there is a male driver involved in the accident the probability of it being severe is 2.8%, that is greater than if there is none (1.92%), as well as higher the average (2.68%) and 
     >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
    """
    text['analysis']['sev_acc~sex']['only_male_driver_involved'] = """
    **Insights:**
    - The probability of having a severe accident when all drivers are male is **3.6%**, while when not it is **1.73%**.
    - When there are **only male drivers involved** in an accident it's almost **3 times more probable** to have a severe accident than when not.
    - Besides, the probability of having a severe accident when **all drivers are male** is **1.35 times higher** than the average probability.
    - On the other hand, when there are **non male drivers** in an accident, there are **1.5 times less chances** of it being severe than in the average case.
     >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
    """
    text['analysis']['sev_acc~sex']['female_driver_involved'] = """
    **Insights:**
    - When there is a **female driver involved** in an accident it is **1.64 times less probable** of being severe than when there is none.
    - In addition, the female drivers involved probability (1.9%) is lower than average one (2.68%).
     >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
    """
    text['analysis']['sev_acc~sex']['only_female_driver_involved'] = """
    **Insights:**
    - The fact of only female drivers are involved in the accident doesn't make a significative impact in the probability of it being severe. It is essentially the same in both scenarios. 
        >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
     """

    text['analysis']['sev_acc~districts'] = """
    **Insights:**
    - The district in which having a severe accident is **most probable**  is **Chamberí (3.13%)**, followed closely by **Salamanca (3.10%), Chamartin (3.09%) and Arganzuela (3.08%)**. All are central districts and above the average probability of 2.68%.
    - Districts with the **lowest probability** of having a severe accident are **Barajas (1.53%), Usera (2.01%), Carabanchel (2.04%) and Moratalaz (2.09%)**. All them are more peripheral and below the average probability.
     >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
    """

    text['analysis']['acc_districts_weather'] = """
    **Insights:**
    - Under **normal weather conditions**, the **Salamanca** district has the **highest percentage of accidents** in Madrid. The district of **Puente de Vallecas** also has a **high percentage**.
    - In presence of **rain**, **Moncloa-Aravaca** takes centre stage, but **Salamanca** is still the one with **more accidents**. But with **heavy rain**, **Moncloa-Aravaca** becomes the **most dominant**.
    - When **snowing**, **Moncloa-Aravaca** is still the district with **more accidents** in proportion, along with **Ciudad Lineal**, and **Hortaleza** becomes the third most relevant.  
    - When **hailing**, **Ciudad Lineal** persist being the **most dominant**, capturing the **25%** of Madrid accidents, being so the district with more accidents under that weather conditions.
     >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
    """

    text['analysis']['phy_sev~age'] = """
    **Insights:**
     - The conclusions in this graph are as expected:
        - **Older people** are **more likely*** to suffer **worse consequences** in the event of an accident. 
        - There are no significant changes between the other two age groups, adults (1.24%) and young people (1.31%).
        - **Older** people account for 3.92%, **3 times more possibilities fo having high severity physical consequencies than young and adult people**. 
        >⚠️ This estimation are affected by the presence of missing values in `positiva_drogras` and `positiva_alcohol`. But, if the sample is representative enough, these numbers would be close to the ones that would be obtained without missing values.
     """

    text['analysis']['num_accidents~poblacion'] = """
    **Insights:**
     - There is a **clear positive relationship** between the **number of accidents** and the **districts population**.
    - Districts with a **larger population** also have a **higher number of accidents**.
    - There are also some **outliers** districts such as Salamanca or Chamartin that have a large number of accidents, but not so large population.
    """

    text['analysis']['num_severe_accident~poblacion'] = """
    **Insights:**
    - In this case, the behavior is similar to the normal accidents, the slope of the straight line is less than the other case, but there is a greater number of outliers, highlighting several districts that have an average population close to 150k but with a number of accidents much higher than expected.
     """

    text['analysis']['num_accidents~num_severe_accident'] = """
    **Insights:**
    - This relationship observed in the graph is as expected, if the **number of accidents increases**, the **number of severe accidents** will **also increase**. There is a perfectly linear relationship, there are no large outliers, perhaps Puente de Vallecas and Caravanchel have a lower number of severe accidents with respect to their non-severe accidents. All the others follow the relationship correctly.
    """
    text['analysis']['num_accidents~intervenciones_policiales_con_detenidos'] = """
    **Insights:**
    - In the case of accidents with respect to police interventions with detainees, there is also a **positive relationship** between these variables. The number of accidents is highly dependent on the number of police interventions. **The higher the number of interventions, the higher the number of accidents**. 
    - District Centro is a **big outlier**, since has many arrests, possibly due to tourists, but there is not as large a number of accidents as would be expected according to the relationship mentioned above.    
    """


    #########################################################################
    # Plot Titles
    #########################################################################

    text['plot_titles']['Barplot'] = {}
    text['plot_titles']['Barplot']['tipo_vehiculo'] = '<b>Distribution of Vehicule Type<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['tipo_persona'] = '<b>Distribution of Involved Person Type<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['rango_edad'] = '<b>Distribution of Age Range<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['sexo'] = '<b>Distribution of Sex<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['lesividad'] = '<b>Distribution of Lesivity<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['positiva_alcohol'] = '<b>Distribution of Positives in Alcohol<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['positiva_droga'] = '<b>Distribution of Positives in Drugs<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['some_death_involved'] = '<b>Distribution of Death Involved<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['distrito'] = '<b>Distribution of Districts<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['tipo_accidente'] = '<b>Distribution of Accidents Type<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['estado_meteorológico'] = '<b>Distribution of Weather Conditions<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['weekday'] = '<b>Distribution of Weekday<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['phy_severity'] = '<b>Distribution of Physical Consequences Severity<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['severe_accident'] = '<b>Distribution of Severe Accidents<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['some_positive_involved'] = '<b>Distribution of Positive Test Involved<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['age_category'] = '<b>Distribution of Age Category<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['male_driver_involved'] = '<b>Distribution of Male Drivers Involved<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['only_male_driver_involved'] = '<b>Distribution of Only Male Drivers Involved<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['female_driver_involved'] = '<b>Distribution of Female Drivers Involved<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['only_female_driver_involved'] = '<b>Distribution of Only Female Drivers Involved<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['young_driver_involved'] = '<b>Distribution of Young Drivers Involved<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['only_young_driver_involved'] = '<b>Distribution of Only Young Drivers Involved<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['old_driver_involved'] = '<b>Distribution of Old Drivers Involved<br> Madrid Traffic Accidents</b>'
    text['plot_titles']['Barplot']['positive_driver_involved'] = '<b>Distribution of Positive Drivers Involved<br> Madrid Traffic Accidents</b>'

    text['plot_titles']['Histogram'] = {}
    text['plot_titles']['Histogram']['num_people_involved'] = '<b>Distribution of Number People Involved<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Histogram']['year'] = '<b>Distribution of Number of Accidents by Year<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Histogram']['quarter'] = '<b>Distribution of Number of Accidents by Quarter<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Histogram']['month'] = '<b>Distribution of Number of Accidents by Month<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Histogram']['week'] = '<b>Distribution of Number of Accidents by Week<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Histogram']['day'] = '<b>Distribution of Number of Accidents by Day<br> Madrid Traffic Accidents (2019-2024)</b>'

    text['plot_titles']['Lineplot'] = {}
    text['plot_titles']['Lineplot']['num_people_involved'] = '<b>Distribution of Number People Involved<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['year'] = '<b>Distribution of Number of Accidents by Year<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['quarter'] = '<b>Distribution of Number of Accidents by Quarter<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['month'] = '<b>Distribution of Number of Accidents by Month<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['week'] = '<b>Distribution of Number of Accidents by Week<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['day'] = '<b>Distribution of Number of Accidents by Day<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['hour'] = '<b>Distribution of Number of Accidents by Hour<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['weekday'] = '<b>Distribution of Number of Accidents by Weekday<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['year-quarter'] = '<b>Distribution of Number of Accidents by Year-Quarter<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['year-month'] = '<b>Distribution of Number of Accidents by Year-Month<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['year-month-day'] = '<b>Distribution of Number of Accidents by Year-Month-Day<br> Madrid Traffic Accidents (2019-2024)</b>'
    text['plot_titles']['Lineplot']['multiplot'] = '<b>Distribution of Number of Accidents by Periods<br> Madrid Traffic Accidents (2019-2024)</b>'
   
    text['plot_titles']['acc_districts'] = {}  
    text['plot_titles']['acc_districts']['accidents'] = 'Accidents'
    text['plot_titles']['acc_districts']['severe_accidents'] = 'Severe Accidents'
    text['plot_titles']['acc_districts']['acc_1000_hab'] = 'Accidents per 1000 inhab.'
    text['plot_titles']['acc_districts']['severe_acc_1000_hab'] = 'Severe Accidents per 1000 inhab.'

    text['hue_titles']['acc_districts'] = {}
    text['hue_titles']['acc_districts']['accidents'] = 'Perc. acc.'
    text['hue_titles']['acc_districts']['severe_accidents'] = 'Perc. severe acc.'
    text['hue_titles']['acc_districts']['acc_1000_hab'] = 'Acc. per 1k inhab.'
    text['hue_titles']['acc_districts']['severe_acc_1000_hab'] = 'Severe acc. per 1k inhab.'

    text['plot_titles']['more_districts'] = {}

    return text