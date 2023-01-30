import streamlit
from streamlit_echarts import st_echarts
import numpy as np

def plot_interactive_parabola(x_values: np.array, a: float, b: float, c: float, y_minmax: list = [-20, 20]):
    y_values = a * x_values ** 2 + b * x_values + c

    x_vals = x_values.tolist()
    y_vals = y_values.tolist()

    data = [[x_val, y_val] for x_val, y_val in zip(x_vals, y_vals)]

    if b < 0:
        b = f'- {-b}'
    else:
        b = f'+ {b}'
    if c < 0:
        c = f'- {-c}'
    else:
        c = f'+ {c}'

    plot_text = f'f(x) = {a}*x^2 {b}*x {c}'

    option = {
    'title': {
        'text': 'Cuadratic Equation plot',
        'left': 'left'
    },
    'legend': {
        'data': [plot_text],
        'left': 'right'
    },
    'tooltip': {
        'trigger': 'axis',
        'formatter': 'Function : <br/>{c}'
    },
    'grid': {
        'left': '3%',
        'right': '4%',
        'bottom': '3%',
        'containLabel': True
    },
    'xAxis': {
        'type': 'category',
        'axisLabel': {
        'formatter': 'x={value}'
        },
    },
    'yAxis': {
        'type': 'value',
        'axisLine': { 'onZero': False },
        'boundaryGap': False,
        'min': y_minmax[0],
        'max': y_minmax[1],
        'splitNumber': 10
    },
    'series': [
        {
        'name': plot_text,
        'type': 'line',
        'symbolSize': 10,
        'symbol': 'circle',
        'smooth': True,
        'lineStyle': {
            'width': 3,
            'shadowColor': 'rgba(0,0,0,0.3)',
            'shadowBlur': 10,
            'shadowOffsetY': 8
        },
        'data': data
        }
    ]
    }

    st_echarts(options=option, width=600, height=500)


def test_parabola(x: float or np.array) -> float or np.array:
    """Function that builds a test parabola of X**2 + 1

    :param x: Input to pass to the function. Can be a scalar or a numpy array.
    :type x: float or np.array
    :return: The output of squaring the input and adding 1.
    :rtype: float or np.array
    """
    return x**2 + 1

def line_between_two_points(xy_two_points: tuple, x: float) -> float:
    """Using the definition of a line that goes through 2 points P1 = (x1, y1) and P2 = (x2, y2), the function outputs the 
    y value of the line that passes through P1 and P2 evaluated at "x".

    :param xy_two_points: Tuple in the format: (x1, x2, y1, y2) from the two points that the line has to go through.
    :type xy_two_points: tuple
    :param x: Point in which you want to evaluate the line.
    :type x: float
    :return: The line evaluated at x. This line passes through P1 and P2.
    :rtype: float
    """
    x1, x2, y1, y2 = xy_two_points

    slope = (y2 - y1) / (x2 - x1)
    intercept = y2 - slope * x2

    return slope * x + intercept

def plot_parabola_for_concept_of_derivative(x: float, h: float):
    """Function that plots the parabola and plots the line between a point x and a point x + h

    :param h: Step in the derivative definition
    :type h: float
    """

    x_values = np.arange(-2, 2.25, 0.25)
    y_values_parabola = test_parabola(x_values)

    data_parabola = [[x_val, y_val] for x_val, y_val in zip(x_values, y_values_parabola)]
    
    inputs  = np.array([x, x+h])
    outputs = test_parabola(inputs)

    x1, x2, y1, y2 = (inputs[0], inputs[1], outputs[0], outputs[1])

    x_line = [x - 10, x, x + h, x + 10]
    y_line = [line_between_two_points([x1, x2, y1, y2], x) for x in x_line]

    data_line = [[x_val, y_val] for x_val, y_val in zip(x_line, y_line)]

    data_derivative = [[x_val, y_val] for x_val, y_val in zip(inputs, outputs)]

    option = {
        # dataset: [
        # {
        #     id: 'dataset_raw',
        #     source: _rawData
        # },
        # {
        #     id: 'dataset_since_1950_of_germany',
        #     fromDatasetId: 'dataset_raw',
        #     transform: {
        #     type: 'filter',
        #     config: {
        #         and: [
        #         { dimension: 'Year', gte: 1950 },
        #         { dimension: 'Country', '=': 'Germany' }
        #         ]
        #     }
        #     }
        # },
        # {
        #     id: 'dataset_since_1950_of_france',
        #     fromDatasetId: 'dataset_raw',
        #     transform: {
        #     type: 'filter',
        #     config: {
        #         and: [
        #         { dimension: 'Year', gte: 1950 },
        #         { dimension: 'Country', '=': 'France' }
        #         ]
        #     }
        #     }
        # }
        # ],
        'title': {
        'text': 'Finding the derivative at a point x analytically'
        },
        'tooltip': {
        'trigger': 'axis'
        },
        'xAxis': {
        'type': 'value',
        'nameLocation': 'middle',
        'min': -2,
        'max': 2
        },
        'yAxis': {
        'min': 0,
        'max': 5
        },
        'series': [
        {
            'type': 'line',
            'data': data_parabola,
            'showSymbol': False,
        },
        {
            'type': 'line',
            'data': data_line,
            'showSymbol': False,
        }
        ]
    }

    st_echarts(options=option, width=600, height=500)