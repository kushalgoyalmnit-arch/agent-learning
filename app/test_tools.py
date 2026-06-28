from tools import get_time
from tools import calculator
from tools import get_day

print(
    get_time.invoke({})
)

print(
    get_day.invoke({})
)

print(
    calculator.invoke(
        {
            "expression": "25*37"
        }
    )
)