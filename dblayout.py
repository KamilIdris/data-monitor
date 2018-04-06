# -*- coding: utf-8 -*-
"""
DB Layouts for the data acquired
Each row should be layed out as follows:-

ADDRESS    VAR_NAME     TYPE
-------    ---------    ------
40         PRESSURE     REAL
                        INT
                        BOOL


Updated 30th March 2018 by Kamil
"""
__unimplemented= [24, 40, 41, 43]

db103 = {
        'dbnum': 103,
        'layout': """
            100    Tilt    REAL
            102    Roll    REAL

            116    VMT-Station      REAL  

            150    Y-value_CH       REAL
            152    X-value_CH       REAL
            154    Y-value_Target   REAL
            156    X-value_Target   REAL
            """,
        'size': 156+2,
        'numrows': 7,
        'layoutoffset': 100,
        'dboffset': 100
            }

db218 = {
        'dbnum': 218,
        'layout': """
            300    TailskinGreaseF1.1_NoOfStroke    INT
            301    TailskinGreaseF1.2_NoOfStroke    INT
            302    TailskinGreaseF1.3_NoOfStroke    INT
            303    TailskinGreaseF1.4_NoOfStroke    INT
            304    TailskinGreaseF1.5_NoOfStroke    INT
            305    TailskinGreaseF1.6_NoOfStroke    INT
            306    TailskinGreaseR1.1_NoOfStroke    INT
            307    TailskinGreaseR1.2_NoOfStroke    INT
            308    TailskinGreaseR1.3_NoOfStroke    INT
            309    TailskinGreaseR1.4_NoOfStroke    INT
            310    TailskinGreaseR1.5_NoOfStroke    INT
            311    TailskinGreaseR1.6_NoOfStroke    INT
        
            400    TailskinGreaseF1.1_Pressure     REAL
            402    TailskinGreaseF1.2_Pressure     REAL
            404    TailskinGreaseF1.3_Pressure     REAL
            406    TailskinGreaseF1.4_Pressure     REAL
            408    TailskinGreaseF1.5_Pressure     REAL
            410    TailskinGreaseF1.6_Pressure     REAL
            
            434    TailskinGreaseR1.1_Pressure     REAL
            436    TailskinGreaseR1.2_Pressure     REAL
            438    TailskinGreaseR1.3_Pressure     REAL
            440    TailskinGreaseR1.4_Pressure     REAL
            442    TailskinGreaseR1.5_Pressure     REAL
            444    TailskinGreaseR1.6_Pressure     REAL
            
            550    TailskinGreaseManual_NoOfStroke     INT
            551    TailskinGreasevalve_Active          INT
            """,
        'size': 551+1,
        'numrows': 26,
        'layoutoffset': 300,
        'dboffset': 300
            }
 
db323 = {
        'dbnum': 323,
        'layout': """
            0.0    GroutL1_Active    BOOL
            0.1    GroutL2_Active    BOOL
            0.2    GroutL3_Active    BOOL
            0.3    GroutL4_Active    BOOL
            
            100.0    GroutL1_PressureCutoff     BOOL    
            100.1    GroutL2_PressureCutoff     BOOL
            100.2    GroutL3_PressureCutoff     BOOL
            100.3    GroutL4_PressureCutoff     BOOL
            
            300    TargetMixProportionCompB     REAL
            
            350    CompA1_Flow     REAL
            352    CompA2_Flow     REAL
            354    CompA3_Flow     REAL
            356    CompA4_Flow     REAL
            
            400    CompB1_Flow     REAL
            402    CompB2_Flow     REAL
            404    CompB3_Flow     REAL
            406    CompB4_Flow     REAL
            
            450    CompA1_Pressure     REAL
            452    CompA2_Pressure     REAL
            454    CompA3_Pressure     REAL
            456    CompA4_Pressure     REAL
            
            610    CompA_TotalQuantity     REAL
            612    CompB_TotalQuantity     REAL
            
            622    CompA_TargetQuantity     REAL
            
            626    Grout_Volume     REAL
            
            750    CompA1_Quantity     REAL
            752    CompA2_Quantity     REAL
            754    CompA3_Quantity     REAL
            756    CompA4_Quantity     REAL
            
            800    CompB1_Quantity     REAL
            802    CompB2_Quantity     REAL
            804    CompB3_Quantity     REAL
            806    CompB4_Quantity     REAL
            
            900    CompB1_Pressure     REAL
            902    CompB2_Pressure     REAL
            904    CompB3_Pressure     REAL
            906    CompB4_Pressure     REAL
            """,
        'size': 906+2,
        'numrows': 37,
        'layoutoffset': 0,
        'dboffset': 0
            }