library(swat)

cashost <- "sas-cas-server-default-client"
casport <- 5570                               # binary port inside Viya pods
access_token <- Sys.getenv("ACCESS_TOKEN")    # Azure Marketplace sets this for you

conn <- CAS(cashost, casport, password = access_token)

# Take a look at the connection/session
conn
cas.builtins.serverStatus(conn)               # server status / nodes, etc.
class(conn)

abt <- cas.builtins.about(conn)
abt$About[["Viya Version"]]

cas.table.fileInfo(conn, caslib = "casuser")

cars_df <- read.csv("data/courses/CASL/data/my_data/cars.csv")

# Upload to CAS as an in-memory table
invisible(
    as.casTable(conn, cars_df,
            casOut = list(name = "cars",
                          caslib = "casuser",
                          replace = TRUE))
)

# Verify the in-memory table exists
cas.table.tableInfo(conn, caslib = "casuser")

castbl <- defCasTable(conn, 'cars')

print(class(castbl))

df <- head(to.casDataFrame(castbl))

print(df)


