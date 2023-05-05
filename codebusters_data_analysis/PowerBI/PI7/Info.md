Query for created tickets

Created

project = CI AND  issuetype  in ("Expense Delivery") AND "Type of Request" in ("Incident Request (IR)", "Service Request (SR)") AND createdDate >= 2023-03-01 AND createdDate < 2023-06-01 AND labels != "Partners" AND labels != "Internal" and "Case Number/s" is not EMPTY

jql=project%20%3D%20CI%20AND%20%20issuetype%20%20in%20("Expense%20Delivery")%20AND%20"Type%20of%20Request"%20in%20("Incident%20Request%20(IR)"%2C%20"Service%20Request%20(SR)")%20AND%20createdDate%20>%3D%202023-01-01%20AND%20createdDate%20<%202023-06-01%20AND%20labels%20!%3D%20"Partners"%20AND%20labels%20!%3D%20"Internal"%20and%20"Case%20Number%2Fs"%20is%20not%20EMPTY



Resolved

project = CI AND  issuetype  in ("Expense Delivery") AND "Type of Request" in ("Incident Request (IR)", "Service Request (SR)") AND resolved  >= 2023-03-01 AND resolved < 2023-06-01



project = CI AND  issuetype  in ("Expense Delivery") AND "Type of Request" in ("Incident Request (IR)",  "Service Request (SR)") AND resolved  >= 2023-04-17 AND resolved < 2023-06-01 AND labels != "Partners" AND labels != "Internal" and "Case Number/s" is not EMPTY



jql=project%20%3D%20CI%20AND%20%20issuetype%20%20in%20("Expense%20Delivery")%20AND%20"Type%20of%20Request"%20in%20("Incident%20Request%20(IR)"%2C%20"Service%20Request%20(SR)")%20AND%20createdDate%20>%3D%202023-03-01%20AND%20createdDate%20<%202023-06-01



Advance Editor

