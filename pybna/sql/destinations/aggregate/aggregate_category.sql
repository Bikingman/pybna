DROP TABLE IF EXISTS pg_temp.tmp_scoreables;
CREATE TEMP TABLE pg_temp.tmp_scoreables AS (
    SELECT
        scores.{blocks_id_col}::blocks_id_type AS id,
        scores.{category_score_col} AS score,
        blocks.{blocks_population_col} AS pop
    FROM
        {scores_schema}.{scores_table} scores,
        {blocks_schema}.{blocks_table} blocks
    WHERE
        scores.{blocks_id_col} = blocks.{blocks_id_col}
        AND scores.{category_score_col} IS NOT NULL
        AND EXISTS (
            SELECT 1
            FROM {boundary_schema}.{boundary_table} bound
            WHERE ST_Intersects(bound.geom,b2.geom)
        )
);


DROP TABLE IF EXISTS pg_temp.tmp_ratios;
CREATE TEMP TABLE pg_temp.tmp_ratios AS (
    SELECT
        tmp_scoreables.id,
        tmp_scoreables.score,
        tmp_scoreables.pop::FLOAT/agg.pop AS ratio
    FROM
        tmp_scoreables,
        (
            SELECT SUM(pop) AS pop
            FROM tmp_scoreables
        ) agg
);


INSERT INTO {aggregate_schema}.{aggregate_table} (category, score)
SELECT
    {category_name},
    SUM(ratio*score)
FROM pg_temp.tmp_ratios
;
