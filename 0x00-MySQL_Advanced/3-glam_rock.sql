-- data
SELECT
    band_name AS band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan
