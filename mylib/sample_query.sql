SELECT 
    t1.group,
    AVG(t1.spi) as avg_soccer_power_in_609,
    AVG(t2.spi) as avg_soccer_power_in_613
FROM 
    wc609_delta t1
JOIN 
    wc613_delta t2 
    ON t1.id = t2.id 
GROUP BY 
    t1.group, t2.group
ORDER BY 
    avg_soccer_power_in_609 DESC;