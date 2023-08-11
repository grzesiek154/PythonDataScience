-- couny duplicate values for a particular column
DuplicatesCount = COUNTROWS(Table) - COUNTROWS(DISTINCT(Table))