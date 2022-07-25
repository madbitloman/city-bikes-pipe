## city-bikes-pipe 
Scripts ready for ETL/BI data wrangling on Toronto city bikes open data 

URL's to acces open data:
  - stations status : https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_status
  - stations information: https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_information

## Stack Used 
|                     | Version           |
|---------------------|------------------------------|
| Python              | 3.7                          |
| AWS                 | EC2 t3.medium                |
| PostgreSQL          | 14                           |
| Tableau             | 10                           |
| Airflow             | 2.0                          |

Currently we collect data on the hourly basis in PostgreSQL and next steps will be to use AWS Lambda Functions/Architecture to adjust for the scalability. On the import data is stored as CSV in the TS partition manner that could be ajusted in the future for AWS S3 use. Next we export the data to PostgreSQL and generate a simple PDF report with the metrics of interest. 
![Screen Shot 2022-07-24 at 9 20 24 PM](https://user-images.githubusercontent.com/9925727/180692308-5033d44b-c454-405e-b694-46d2c37e8b70.png)

Integration can be done further with any BI tools aka Tableau (preference) or Power BI to harvest insights
![Screen Shot 2022-07-24 at 11 17 40 PM](https://user-images.githubusercontent.com/9925727/180692525-4101958a-ee3d-4c2a-bfcc-ee5cbc60fed4.png)
