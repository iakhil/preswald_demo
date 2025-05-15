from preswald import connect, get_df, table

connect()  # Initialize connection to preswald.toml data sources
df = get_df("1000_ml_jobs_us.csv")  # Load data

from preswald import query

job_title_sql = "SELECT job_title, count(*) as num_openings from ml_jobs_csv group by job_title order by num_openings desc"
results = query(job_title_sql, "ml_jobs_csv")



from preswald import table, text
text("# ML Jobs Analyses")

text("### Number of openings by job title")

table(results, title="All companies")

from preswald import plotly
import plotly.express as px


location_sql = "SELECT company_address_locality, count(distinct company_name) as company_count from ml_jobs_csv group by company_address_locality order by company_count desc"

location_results = query(location_sql, "ml_jobs_csv")



fig = px.bar(
    location_results.head(15),  # Top 15 locations
    x="company_address_locality",
    y="company_count",
    title="Companies with ML Jobs by Location",
    labels={
        "company_address_locality": "Location",
        "company_count": "Number of Companies"
    }
)

# Improve readability
fig.update_layout(
    xaxis_tickangle=45,  # Angle the x-axis labels for better readability
    height=500,
    width=800
)

# Display the plot
plotly(fig)


# Pie chart for number of openings by company

company_sql = "select company_name, count(*) as num_openings from ml_jobs_csv group by company_name order by num_openings desc"


company_data = query(company_sql, "ml_jobs_csv")

# Pie chart with the top 10 companies
fig = px.pie(
    company_data.head(10),
    values="num_openings",
    names="company_name",
    title="Top 10 Companies by ML Job Openings"
)

# Display the pie chart
plotly(fig)


