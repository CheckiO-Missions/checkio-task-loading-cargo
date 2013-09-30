"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input":[10, 10],
            "answer":0,
            "explanation":[
                [10],
                [10]
            ]
        },
        {
            "input":[10],
            "answer":10,
            "explanation":[
                [10],
                []
            ]
        },
        {
            "input":[5, 8, 13, 27, 14],
            "answer":3,
            "explanation":[
                [8, 13, 14],
                [5, 27]
            ]
        },
        {
            "input":[5, 5, 6, 5],
            "answer":1,
            "explanation":[
                [6, 5],
                [5, 5]
            ]
        },
        {
            "input":[12, 30, 30, 32, 42, 49],
            "answer":9,
            "explanation":[
                [30, 30, 42],
                [12, 32, 49]
            ]
        },
        {
            "input":[1, 1, 1, 3],
            "answer":0,
            "explanation":[
                [1, 1, 1],
                [3]
            ]
        },
        {
            "input":[9, 9, 7, 6, 5],
            "answer":0,
            "explanation":[
                [7, 6, 5],
                [9, 9]
            ]
        },
        {
            "input":[5, 10, 5, 10, 1],
            "answer":1,
            "explanation":[
                [5, 10, 1],
                [5, 10]
            ]
        },
        {
            "input":[30, 30, 30, 30, 30, 30, 30, 30],
            "answer":0,
            "explanation":[
                [30, 30, 30, 30],
                [30, 30, 30, 30]
            ]
        },
        {
            "input":[30, 30, 30, 30, 30, 30, 30],
            "answer":30,
            "explanation":[
                [30, 30, 30, 30],
                [30, 30, 30]
            ]
        },
        {
            "input":[33, 5, 10, 19, 35, 16, 10],
            "answer":0,
            "explanation":[
                [33, 5, 16, 10],
                [10, 19, 35]
            ]
        },
        {
            "input":[25, 43, 8, 8, 31, 1, 17, 7, 3],
            "answer":1,
            "explanation":[
                [8, 8, 31, 1, 17, 7],
                [25, 43, 3]
            ]
        },
        {
            "input":[4, 24],
            "answer":20,
            "explanation":[
                [24],
                [4]
            ]
        },
        {
            "input":[11, 19, 28, 21, 20, 43, 47, 7, 17],
            "answer":1,
            "explanation":[
                [11, 19, 28, 21, 20, 7],
                [43, 47, 17]
            ]
        },
        {
            "input":[10, 1, 6, 18, 47, 36, 38],
            "answer":4,
            "explanation":[
                [10, 1, 18, 47],
                [6, 36, 38]
            ]
        },
        {
            "input":[17, 7, 41, 22, 20, 4, 12],
            "answer":1,
            "explanation":[
                [17, 7, 22, 4, 12],
                [41, 20]
            ]
        },
        {
            "input":[33, 38, 25, 5, 40, 46, 7, 27],
            "answer":1,
            "explanation":[
                [25, 5, 46, 7, 27],
                [33, 38, 40]
            ]
        },
        {
            "input":[43, 14, 19, 24, 23, 16, 46],
            "answer":1,
            "explanation":[
                [43, 14, 19, 16],
                [24, 23, 46]
            ]
        },
        {
            "input":[42, 30],
            "answer":12,
            "explanation":[
                [30],
                [42]
            ]
        },
        {
            "input":[20, 6, 5],
            "answer":9,
            "explanation":[
                [6, 5],
                [20]
            ]
        },
        {
            "input":[49],
            "answer":49,
            "explanation":[
                [49],
                []
            ]
        }
    ],
    "Extra": [
        {
            "input":[1, 1, 1, 1],
            "answer":0,
            "explanation":[
                [1, 1],
                [1, 1]
            ]
        },
        {
            "input":[2, 2, 2, 2],
            "answer":0,
            "explanation":[
                [2, 2],
                [2, 2]
            ]
        },
        {
            "input":[3, 3, 3, 3],
            "answer":0,
            "explanation":[
                [3, 3],
                [3, 3]
            ]
        },
        {
            "input":[25, 21, 7, 16, 13, 38, 25],
            "answer":1,
            "explanation":[
                [25, 7, 16, 25],
                [21, 13, 38]
            ]
        },
        {
            "input":[1, 7, 23, 9, 37, 15],
            "answer":0,
            "explanation":[
                [1, 7, 23, 15],
                [9, 37]
            ]
        },
        {
            "input":[20, 1, 49, 18, 21, 48, 17, 35, 23, 50],
            "answer":0,
            "explanation":[
                [1, 49, 18, 21, 17, 35],
                [20, 48, 23, 50]
            ]
        },
        {
            "input":[43, 43],
            "answer":0,
            "explanation":[
                [43],
                [43]
            ]
        },
        {
            "input":[23, 26, 37, 5, 38, 37, 3, 28, 6, 23],
            "answer":0,
            "explanation":[
                [37, 5, 37, 28, 6],
                [23, 26, 38, 3, 23]
            ]
        },
        {
            "input":[36, 37, 50, 42],
            "answer":7,
            "explanation":[
                [37, 42],
                [36, 50]
            ]
        },
        {
            "input":[41],
            "answer":41,
            "explanation":[
                [41],
                []
            ]
        },
        {
            "input":[30, 10, 45, 35, 20, 12, 17],
            "answer":1,
            "explanation":[
                [35, 20, 12, 17],
                [30, 10, 45]
            ]
        },
        {
            "input":[32, 29, 19, 10, 17],
            "answer":5,
            "explanation":[
                [29, 10, 17],
                [32, 19]
            ]
        },
        {
            "input":[49, 50, 6, 3, 42, 30, 2],
            "answer":0,
            "explanation":[
                [50, 6, 3, 30, 2],
                [49, 42]
            ]
        }
    ]
}
