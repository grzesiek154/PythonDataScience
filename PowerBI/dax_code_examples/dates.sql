-- Creating a Hierarchical Date Table
Year = Date.Year([Date])
Quarter = "Q" & Text.From(Date.QuarterOfYear([Date]))
Month = Date.ToText([Date], "MMMM")
Day = Date.Day([Date])


-- Creating a Date Table with Fiscal Year
-- This formula considers a fiscal year starting from July. Adjust the logic based on your organization's fiscal year start month.
FiscalYear = if Date.Month([Date]) >= 7 then Date.Year([Date]) + 1 else Date.Year([Date])


-- Creating a Basic Date Table
DateTable = List.Dates(#date(2022, 1, 1), Duration.Days(#date(2022, 12, 31) - #date(2022, 1, 1)), #duration(1, 0, 0, 0))


-- Date table from mix and max date value of a given column
Dim_Date = CALENDAR(MIN(all_tickets_appended[Resolved]), MAX(all_tickets_appended[Resolved]))


-- https://www.youtube.com/watch?v=fKygF7VEJnQ
Date Periods = 
UNION(
    ADDCOLUMNS(
        CALENDAR(DATE(2022, 12, 19), DATE(2023, 1, 6)),
        "Type", "PI#6.1",
        "Order", 1
    ),
    ADDCOLUMNS(
        CALENDAR(DATE(2023, 1, 9), DATE(2023, 1, 27)),
        "Type", "PI#6.2",
        "Order", 2
    ),
    ADDCOLUMNS(
        CALENDAR(DATE(2023, 1, 30), DATE(2023, 2, 17)),
        "Type", "PI#6.3",
        "Order", 3
    ),
        ADDCOLUMNS(
        CALENDAR(DATE(2023, 2, 20), DATE(2023, 3, 10)),
        "Type", "PI#6.4",
        "Order", 4
    )
)



Dim_Date_2 = GENERATE(

    CALENDAR(MIN(all_tickets_appended[Resolved]), MAX(all_tickets_appended[Resolved])),
    VAR CurrentDate = [Date]
    VAR Year = YEAR(CurrentDate)
    VAR Month = MONTH(CurrentDate)
    VAR Quarter = CONCATENATE("Q", FORMAT(CurrentDate, "Q"))
    VAR ProgramIncrement = // Calculate the Program Increment based on the date
        SWITCH(
            TRUE(),
            CurrentDate >= DATE(2022, 12, 19) && CurrentDate <= DATE(2023, 3, 24), "PI6",
            CurrentDate >= DATE(2023, 3, 27) && CurrentDate <= DATE(2023, 6, 16), "PI7",
            // Add more conditions for other Program Increments
            BLANK()
        )
    VAR Iteration = // Calculate the Iteration based on the date
        SWITCH(
            TRUE(),
            CurrentDate >= DATE(2020, 1, 1) && CurrentDate <= DATE(2020, 3, 31), "Iteration 1",
            CurrentDate >= DATE(2020, 4, 1) && CurrentDate <= DATE(2020, 6, 30), "Iteration 2",
            // Add more conditions for other Iterations
            BLANK()
        )
    RETURN
        ROW(
            "Date", CurrentDate,
            "Year", Year,
            "Month", Month,
            "Quarter", Quarter,
            "Program Increment", ProgramIncrement,
            "Iteration", Iteration
        )
) 


