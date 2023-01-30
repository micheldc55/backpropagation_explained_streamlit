import streamlit

def write_derivative_definition_latex(streamlit_column):
    """Write the definition of a derivative in LaTeX.

    :param streamlit_column: Column on which to plot
    :type streamlit_column: streamlit column
    """
    streamlit_column.latex(r"""\frac{df}{dx} = f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}""")

def derive_example_derivative():
    """Derive the expression for the derivative of x^2 + 1 in LaTeX.
    """
    streamlit.latex(r"""f(x) = x^{2} + 1""")
    streamlit.latex(r"""\frac{df}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}""")
    streamlit.latex(r"""f(x + h) = (x + h)^{2} + 1 | f(x) = x^{2} + 1""")
    streamlit.latex(r"""\Rightarrow \frac{(x + h)^{2} + 1 - (x^{2} + 1)}{h}""")
    streamlit.latex(r"""\Rightarrow \frac{x^{2} + 2hx + h^{2} + 1 - x^{2} - 1}{h}""")
    streamlit.latex(r"""\Rightarrow \frac{2hx + h^{2}}{h}""")
    streamlit.latex(r"""\Rightarrow 2x + h \Rightarrow 2x""")

def write_numerical_approximation_derivate(streamlit_col):
    """Write the LaTeX derivation of the numerical approximation of a derivative.

    :param streamlit_column: Column on which to plot
    :type streamlit_column: streamlit column
    """
    streamlit_col.latex(r"""\frac{df}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}""")
    streamlit_col.latex(r"""\text{If we approximate h} \approx \Delta{x} \text{, where } \Delta{x} \text{ is a very small number: }""")
    streamlit_col.latex(r"""\frac{df}{dx} \approx \frac{f(x + \Delta{x}) - f(x)}{\Delta{x}}""")
    streamlit_col.latex(r"""\text{If we take } \Delta{x} = 0.001""")
    streamlit_col.latex(r"""\frac{df}{dx} \approx \frac{f(x + 0.001) - f(x)}{0.001}""")

def compare_num_derivative_vs_math_derivative__math_derivative(streamlit_col):
    """Write the LaTeX comparison between the numerical derivative and the mathematical counterpart. This does the mathematical part

    :param streamlit_column: Column on which to plot
    :type streamlit_column: streamlit column
    """
    streamlit_col.latex(r"""\text{Let p=1 be the point on which we want to calculate the derivative}""")
    streamlit_col.latex(r"""\text{Then the derivative of } x^{2} + 1 \text{ is: 2x, which evaluated at x=1 equals 2}""")
    streamlit_col.latex(r"""\text{In other words, } f'(1) = 2""")

def compare_num_derivative_vs_math_derivative__num_derivative(streamlit_col):
    """Write the LaTeX comparison between the numerical derivative and the mathematical counterpart. This does the numerical part

    :param streamlit_column: Column on which to plot
    :type streamlit_column: streamlit column
    """
    streamlit_col.latex(r"""\text{We start from the numerical approximation we stated above for h = 0.001}""")
    streamlit_col.latex(r"""\frac{df}{dx} \approx \frac{f(x + 0.001) - f(x)}{0.001}""")
    streamlit_col.latex(r"""\frac{df}{dx} \approx \frac{(x + 0.001)^{2} + 1 - (x^{2} + 1)}{0.001}""")
    streamlit_col.latex(r"""\text{The math is left to the user so that we don't have to write so many steps...}""")
    streamlit_col.latex(r"""\frac{df}{dx} \approx \frac{2 * 0.001 * x + 0.001^{2}}{0.001}""")
    streamlit_col.latex(r"""\frac{df}{dx} \approx 2 * x + 0.001""")
    streamlit_col.latex(r"""\text{If x = 1, then f'(x) } \approx \text{2.001}""")


def chain_rule_definition_and_example(streamlit_col):
    """Writes the mathematical definition of the chain rule and applies it to y = 4u and u = 2x

    :param streamlit_column: Column on which to plot
    :type streamlit_column: streamlit column
    """
    streamlit_col.latex(r"""\frac{dy}{dx} = \frac{dy}{du}.\frac{du}{dx}""")
    streamlit_col.latex(r"""\text{Now, let's imagine that } y = 4u\text{ and }u = 2x\text{ then we have:}""")
    streamlit_col.latex(r"""\frac{du}{dx} = 2\text{ and}""")
    streamlit_col.latex(r"""\frac{dy}{du} = 4""")
    streamlit_col.latex(r"""\text{So, }\Rightarrow \frac{dy}{dx} = \frac{dy}{du}.\frac{du}{dx} = (4) . (2) = 8""")