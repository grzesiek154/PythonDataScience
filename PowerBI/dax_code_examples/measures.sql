PI6.1_resolved = CALCULATE(
    COUNTROWS('all_tickets_appended'),
    all_tickets_appended[Resolved] >= DATE(2022,12,19),
    all_tickets_appended[Resolved] <= DATE(2023,01,08)
)

PI6.1_created = CALCULATE(
    COUNTROWS('all_tickets_appended'),
    all_tickets_appended[Created] >= DATE(2022,12,19),
    all_tickets_appended[Created] <= DATE(2023,01,08)
)

IR_percentage = ROUND(DIVIDE(
    CALCULATE(
        COUNTROWS(all_tickets_appended), all_tickets_appended[type_of_reuqest_id] == 1
        ),
    CALCULATE(
        COUNTROWS(all_tickets_appended), ALL(all_tickets_appended)
        )
    )
,2) * 100


-- Calculate the sum percentage of SP for a particular assigment for total developer story points usded

                            ROUND(DIVIDE(
                                Iteration1[SP - Planning],
                                CALCULATE(
                                    SUM(Iteration1[SP - Planning]),
                                    ALLEXCEPT(Iteration1, Iteration1[Assignee])
                                )) * 100, 0)