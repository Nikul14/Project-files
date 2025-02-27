show databases;
use financial_analysis;
select*from financial_data;
show tables;
desc financial_data;

-- data cleaning Remove NULLs Without Deleting Rows
SELECT CONCAT('UPDATE financial_data SET ', 
       GROUP_CONCAT(CONCAT(column_name, ' = COALESCE(', column_name, ', 0)') SEPARATOR ', '), ';')
FROM information_schema.columns
WHERE table_name = 'financial_data';

 -- use backtick` ` to remove extra space from columns and is null to see if there any null
SELECT *  
FROM financial_data 
WHERE `Revenue` IS NULL 
   OR `Net Income` IS NULL 
   OR `Market Cap(in B USD)` IS NULL  
LIMIT 1000;

update financial_data
set Revenue=0
where Revenue is null;
-- Standardize Market Cap Format 
update financial_data
set `Market Cap(in B USD)`=replace(`Market Cap(in B USD)`,"B","");

-- For all columns with text, generate a bulk update query:

SELECT CONCAT('UPDATE financial_data SET `', COLUMN_NAME, '` = TRIM(`', COLUMN_NAME, '`);')
FROM information_schema.columns
WHERE table_name = 'financial_data'
AND DATA_TYPE IN ('char', 'varchar', 'text');

-- to see DUPLICATE
 with CTE as(
 select*,
 row_number() over (partition by `Year`,`Company`order by `Year`,`Company` desc) as row_num
 from financial_data)
 select*from CTE 
 where row_num>1;
 -- to remove 
 
 with cte as(
 select*,row_number() over (partition by `Year`,`Company`) as row_num
 from financial_data)
 delete from financial_data
 where (`Year`,`Company`)in(
 select `Year`,Company from cte where row_num >1);

-- MODIFEY /ALTER COLUMN
Alter table financial_data 
modify column Revenue decimal(15,2);

 -- Perform Financial Analysis in SQL
-- Top 5 Companies by Revenue
 show columns from financial_data;
select  Company,max(Revenue) as max_Revenue
from financial_data
group by company,Revenue
order by max_Revenue desc
limit 5;

-- Profitability Analysis (Net Profit Margin)
select `Company`,max(`Net Income`/ `Revenue`)*100 as net_profit_margin
from financial_data
group by `Company`
order by net_profit_margin desc
limit 5;
show columns from financial_data;

SELECT `Company`, MAX(`Debt/Equity Ratio`) AS Max_Debt_Equity_Ratio
FROM financial_data
GROUP BY `Company`
ORDER BY Max_Debt_Equity_Ratio DESC;
select*from financial_data;
SELECT `Company`, `Revenue`, `Net Income`, `Debt/Equity Ratio` 
FROM financial_data;











