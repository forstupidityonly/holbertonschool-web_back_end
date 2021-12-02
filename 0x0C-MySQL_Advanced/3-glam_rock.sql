-- find all glan rock and rank by longevity

SELECT band_name, IFNULL(split, year(CURDATE())) - formed as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
