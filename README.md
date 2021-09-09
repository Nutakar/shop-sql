# :purse: :credit_card: shop-sql
Project for analyzing customers' purchases data for shop
## :rocket: How to launch 
The only thing you need to launch the app is Docker:
```bash
docker-compose up -d
```
The preceding command build images if they don't exist and starts the containers.
## :money_with_wings: Queries 
To make each query you need to uncomment corresponding function and run in terminal:
```bash
python3 queries.py
```
A) Average sum for each month:
  - users from 18 to 25 years inclusive: *average_per_month_18_25()*
  - users from 26 to 35 years inclusive: *average_per_month_26_35()*  
  
B) A month in the year with the biggest earnings from users age 35+:
  - *max_money_month_35()*  
  
C) A product with the biggest earnings share in a year:
  - *max_money_share_item()*
