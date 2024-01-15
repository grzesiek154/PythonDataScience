Custom Resolution Date = 
  IF (ISBLANK('Features 23_4'[Resolution Date]),
    SWITCH(
            'Features 23_4'[Actual Iteration], 
            "PI 23.4-1",DATE(2023, 10, 13),
            "PI 23.4-2", DATE(2023, 11, 03),
            "PI 23.4-3", DATE(2023, 11, 24),
            "PI 23.4 IP", DATE(2023, 12, 15)
        ),
        'Features 23_4'[Resolution Date]
  )