let
    Source = Json.Document(Web.Contents("https://jira.ifao.net/rest/api/2/search?" & "jql=project%20%3D%20CI%20AND%20%20issuetype%20%20in%20(""Expense%20Delivery"")%20AND%20""Type%20of%20Request""%20in%20(""Incident%20Request%20(IR)""%2C%20""Service%20Request%20(SR)"")%20AND%20createdDate%20>%3D%202023-03-01%20AND%20createdDate%20<%202023-06-01" & "&maxResults=3000")),
       #"Converted to Table" = Table.FromRecords({Source}),
    #"Expanded issues" = Table.ExpandListColumn(#"Converted to Table", "issues"),
    #"Expanded issues1" = Table.ExpandRecordColumn(#"Expanded issues", "issues", {"expand", "id", "self", "key", "fields"}, {"issues.expand", "issues.id", "issues.self", "issues.key", "issues.fields"}),
    #"Expanded issues.fields" = Table.ExpandRecordColumn(#"Expanded issues1", "issues.fields", {"resolution", "labels", "assignee", "reporter", "issuetype", "project", "resolutiondate", "description", "summary", "customfield_10004", "duedate", "customfield_14839", "customfield_14702", "status", "creator", "customfield_14125", "customfield_10304", "customfield_10305", "created"}, {"issues.fields.resolution", "issues.fields.labels", "issues.fields.assignee", "issues.fields.reporter", "issues.fields.issuetype", "issues.fields.project", "issues.fields.resolutiondate", "issues.fields.description", "issues.fields.summary", "issues.fields.customfield_10004", "issues.fields.duedate", "issues.fields.customfield_14839", "issues.fields.customfield_14702", "issues.fields.status", "issues.fields.creator", "issues.fields.customfield_14125", "issues.fields.customfield_10304", "issues.fields.customfield_10305", "issues.fields.created"}),
    #"Removed Columns" = Table.RemoveColumns(#"Expanded issues.fields",{"expand", "startAt", "maxResults", "total", "issues.expand", "issues.id", "issues.self"}),
    #"Expanded issues.fields.customfield_10305" = Table.ExpandListColumn(#"Removed Columns", "issues.fields.customfield_10305"),
    #"Expanded issues.fields.customfield_1" = Table.ExpandRecordColumn(#"Expanded issues.fields.customfield_10305", "issues.fields.customfield_10305", {"value"}, {"issues.fields.customfield_10305.value"}),
    #"Renamed Columns" = Table.RenameColumns(#"Expanded issues.fields.customfield_1",{{"issues.fields.customfield_10305.value", "CustomerName"}, {"issues.key", "ticket_number"}, {"issues.fields.labels", "labels"}, {"issues.fields.assignee", "assignee"}, {"issues.fields.reporter", "reporter"}, {"issues.fields.issuetype", "issuetype"}}),
    #"Expanded issuetype" = Table.ExpandRecordColumn(#"Renamed Columns", "issuetype", {"name"}, {"issuetype.name"}),
    #"Renamed Columns1" = Table.RenameColumns(#"Expanded issuetype",{{"issuetype.name", "issue_type"}, {"issues.fields.description", "description"}, {"issues.fields.summary", "summary"}}),
    #"Expanded reporter" = Table.ExpandRecordColumn(#"Renamed Columns1", "reporter", {"displayName"}, {"reporter.displayName"}),
    #"Removed Columns1" = Table.RemoveColumns(#"Expanded reporter",{"issues.fields.project", "description", "summary", "issues.fields.customfield_10004"}),
    #"Renamed Columns2" = Table.RenameColumns(#"Removed Columns1",{{"issues.fields.customfield_14839", "case_creation_date"}}),
    #"Expanded issues.fields.status" = Table.ExpandRecordColumn(#"Renamed Columns2", "issues.fields.status", {"name"}, {"issues.fields.status.name"}),
    #"Renamed Columns3" = Table.RenameColumns(#"Expanded issues.fields.status",{{"issues.fields.status.name", "current_status"}, {"reporter.displayName", "CI_reporter"}}),
    #"Removed Columns2" = Table.RemoveColumns(#"Renamed Columns3",{"issues.fields.creator"}),
    #"Expanded issues.fields.customfield_14125" = Table.ExpandRecordColumn(#"Removed Columns2", "issues.fields.customfield_14125", {"value"}, {"issues.fields.customfield_14125.value"}),
    #"Renamed Columns4" = Table.RenameColumns(#"Expanded issues.fields.customfield_14125",{{"issues.fields.customfield_14125.value", "type_of_request"}, {"issues.fields.customfield_10304", "oneview_case_number"}, {"CustomerName", "customer_name"}, {"issues.fields.resolutiondate", "resolution_date"}, {"issues.fields.duedate", "due_date"}}),
    #"Removed Columns3" = Table.RemoveColumns(#"Renamed Columns4",{"issues.fields.customfield_14702"}),
    #"Renamed Columns5" = Table.RenameColumns(#"Removed Columns3",{{"case_creation_date", "oneview_case_creation_date"}, {"issues.fields.created", "create_date"}}),
    #"Added Custom" = Table.AddColumn(#"Renamed Columns5", "create_date_custom", each Text.Range([create_date], 0, 10)),
    #"Added Custom1" = Table.AddColumn(#"Added Custom", "resolution_date_custom", each Text.Range([resolution_date], 0, 10)),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom1",{{"resolution_date_custom", type date}, {"create_date_custom", type date}}),
    #"Filtered Rows" = Table.SelectRows(#"Changed Type", each ([type_of_request] <> "Project")),
    #"Appended Query" = Table.Combine({#"Filtered Rows", #"Filtered Rows"}),
    #"Added Conditional Column" = Table.AddColumn(#"Appended Query", "Is_done", each if [current_status] = "Done " then "Completed" else if [current_status] = "Communicate" then "Completed" else if [current_status] = "Review" then "Not started" else "In progress")
in
    #"Added Conditional Column"