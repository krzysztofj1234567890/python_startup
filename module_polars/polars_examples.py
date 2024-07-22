import numpy as np
import polars as pl

num_rows = 5000
rng = np.random.default_rng(seed=7)

buildings_data = {
    "sqft": rng.exponential(scale=1000, size=num_rows),
    "price": rng.exponential(scale=100_000, size=num_rows),
    "year": rng.integers(low=1995, high=2023, size=num_rows),
    "building_type": rng.choice(["A", "B", "C"], size=num_rows),
}
buildings = pl.DataFrame(buildings_data)

# show random data
print( buildings )

# show schema
print( buildings.schema )

# stats
print( buildings.describe() )

# polars data frame
pdf = pl.DataFrame(buildings_data)

print( "select" )
print( pdf.select(pl.col("sqft").sort() /100 ) )

print( "filter" )
print( pdf.filter(pl.col("year") > 2015 ) )

print( "group by" )
print( pdf.group_by("building_type").agg(
    [
        pl.mean("sqft").alias("mean_sqft"),
        pl.median("year").alias("median_year"),
        pl.count(),
    ]
))

print( "lazy" )
buildings_lazy = pl.LazyFrame( buildings_data  )
lazy_query = (
    buildings_lazy.with_columns(
        (pl.col("price") / pl.col("sqft")).alias("price_per_sqft"))
        .filter(pl.col("price_per_sqft") > 100)
        .filter(pl.col("year") < 2010)
)
print( lazy_query.explain())
