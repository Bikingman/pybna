DROP TABLE IF EXISTS {workspace_schema}.{workspace_table};
CREATE TABLE {workspace_schema}.{workspace_table} AS (
    SELECT
        COALESCE(hs.block_id,ls.block_id) AS block_id,
        hs.total AS hs,
        ls.total AS ls,
        NULL::FLOAT AS score
    FROM
        pg_temp.high_stress
        FULL OUTER JOIN pg_temp.low_stress
            ON high_stress.block_id = low_stress.block_id
);

CREATE INDEX {index} ON {workspace_schema}.{workspace_table} (block_id);
ANALYZE {workspace_schema}.{workspace_table};
