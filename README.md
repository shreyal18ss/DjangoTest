The file attached  “weather data” contains one month of weather data from two locations: location1 and location2. The data timestamp is at UTC. It has record for temperature, solar radiation, wind speed, wind direction and relative humidity. All parameters are in SI unit system.
The tasks are as follows:
1.	Upload this data into local MySQL DB with an efficient ER architecture keeping in mind about handling most frequent query on timestamp and location. Share the ER diagram for same. Avoid duplicate insertion for same location and timestamp.
2.	Write this into Django models and migrate this into MySQL DB. --> DB Details to be uplated in settings.py
3.	Share the python script to upload this data into DB. You may check pangres for efficient handling of insert or update. -->  upload_weather_data.py
4.	Write an API to bulk create rows where user can post excel through UI. --> 127.0.0.1:8000/uploadexcel/upload (Excel available in this folder)
5.	Make DataGrid in UI to show uploaded data in database, create API to get data too --> 127.0.0.1:8000/uploadexcel/datagrid
